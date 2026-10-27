# 🎮 Videojuego con Red Neuronal MLP (Pygame + Scikit-Learn)

Simulación interactiva desarrollada en Python con **Pygame** donde un personaje aprende a esquivar proyectiles mediante un modelo de **Perceptrón Multicapa (`MLPClassifier`)**.

---

## 🕹️ Dinámica del Juego y Aprendizaje
1. **Fase de recolección de datos (Modo Manual):** El usuario juega controlando el salto del personaje. Cada frame registra:
   - Velocidad de la bala.
   - Distancia del personaje al proyectil.
   - Decisión de salto (1 = saltó, 0 = no saltó).
2. **Entrenamiento en memoria:** Al acumular muestras suficientes, se entrena un `MLPClassifier` con `StandardScaler`.
3. **Modo Automático (IA):** El modelo toma control del personaje en tiempo real prediciendo el momento óptimo para saltar en función de la velocidad y distancia de la bala.

---

## 📋 Requisitos e Instalación

```bash
pip install pygame scikit-learn matplotlib
```

---

## 🚀 Ejecución y Controles

```bash
python juego_pygame_mlp1.py
```

### Controles principales:
- `ESPACIO`: Saltar en modo manual.
- `A`: Alternar entre Modo Manual y Modo Automático (IA).
- `E`: Entrenar el modelo con los datos recolectados en la sesión.
- `G`: Guardar las muestras acumuladas en `datos_mlp.csv`.
- `V`: Visualizar gráficos de dispersión 2D/3D de las variables y decisiones tomadas.
- `R`: Reiniciar estado del juego.
- `ESC`: Salir.

---

## 📁 Archivos y Directorios
- `juego_pygame_mlp1.py`: Código principal del juego, ciclo de eventos, física y red neuronal.
- `datos_mlp.csv`: Conjunto de datos exportado con las muestras recolectadas durante las partidas.
- `assets/`: Sprites de animación, fondos y efectos de sonido.
- `lib/`: Librerías auxiliares (`phaser.min.js`, `synaptic.js`).
