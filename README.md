# 🤖 Inteligencia Artificial - 2026

<div align="center">
  <img src="img/IA.jpg" alt="IA Banner" width="100%" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

> **Repositorio de actividades, prácticas, códigos y proyectos de la materia de Inteligencia Artificial.**  
> *10mo Semestre — Ingeniería en Sistemas Computacionales*  
> **Alumno:** Daniels John Altamirano Ramírez  
> **Docente:** Jesús Eduardo Alcaraz Chávez  

---

## 📚 Sobre este Repositorio

Este espacio reúne los trabajos teóricos, análisis de datos, algoritmos de aprendizaje automático y proyectos prácticos desarrollados a lo largo del curso. Los contenidos se encuentran estructurados por unidades temáticas y proyectos aplicados.

---

## 📂 Estructura General del Repositorio

```text
IA-2026/
├── Unidad 1/                          # Introducción, Búsqueda Informada y Análisis
│   ├── Analisis_datos_Dino Crash.md   # Planteamiento de variables y análisis de telemetría
│   └── Evaluacion A(estrella).pdf     # Evaluación del algoritmo de búsqueda heurística A*
│
├── Unidad 2/                          # Modelos de Clasificación y Redes Neuronales
│   ├── Actividades/
│   │   └── actividad_arboles_de_decision.md # Árboles de decisión vs Perceptrón Multicapa
│   ├── Perceptron/                    # MLP implementado en lenguaje C (Problema XOR)
│   │   ├── percep.c
│   │   ├── percep.exe
│   │   └── README.md
│   └── Pygame MLP/                    # Juego con agente inteligente entrenado con MLP
│       ├── juego_pygame_mlp1.py
│       ├── datos_mlp.csv
│       ├── assets/
│       ├── lib/
│       └── README.md
│
├── Proyectos/                         # Proyectos integradores de IA
│   └── Reconocimiento Facial/         # Visión por computadora y biométrica facial
│       ├── 1_capturar_rostros.py      # Captura asistida de dataset
│       ├── 2_entrenar_modelo.py       # Entrenamiento con Eigenfaces, LBPH y Fisherfaces
│       ├── 3_reconocimiento.py        # Reconocimiento facial en tiempo real vía Webcam
│       ├── labels.json                # Mapa de etiquetas / identidades
│       ├── data/                      # Haar Cascades para detección facial
│       ├── dataset/                   # Muestras biométricas normalizadas
│       └── README.md
│
├── Libros y Recursos/                 # Bibliografía y material de consulta
│   ├── IA/                            # Russell & Norvig: Un Enfoque Moderno
│   ├── Videojuegos/                   # Desarrollo de videojuegos (Fernando Sansberro)
│   └── Python/                        # Manuales y guías de programación en Python
│
├── img/                               # Recursos gráficos del repositorio
└── .gitignore                         # Reglas de exclusión de git
```

---

## 📑 Índice Detallado de Contenidos

### 🔹 [Unidad 1](./Unidad%201) — Conceptos Básicos y Búsqueda
- **[Análisis de datos — Operación Dino Crash](./Unidad%201/Analisis_datos_Dino%20Crash.md):** Formulación de variables objetivo ($Y$) y predictoras ($X$), granularidad y riesgos de fuga de datos para aprendizaje automático en un videojuego tipo runner.
- **[Evaluación Algoritmo A*](./Unidad%201/Evaluacion%20A(estrella).pdf):** Análisis teórico y práctico sobre heurísticas y búsqueda informada en grafos.

### 🔹 [Unidad 2](./Unidad%202) — Árboles de Decisión y Redes Neuronales
- **[Actividad: Árboles de Decisión](./Unidad%202/Actividades/actividad_arboles_de_decision.md):** Comparativa entre modelos basados en reglas lógicas y redes neuronales densas (pesos, sesgos y retropropagación). Aplicación a casos reales: fraudes bancarios, deserción escolar, triage médico y crédito bancario.
- **[Perceptrón Multicapa en C](./Unidad%202/Perceptron):** Implementación desde cero de una red neuronal 2-2-1 con activación sigmoidal y Backpropagation para resolver la compuerta lógica no lineal XOR.
- **[Pygame MLP](./Unidad%202/Pygame%20MLP):** Videojuego interactivo en Pygame que registra telemetría de salto en `datos_mlp.csv` y permite alternar a un modo autónomo controlado por un `MLPClassifier` de Scikit-Learn.

### 🔹 [Proyectos](./Proyectos) — Visión Computacional Aplicada
- **[Reconocimiento Facial en Tiempo Real](./Proyectos/Reconocimiento%20Facial):** Pipeline completo en OpenCV con detección mediante Viola-Jones (Haar Cascades) y reconocimiento biométrico entrenado con Eigenfaces (PCA), LBPH y Fisherfaces (LDA).

### 🔹 [Libros y Recursos](./Libros%20y%20Recursos) — Bibliografía
- **[IA](./Libros%20y%20Recursos/IA):** *Inteligencia Artificial: Un Enfoque Moderno* (Stuart J. Russell & Peter Norvig).
- **[Videojuegos](./Libros%20y%20Recursos/Videojuegos):** Guías completas de Game Development y diseño de carreras de videojuegos.
- **[Python](./Libros%20y%20Recursos/Python):** Libros de fundamentos de computación y programación con Python.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguajes:** Python 3.x, C (GCC / MinGW).
- **Librerías de IA y Visión:** OpenCV (`opencv-contrib-python`), Scikit-Learn, NumPy.
- **Visualización y Gráficos:** Matplotlib, Pygame.
- **Herramientas de Entorno:** Git, GitHub, VS Code.

---

<div align="center">
  <i>Daniels John Altamirano Ramírez — 2026</i>
</div>
