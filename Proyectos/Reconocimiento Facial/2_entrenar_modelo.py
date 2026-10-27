import cv2 as cv
import numpy as np
import os
import json

def entrenar_modelo():
    print("=" * 60)
    print("        ENTRENAMIENTO DEL MODELO DE RECONOCIMIENTO        ")
    print("=" * 60)

    # Buscar la carpeta del dataset (dataset o pruebacaras)
    dataset_dir = "dataset"
    if not os.path.exists(dataset_dir) and os.path.exists("pruebacaras"):
        dataset_dir = "pruebacaras"

    if not os.path.exists(dataset_dir):
        print(f"Error: No se encontró la carpeta '{dataset_dir}'.")
        print("Ejecuta primero el script '1_capturar_rostros.py' para registrar personas.")
        return

    personas = sorted([p for p in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, p))])
    if len(personas) == 0:
        print(f"Error: La carpeta '{dataset_dir}' no contiene subcarpetas de personas.")
        return

    print(f"Directorio de dataset: '{dataset_dir}'")
    print("Personas encontradas:", personas)

    labels = []
    faces_data = []
    label_map = {}
    label_id = 0

    target_size = (100, 100)

    for person in personas:
        person_path = os.path.join(dataset_dir, person)
        label_map[label_id] = person
        img_count = 0

        for img_name in sorted(os.listdir(person_path)):
            if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            img_path = os.path.join(person_path, img_name)
            # Cargar en escala de grises (flag 0)
            img = cv.imread(img_path, 0)
            if img is None:
                continue

            # Asegurar que todas las imágenes tengan exactamente 100x100
            if img.shape != target_size:
                img = cv.resize(img, target_size, interpolation=cv.INTER_CUBIC)

            labels.append(label_id)
            faces_data.append(img)
            img_count += 1

        print(f"  [+] {person} (label={label_id}): {img_count} imágenes cargadas")
        label_id += 1

    if len(faces_data) == 0:
        print("Error: No se encontraron imágenes válidas para entrenar.")
        return

    print(f"\nTotal de imágenes para entrenamiento: {len(faces_data)}")
    print(f"Dimensiones de cada rostro: {target_size[0]}x{target_size[1]} píxeles")

    # Guardar mapeo de etiquetas en JSON para el script de reconocimiento
    with open("labels.json", "w", encoding="utf-8") as f:
        json.dump(label_map, f, ensure_ascii=False, indent=4)
    print("Mapa de etiquetas guardado en: labels.json")

    # 1. Entrenamiento con Eigenfaces (Método principal de la actividad)
    print("\nEntrenando con EigenFaceRecognizer (PCA / Vectores propios)...")
    eigen_recognizer = cv.face.EigenFaceRecognizer_create()
    eigen_recognizer.train(faces_data, np.array(labels))
    modelo_eigen_path = "modeloEigenface.xml"
    eigen_recognizer.write(modelo_eigen_path)
    print(f"  -> Modelo Eigenface guardado exitosamente en: '{modelo_eigen_path}'")

    # 2. Entrenamiento con LBPH (Excelente para variaciones de iluminación)
    print("\nEntrenando con LBPHFaceRecognizer...")
    lbph_recognizer = cv.face.LBPHFaceRecognizer_create()
    lbph_recognizer.train(faces_data, np.array(labels))
    modelo_lbph_path = "modeloLBPH.xml"
    lbph_recognizer.write(modelo_lbph_path)
    print(f"  -> Modelo LBPH guardado exitosamente en: '{modelo_lbph_path}'")

    # 3. Entrenamiento con Fisherfaces (Requiere al menos 2 personas / clases distintas)
    if len(personas) >= 2:
        print("\nEntrenando con FisherFaceRecognizer (LDA)...")
        fisher_recognizer = cv.face.FisherFaceRecognizer_create()
        fisher_recognizer.train(faces_data, np.array(labels))
        modelo_fisher_path = "modeloFisherface.xml"
        fisher_recognizer.write(modelo_fisher_path)
        print(f"  -> Modelo Fisherface guardado exitosamente en: '{modelo_fisher_path}'")
    else:
        print("\n[Nota] FisherFaceRecognizer requiere al menos 2 personas diferentes para entrenar.")

    print("\n" + "=" * 60)
    print("¡Entrenamiento finalizado con éxito!")
    print("Ahora puedes ejecutar '3_reconocimiento.py' para probar en vivo con tu webcam.")
    print("=" * 60)

if __name__ == "__main__":
    entrenar_modelo()