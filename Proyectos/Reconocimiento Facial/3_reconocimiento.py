import cv2 as cv
import os
import json

def reconocer_rostros():
    print("=" * 60)
    print("      RECONOCIMIENTO FACIAL EN TIEMPO REAL CON WEBCAM     ")
    print("=" * 60)

    # Cargar etiquetas
    if not os.path.exists("labels.json"):
        print("Error: No se encontró 'labels.json'. Ejecuta primero '2_entrenar_modelo.py' para entrenar.")
        return

    with open("labels.json", "r", encoding="utf-8") as f:
        # json almacena las llaves como strings ("0", "1", ...)
        raw_labels = json.load(f)
        labels = {int(k): v for k, v in raw_labels.items()}

    print(f"Personas registradas en el modelo: {list(labels.values())}")

    # Seleccionar modelo (prioriza Eigenface que es el objetivo de la clase)
    modelo_path = "modeloEigenface.xml"
    tipo_modelo = "Eigenfaces"
    umbral_desconocido = 4500  # En Eigenfaces distancias mayores suelen ser desconocidos

    if not os.path.exists(modelo_path):
        if os.path.exists("modeloLBPH.xml"):
            modelo_path = "modeloLBPH.xml"
            tipo_modelo = "LBPH"
            umbral_desconocido = 75
        elif os.path.exists("laloEigenface.xml"):
            modelo_path = "laloEigenface.xml"
            tipo_modelo = "Eigenfaces"
            umbral_desconocido = 4500
        else:
            print("Error: No se encontró ningún archivo de modelo (.xml).")
            print("Asegúrate de ejecutar el script de entrenamiento primero.")
            return

    print(f"Cargando modelo '{tipo_modelo}' desde: {modelo_path}")

    if tipo_modelo == "Eigenfaces":
        face_recognizer = cv.face.EigenFaceRecognizer_create()
    elif tipo_modelo == "LBPH":
        face_recognizer = cv.face.LBPHFaceRecognizer_create()
    else:
        face_recognizer = cv.face.FisherFaceRecognizer_create()

    face_recognizer.read(modelo_path)

    # Cargar clasificador Haar
    cascade_path = os.path.join("data", "haarcascade_frontalface_alt.xml")
    if not os.path.exists(cascade_path):
        cascade_path = os.path.join("data", "haarcascade_frontalface_default.xml")

    face_cascade = cv.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print(f"Error: No se pudo cargar el clasificador Haar en {cascade_path}.")
        return

    # Iniciar cámara
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara web.")
        return

    print("\nIniciando reconocimiento en tiempo real...")
    print("Recuerda: Confidence es disimilitud (más bajo = mejor match).")
    print("Presiona 'q' o 'ESC' para cerrar la ventana.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(60, 60)
        )

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            roi_resized = cv.resize(roi, (100, 100), interpolation=cv.INTER_CUBIC)

            # Predecir rostro
            label, confidence = face_recognizer.predict(roi_resized)

            # Determinar si se reconoce o es desconocido según la distancia
            if confidence < umbral_desconocido and label in labels:
                nombre = labels[label]
                color = (0, 255, 0) # Verde
                texto_etiqueta = f"{nombre} ({int(confidence)})"
            else:
                nombre = "Desconocido"
                color = (0, 0, 255) # Rojo
                texto_etiqueta = f"{nombre} ({int(confidence)})"

            # Dibujar caja y etiqueta
            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv.rectangle(frame, (x, y - 30), (x + w, y), color, -1)
            cv.putText(frame, texto_etiqueta, (x + 5, y - 8),
                       cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        # Información general en pantalla
        cv.putText(frame, f"Modelo: {tipo_modelo}", (20, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv.putText(frame, "Presiona 'q' para salir", (20, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv.imshow("Reconocimiento Facial en Tiempo Real", frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break

    cap.release()
    cv.destroyAllWindows()
    print("Reconocimiento finalizado.")

if __name__ == "__main__":
    reconocer_rostros()
