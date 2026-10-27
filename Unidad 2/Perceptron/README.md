# 🧠 Perceptrón Multicapa en C (MLP - XOR)

Implementación en lenguaje C de una Red Neuronal Artificial de tipo **Perceptrón Multicapa (Multilayer Perceptron - MLP)** entrenada mediante el algoritmo de **Retropropagación del Error (Backpropagation)** para resolver la compuerta lógica no lineal **XOR**.

---

## 📐 Arquitectura de la Red
- **Capa de entrada:** 2 neuronas ($x_0, x_1$).
- **Capa oculta:** 2 neuronas con sesgos ($BiasOculta$).
- **Capa de salida:** 1 neurona con sesgo ($BiasSalida$).
- **Función de activación:** Sigmoide logística $\sigma(s) = \frac{1}{1 + e^{-s}}$.
- **Tasa de aprendizaje ($K$):** 0.2.
- **Épocas de entrenamiento:** 80,000.

---

## 🎯 Problema XOR
La compuerta lógica XOR es linealmente inseparable, por lo que un perceptrón simple de una sola capa no puede clasificarla:

| Entrada 1 ($x_0$) | Entrada 2 ($x_1$) | Salida Esperada ($y$) |
|:-----------------:|:-----------------:|:---------------------:|
| 0                 | 0                 | 0                     |
| 0                 | 1                 | 1                     |
| 1                 | 0                 | 1                     |
| 1                 | 1                 | 0                     |

---

## ⚙️ Compilación y Ejecución

### Opción 1: Ejecutar el binario precompilado
```cmd
percep.exe
```

### Opción 2: Compilar desde el código fuente con GCC
```bash
gcc percep.c -o percep.exe -lm
./percep.exe
```

---

## 📄 Archivos
- `percep.c`: Código fuente en C con la lógica de inicialización aleatoria de pesos, propagación hacia adelante (forward pass) y ajuste de gradientes hacia atrás (backpropagation).
- `percep.exe`: Binario ejecutable compilado para Windows.
