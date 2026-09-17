# Análisis de datos — Operación Dino Crash

## 1. Misión 1 - Problema y dataset

Antes de lanzar cualquier algoritmo, se debe traducir el juego a filas y columnas con sentido. A continuación muestro mi análisis de los tres escenarios planteados:

### P1 — ¿Morirá en el siguiente frame?
- **Y (Variable Objetivo):** `die_next_frame` (Binaria: 1 si muere en el *siguiente* instante, 0 si no). La columna `died` actual no sirve por sí sola porque nos avisa cuando ya es tarde.
- **X (mínimo 5 variables):**
  1. `speed` (Numérica): Ya que a mayor velocidad, menos tiempo de reacción.
  2. `dist_obstacle` (Numérica):  Para saber qué tan cerca está el obstaculo.
  3. `obstacle_type` (Categórica): Ya que no es lo mismo saltar un cactus pequeño que un pájaro alto.
  4. `is_jumping` (Binaria): Estado actual del dinosaurio.
  5. `dino_y_position` (Numérica): *Columna nueva sugerida*. Saber la altura exacta es vital para saber si choca con un pájaro o lo esquiva.
- **Granularidad:** Un frame por cada iteración del juego (ej. cada 16ms / 60fps). 
- **Tamaño mínimo de dataset:** Unas 500 partidas (aprox. 100,000 frames). Necesitamos ver suficientes "muertes" para que el modelo aprenda, no solo frames de supervivencia.
- **Riesgo:** Si dejamos la variable `died` en el frame exacto de la muerte, el modelo aprenderá a predecir la muerte cuando la distancia al obstáculo sea 0 (físicamente ya chocó). No predecirá, solo describirá.

### P2 — ¿Cuántos puntos alcanzará esta partida al morir?
- **Y:** `final_score` (Numérica continua).
- **X:** `player_id`, `time_of_day`, `device_type` (móvil/PC), `avg_past_scores`, `is_first_game_of_session`.
- **Granularidad:** Una partida completa = Una fila.
- **Tamaño mínimo:** 1,000 a 2,000 partidas para captar la varianza entre jugadores buenos y malos.
- **Riesgo:** Incluir variables que ocurren *durante* el juego (como `max_speed_reached`). Eso sería hacer trampa, porque no conoceríamos ese dato antes de que empiece la partida.

### P3 — ¿Qué tipo de obstáculo viene próximo?
- **Y:** `next_obstacle_type` (Categórica multiclase: none, cactus_small, cactus_large, bird).
- **X:** `current_score`, `current_speed`, `time_since_last_obstacle`, `last_obstacle_type`, `random_seed_if_available`.
- **Granularidad:** Un evento (cada vez que un obstáculo sale de la pantalla, generamos una fila para predecir el siguiente).
- **Tamaño mínimo:** Unos 5,000 obstáculos registrados.
- **Riesgo:** Si el juego genera los obstáculos de forma 100% aleatoria (RNG puro), ningún modelo servirá de nada y solo estaremos modelando ruido.

---

## 2. Diccionario y muestra (Misión 2)

Revisando la telemetría interceptada de la sesión 7:

- **Patrón en `died=1` (frame 82):** El dinosaurio muere porque `dist_obstacle` bajó a 12 píxeles, venía un `cactus_small`, y la variable `jump` era 0. Es decir, se estrelló por no saltar a tiempo.
- **¿`score` es buena variable para P1?:** No de forma directa. El puntaje (`score=120`) es un proxy del tiempo que lleva vivo y de la velocidad, pero no te dice nada sobre si está a punto de chocar en ese milisegundo. Usar el `score` solo confundiría al modelo.
- **¿Falta alguna columna?:** Sí, faltan columnas críticas espaciales. Además de la altura del dino (`dino_y`), falta saber si está agachado (`is_ducking`) y las dimensiones del obstáculo (ancho y alto).
- **¿`died` sirve para P1?:** No. Como está definida, `died=1` describe la pantalla de "Game Over". Para *predecir*, necesitamos crear una columna llamada `target_die_next_frame` desplazando `died` un frame hacia atrás.

---

## 3. Checklist EDA (Misión 3)

Elegí tres preguntas clave de la checklist para P1:

1. **¿La clase objetivo está balanceada? (Q3):** Definitivamente no. El 99% del tiempo el dino está vivo (clase 0). Si el EDA me muestra esto, evito usar *Accuracy* (exactitud) como métrica y recurro a técnicas de balanceo o pesos de clase.
2. **¿Hay valores faltantes? (Q2):** Probablemente en `dist_obstacle` cuando no hay ningún obstáculo en pantalla (`obstacle_type = none`). Si veo NAs allí, no puedo usar una regresión lineal básica o un Random Forest sin antes imputar ese valor (ej. poner un número gigante como 9999).
3. **¿Outliers? (Q7):** Podríamos tener saltos imposibles o valores de `dist_obstacle` negativos si el dino atraviesa el cactus un par de píxeles antes de que el motor gráfico registre la muerte. Esto habría que limpiarlo.

**Sobre la pregunta 8 (Datos i.i.d. e Independencia):**
Mezclar frames de la misma partida entre entrenamiento y prueba es un error grave. El frame 80 y el 81 son casi idénticos. Si el modelo ve el 80 en entrenamiento, "memorizará" el contexto y acertará el 81 en prueba no porque sea inteligente, sino porque hizo trampa. La separación debe ser por `session_id`.

**Ejemplo de Data Leakage con `time_ms`:**
Si incluimos `total_session_time_ms` (el tiempo que duró toda la partida) como variable predictora para saber si muere en el frame actual. El modelo aprendería: "Si `time_ms` actual se acerca a `total_session_time_ms`, entonces muere". ¡Pero en la vida real no sabemos cuánto va a durar la partida!

---

## 4. Interpretación de resúmenes (Misión 4)

Con base en la tabla estadística (12,000 frames, 50 partidas):

- **Desbalance:** Tenemos 50 unos (muertes) en 12,000 frames. Esto significa que la clase positiva representa apenas el **0.41%** de los datos.
- **Métricas:** Con este desbalance extremo, la métrica de *Accuracy* no sirve (predecir siempre "no muere" daría 99.59% de exactitud). Deberíamos usar **Recall** (queremos encontrar todos los choques inminentes) o el **F1-Score**.
- **Utilidad de `dist_obstacle`:** Es altamente predictiva. La media general es 95 píxeles, pero las notas dicen que "muertes suelen con dist < 20". Es una frontera de decisión clarísima.
- **Distribución de `score`:** Una "cola larga hacia la derecha" indica que la mayoría muere rápido (scores bajos), y unos pocos llegan muy lejos. Si usáramos esto para regresión, una simple regresión lineal fallaría porque los datos no son normales; requeriría aplicar un logaritmo (`log(score)`) para normalizar la curva.

---

## 5. Elección de modelo (Misiones 5–6)

### Tabla de Escenarios
| Escenario | Tras tu EDA, ¿qué fila aplica? | Modelo Propuesto | 2 Condiciones a cumplir |
| :--- | :--- | :--- | :--- |
| **P1** | Y binaria muy desbalanceada | Random Forest con pesos de clase (`class_weight`) | 1. Features desplazadas (Y en t+1). 2. Split por `session_id`. |
| **P2** | Y numérica (score final) | Regresión Lineal Robusta o Random Forest Regressor | 1. Datos agregados por partida, no por frame. 2. `score` normalizado (log). |
| **P3** | Y categórica multiclase | XGBoost (Clasificador multiclase) | 1. Clases balanceadas o ponderadas. 2. Secuencia lógica demostrable. |

### Contraejemplos
- **¿Cuándo desaconsejar un Árbol Profundo para P1?** Aunque un árbol capta reglas complejas, el EDA nos dijo que solo hay 50 muertes en 12,000 frames. Un árbol profundo creará hojas específicas para cada una de esas 50 muertes (overfitting extremo) y fallará en la partida 51.
- **¿Cuándo usar una Red Neuronal?** Solo tendría sentido si en el EDA descartamos los datos tabulares y decidimos alimentar el modelo con capturas de pantalla (píxeles) del juego usando Redes Convolucionales (CNN), comprobando que tenemos cientos de miles de imágenes y recursos de GPU.
- **Reglas fijas vs Machine Learning para P1:** Podríamos usar la regla `IF dist_obstacle < 15 AND jump=0 THEN death`. La ventaja es que es 100% interpretable y sin costo computacional. ¿El límite? A medida que aumenta el `speed` en el juego, la distancia crítica ya no será 15, será 30 o 45. Un modelo de ML capta esa interacción (`dist_obstacle` *vs* `speed`) automáticamente, mientras que la regla fija se rompe al acelerar.

---

## 6. Síntesis
El análisis EDA demuestra que el juego del dinosaurio no es un problema de "aplicar IA por aplicar". Antes que cualquier modelo, pediría un dataset tabular por frames con variables espaciales (`dino_y`), separando estrictamente por `session_id` y desplazando la variable `died` un frame al futuro para evitar la filtración de datos. Solo después de aislar el masivo desbalance de clases (0.41%), plantearía un ensamble ligero, como Random Forest, capaz de aprender umbrales de colisión variables según la velocidad.