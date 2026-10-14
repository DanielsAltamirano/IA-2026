import cv2 as cv
import os
import time

def capturar_rostros():
    print("=" * 60)
    print("      CAPTURADOR DE ROSTROS PARA DATASET (100x100)      ")
    print("=" * 60)

    nombre_persona = input("Ingresa el nombre de la persona a registrar: ").strip()
    if not nombre_persona:
        print("El nombre no puede estar vacío.")
        return

    # Carpeta del dataset
    dataset_dir = "dataset"
    persona_dir = os.path.join(dataset_dir, nombre_persona)
    os.makedirs(persona_dir, exist_ok=True)

    # Contar fotos ya existentes para no sobreescribir
    fotos_existentes = [f for f in os.listdir(persona_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    contador = len(fotos_existentes)
    total_fotos_a_tomar = 200  # Cantidad recomendada para un buen entrenamiento

    print(f"\nGuardando imágenes en: {persona_dir}")
    print(f"Fotos ya existentes: {contador}")
    print(f"Meta de fotos a tomar en esta sesión: {total_fotos_a_tomar}")
    print("\nInstrucciones:")
    print(" - Mira a la cámara de frente, luego rota levemente la cabeza.")
    print(" - Haz diferentes expresiones (serio, sonriendo, etc.) y varía un poco la distancia.")
    print(" - Presiona la tecla 'q' o 'ESC' en cualquier momento para salir.")
    print("Iniciando cámara en 2 segundos...")
    time.sleep(2)

    # Cargar clasificador Haar
    cascade_path = os.path.join("data", "haarcascade_frontalface_alt.xml")
    if not os.path.exists(cascade_path):
        cascade_path = os.path.join("data", "haarcascade_frontalface_default.xml")
    
    if not os.path.exists(cascade_path):
        print(f"Error: No se encontró el archivo Haar Cascade en 'data/'.")
        return

    face_cascade = cv.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print("Error: No se pudo cargar el clasificador Haar.")
        return

    # Iniciar captura de video (probar DirectShow en Windows para evitar lentitud)
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se detectó ninguna cámara web disponible.")
        return

    capturadas_esta_sesion = 0
    frame_interval = 2  # Capturar cada 2 frames para dar tiempo de variar la pose
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el fotograma de la cámara.")
            break

        frame_count += 1
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_display = frame.copy()

        # Detección de rostros
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(60, 60)
        )

        for (x, y, w, h) in faces:
            # Dibujar recuadro en el rostro detectado
            cv.rectangle(frame_display, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Tomar muestra cada cierto intervalo si no se ha alcanzado la meta
            if frame_count % frame_interval == 0 and capturadas_esta_sesion < total_fotos_a_tomar:
                # Recorte del rostro (ROI)
                roi = gray[y:y+h, x:x+w]

                # Redimensionar a 100x100 tal como requiere la actividad
                roi_resized = cv.resize(roi, (100, 100), interpolation=cv.INTER_CUBIC)

                contador += 1
                capturadas_esta_sesion += 1
                img_name = f"{contador:03d}.jpg"
                img_path = os.path.join(persona_dir, img_name)
                cv.imwrite(img_path, roi_resized)

        # Información en pantalla
        cv.putText(frame_display, f"Persona: {nombre_persona}", (20, 35),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv.putText(frame_display, f"Fotos: {capturadas_esta_sesion}/{total_fotos_a_tomar} (Total: {contador})", (20, 70),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv.putText(frame_display, "Presiona 'q' para salir", (20, 105),
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)

        # Barra de progreso visual
        progreso = int((capturadas_esta_sesion / total_fotos_a_tomar) * 300)
        cv.rectangle(frame_display, (20, 120), (320, 135), (80, 80, 80), -1)
        cv.rectangle(frame_display, (20, 120), (20 + progreso, 135), (0, 255, 0), -1)

        cv.imshow("Captura de Rostros para Entrenamiento", frame_display)

        key = cv.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            print("\nCaptura terminada por el usuario.")
            break

        if capturadas_esta_sesion >= total_fotos_a_tomar:
            print(f"\n¡Meta alcanzada! Se capturaron {capturadas_esta_sesion} fotos de {nombre_persona}.")
            break

    cap.release()
    cv.destroyAllWindows()
    print(f"Directorio finalizado: {persona_dir}")
    print("=" * 60)

if __name__ == "__main__":
    capturar_rostros()
