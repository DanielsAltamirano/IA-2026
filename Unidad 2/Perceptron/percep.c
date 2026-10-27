#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define epoca 80000
#define K 0.2f // Tasa de aprendizaje (Learning Rate)

// Prototipos de funciones
float EntNt(float, float, float);
float InitNt(float, float);
float sigmoide(float);
float d_sigmoide(float);
void pesos_initNt(void);

// Arquitectura de la red: 2 entradas -> 2 neuronas ocultas -> 1 neurona de salida
// Pesos y sesgos de la capa oculta
float PesosOculta[2][2]; // [entrada][neurona_oculta]
float BiasOculta[2];

// Pesos y sesgos de la capa de salida
float PesosSalida[2];    // [neurona_oculta]
float BiasSalida;

// Función de activación sigmoide logística
float sigmoide(float s) {
    return 1.0f / (1.0f + expf(-s));
}

// Derivada de la función sigmoide: s'(y) = y * (1 - y)
float d_sigmoide(float y) {
    return y * (1.0f - y);
}

// Inicialización de pesos y sesgos con valores aleatorios entre -1.0 y 1.0
void pesos_initNt(void) {
    int i, j;
    srand((unsigned int)time(NULL));
    for (i = 0; i < 2; i++) {
        BiasOculta[i] = (((float)rand() / (float)RAND_MAX) * 2.0f) - 1.0f;
        PesosSalida[i] = (((float)rand() / (float)RAND_MAX) * 2.0f) - 1.0f;
        for (j = 0; j < 2; j++) {
            PesosOculta[i][j] = (((float)rand() / (float)RAND_MAX) * 2.0f) - 1.0f;
        }
    }
    BiasSalida = (((float)rand() / (float)RAND_MAX) * 2.0f) - 1.0f;
}

// Función de entrenamiento con Retropropagación (Backpropagation)
float EntNt(float x0, float x1, float target) {
    // 1. PASO HACIA ADELANTE (Forward Pass)
    // Activación de la capa oculta
    float h[2];
    h[0] = sigmoide(x0 * PesosOculta[0][0] + x1 * PesosOculta[1][0] + BiasOculta[0]);
    h[1] = sigmoide(x0 * PesosOculta[0][1] + x1 * PesosOculta[1][1] + BiasOculta[1]);

    // Activación de la neurona de salida
    float net_out = h[0] * PesosSalida[0] + h[1] * PesosSalida[1] + BiasSalida;
    float out = sigmoide(net_out);

    // 2. RETROPROPAGACIÓN DEL ERROR (Backpropagation)
    float error = target - out;

    // Gradiente de la capa de salida
    float delta_salida = error * d_sigmoide(out);

    // Gradientes de la capa oculta
    float delta_h[2];
    delta_h[0] = (delta_salida * PesosSalida[0]) * d_sigmoide(h[0]);
    delta_h[1] = (delta_salida * PesosSalida[1]) * d_sigmoide(h[1]);

    // 3. ACTUALIZACIÓN DE PESOS Y SESGOS
    // Capa de salida
    PesosSalida[0] += K * delta_salida * h[0];
    PesosSalida[1] += K * delta_salida * h[1];
    BiasSalida     += K * delta_salida;

    // Capa oculta
    PesosOculta[0][0] += K * delta_h[0] * x0;
    PesosOculta[1][0] += K * delta_h[0] * x1;
    BiasOculta[0]     += K * delta_h[0];

    PesosOculta[0][1] += K * delta_h[1] * x0;
    PesosOculta[1][1] += K * delta_h[1] * x1;
    BiasOculta[1]     += K * delta_h[1];

    return out;
}

// Función para consultar la red entrenada (Inferencia / Forward pass sin entrenar)
float InitNt(float x0, float x1) {
    float h[2];
    h[0] = sigmoide(x0 * PesosOculta[0][0] + x1 * PesosOculta[1][0] + BiasOculta[0]);
    h[1] = sigmoide(x0 * PesosOculta[0][1] + x1 * PesosOculta[1][1] + BiasOculta[1]);

    float net_out = h[0] * PesosSalida[0] + h[1] * PesosSalida[1] + BiasSalida;
    return sigmoide(net_out);
}

int main() {
    int i = 0;
    float apr;
    pesos_initNt();

    printf("============================================================\n");
    printf(" Entrenando Perceptron Multicapa (MLP) para compuerta XOR   \n");
    printf(" Arquitectura: 2 entradas -> 2 ocultas -> 1 salida          \n");
    printf(" Epocas: %d | Tasa de aprendizaje (K): %.2f                \n", epoca, K);
    printf("============================================================\n");

    while (i < epoca) {
        float err_acum = 0.0f;

        apr = EntNt(1, 1, 0);
        err_acum += (0 - apr) * (0 - apr);

        apr = EntNt(1, 0, 1);
        err_acum += (1 - apr) * (1 - apr);

        apr = EntNt(0, 1, 1);
        err_acum += (1 - apr) * (1 - apr);

        apr = EntNt(0, 0, 0);
        err_acum += (0 - apr) * (0 - apr);

        // Imprimir progreso periódicamente para mantener la consola ágil
        if (i % 10000 == 0 || i == epoca - 1) {
            printf("------------------------------------------------------------\n");
            printf("Epoca %d | Error cuadratico medio: %f\n", i, err_acum / 4.0f);
            printf("  1 XOR 1 = %f (Esperado: 0)\n", InitNt(1, 1));
            printf("  1 XOR 0 = %f (Esperado: 1)\n", InitNt(1, 0));
            printf("  0 XOR 1 = %f (Esperado: 1)\n", InitNt(0, 1));
            printf("  0 XOR 0 = %f (Esperado: 0)\n", InitNt(0, 0));
        }
        i++;
    }

    printf("\n============================================================\n");
    printf("              RESULTADOS FINALES DE LA COMPUERTA XOR         \n");
    printf("============================================================\n");
    printf("Entrada (1, 1) -> Salida: %.4f => Clasificacion: %d (Esperado: 0)\n", 
           InitNt(1, 1), InitNt(1, 1) >= 0.5f ? 1 : 0);
    printf("Entrada (1, 0) -> Salida: %.4f => Clasificacion: %d (Esperado: 1)\n", 
           InitNt(1, 0), InitNt(1, 0) >= 0.5f ? 1 : 0);
    printf("Entrada (0, 1) -> Salida: %.4f => Clasificacion: %d (Esperado: 1)\n", 
           InitNt(0, 1), InitNt(0, 1) >= 0.5f ? 1 : 0);
    printf("Entrada (0, 0) -> Salida: %.4f => Clasificacion: %d (Esperado: 0)\n", 
           InitNt(0, 0), InitNt(0, 0) >= 0.5f ? 1 : 0);
    printf("============================================================\n");

    return 0;
}
