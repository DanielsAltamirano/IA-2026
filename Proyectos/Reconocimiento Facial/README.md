# 👤 Proyecto: Reconocimiento Facial en Tiempo Real

Este proyecto implementa un sistema completo de visión por computadora para detección y reconocimiento de rostros en tiempo real utilizando la cámara web.

---

## 🛠️ Tecnologías y Algoritmos
- **OpenCV (`opencv-contrib-python`)**: Procesamiento de imagen y clasificadores.
- **Detección facial**: Algoritmo de Viola-Jones mediante Haar Cascades (`haarcascade_frontalface_alt.xml`).
- **Algoritmos de reconocimiento**:
  1. **Eigenfaces (PCA - Vectores Propios)**: Reduce dimensionalidad capturando las variaciones globales más significativas.
  2. **Fisherfaces (LDA - Análisis Discriminante Lineal)**: Maximiza la separación entre clases y minimiza la variación intraclasal.
  3. **LBPH (Local Binary Patterns Histograms)**: Robusto ante variaciones de iluminación local.

---

## 📋 Requisitos e Instalación
Se recomienda utilizar un entorno virtual con Python 3.9+:

```bash
pip install opencv-contrib-python numpy
```

> **Nota:** Es necesario instalar `opencv-contrib-python` (no la versión estándar `opencv-python`) para contar con el módulo `cv2.face`.

---

## 🚀 Flujo de Ejecución

El proyecto sigue una secuencia ordenada de 3 pasos:

### 1. Captura de Rostros
```bash
python 1_capturar_rostros.py
```
- Solicita el nombre de la persona a registrar.
- Abre la cámara web y detecta el rostro.
- Guarda 200 muestras recortadas y normalizadas a 100x100 píxeles en escala de grises dentro de `dataset/<Nombre>/`.

### 2. Entrenamiento del Modelo
```bash
python 2_entrenar_modelo.py
```
- Lee todas las imágenes registradas en `dataset/`.
- Asocia cada persona con un identificador numérico y guarda el diccionario en `labels.json`.
- Entrena los clasificadores `EigenFaceRecognizer`, `LBPHFaceRecognizer` y `FisherFaceRecognizer`.
- Genera los archivos de pesos `modeloEigenface.xml`, `modeloLBPH.xml` y `modeloFisherface.xml`.

### 3. Reconocimiento en Vivo
```bash
python 3_reconocimiento.py
```
- Carga las etiquetas (`labels.json`) y el modelo entrenado.
- Abre la cámara web, detecta los rostros presentes en cada fotograma y predice la identidad junto con la distancia/confianza.
- Dibuja el marco verde con el nombre del usuario reconocido o rojo si es desconocido.
- Presiona `ESC` o `q` para cerrar la ventana.

---

## 📁 Estructura del Directorio
- `1_capturar_rostros.py`: Script interactivo de captura.
- `2_entrenar_modelo.py`: Generador y extractor de modelos biométricos.
- `3_reconocimiento.py`: Clasificador en tiempo real con webcam.
- `labels.json`: Diccionario serializado de clases e identidades.
- `data/`: Modelos Haar Cascade oficiales de OpenCV para detección frontal de rostros.
- `dataset/`: Directorios con imágenes capturadas de cada participante.
- `.gitignore`: Evita subir modelos `.xml` pesados (>100MB) a GitHub.
