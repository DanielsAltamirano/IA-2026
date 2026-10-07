# Actividad: Árboles de decisión

> **Alumno:** Altamirano Ramirez Daniels John
> **Maestro:** Alcaraz Chavez Jesus Eduardo
> **Materia:** Inteligencia Artificial
> **Carrera:** Ingeniería en sistemas computacionales
> **Lugar y Fecha:** Morelia, Michoacán (Octubre 2026)

---

## Parte I. Conceptos y definiciones

### Pregunta 1
**¿Qué es un árbol de decisión y cuál es su objetivo principal dentro de un problema de clasificación?**

Un árbol de decisión es un modelo de aprendizaje supervisado que utiliza una estructura jerárquica, similar a un diagrama de flujo, para tomar decisiones basadas en una serie de reglas extraídas de los datos. 

Su objetivo principal en un problema de clasificación es dividir iterativamente un conjunto de datos en categorías discretas o clases. Lo logra realizando preguntas secuenciales sobre las características de un dato particular hasta que este es asignado a una etiqueta final, logrando la mayor homogeneidad o pureza posible en cada grupo resultante.

### Pregunta 2
**Elementos de un árbol de decisión:**

*   **Nodo raíz:** 
    *   Es el punto de partida del modelo y contiene todo el conjunto de datos inicial antes de cualquier división. Representa la característica más importante o el primer filtro que mejor separa la información disponible.
*   **Nodo interno:** 
    *   Son los puntos intermedios donde el conjunto de datos se vuelve a dividir. Cada nodo interno representa una prueba o condición lógica sobre una característica específica.
*   **Rama:** 
    *   Es la conexión que une a los nodos. Representa el resultado directo de la prueba realizada en un nodo anterior y dirige el flujo de la decisión hacia el siguiente nivel del árbol.
*   **Hoja (o nodo terminal):** 
    *   Son los extremos del árbol donde el proceso se detiene y ya no hay más divisiones. Representan la decisión final, es decir, la clase o categoría que el modelo le asigna al dato evaluado.

### Pregunta 3
**¿Qué es una red neuronal multicapa y la función de sus capas?**

Una red neuronal multicapa (o perceptrón multicapa) es un modelo computacional inspirado en las redes neuronales biológicas, compuesto por múltiples capas de neuronas artificiales densamente interconectadas. Su principal fortaleza es la capacidad de modelar y aprender relaciones complejas y no lineales dentro de los datos.

*   **Capa de entrada:** 
    *   Es la puerta de acceso al modelo. Recibe los datos crudos (las variables o características del problema) y los transfiere a la siguiente capa. No realiza cálculos ni transformaciones.
*   **Capa oculta:** 
    *   Son las capas intermedias donde ocurre el procesamiento pesado. Aquí, las neuronas aplican transformaciones matemáticas y funciones de activación para extraer características, identificar patrones abstractos y descubrir relaciones no lineales en los datos.
*   **Capa de salida:** 
    *   Es la última etapa de la red. Toma la información procesada por las capas ocultas y emite la predicción final, que en un problema de clasificación suele ser una etiqueta específica o una probabilidad para cada clase posible.

### Pregunta 4
**Pesos, sesgos y su cambio durante el entrenamiento:**

*   **Pesos:** 
    *   Representan la fuerza o importancia de la conexión entre dos neuronas. Determinan cuánta influencia tiene la señal de salida de una neurona sobre la activación de la neurona receptora en la siguiente capa.
*   **Sesgos:** 
    *   Son valores constantes adicionales que actúan de manera similar a la intersección en una ecuación lineal. Permiten desplazar la función de activación hacia la izquierda o la derecha, brindando flexibilidad al modelo para ajustarse a los datos incluso cuando todas las entradas a la neurona son cero.

**¿Por qué cambian sus valores?** 
Inicialmente, los pesos y sesgos se asignan de forma aleatoria. Durante el entrenamiento generalmente usando un algoritmo de propagación hacia atrás o *backpropagation*, la red emite una predicción y calcula la diferencia matemática entre esta y el resultado real esperado. Para reducir ese error, el modelo utiliza técnicas de cálculo diferencial para actualizar de manera iterativa los valores de los pesos y sesgos. Este ajuste continuo de parámetros matemáticos es precisamente lo que constituye el aprendizaje de la red.

### Pregunta 5
**Diferencia principal en la forma de aprender de ambos modelos:**

La principal diferencia radica en su enfoque matemático y estructural: un árbol de decisión aprende construyendo particiones lógicas y secuenciales, mientras que una red neuronal multicapa aprende optimizando parámetros matemáticos continuos en una arquitectura de grafos.

*   **Qué aprende el árbol de decisión:** 
    *   Aprende la topología de las reglas lógicas. Identifica qué variables son las más informativas, en qué orden deben evaluarse y cuáles son los umbrales de corte exactos para separar los datos. El resultado final es un conjunto discreto de reglas 'If-Then' altamente interpretables.
*   **Qué aprende la red neuronal multicapa:** 
    *   Aprende los valores óptimos de los pesos y sesgos en cada conexión de la red. No genera reglas lógicas legibles para un humano, sino que ajusta matrices de números mediante la minimización iterativa de una función de error. Este proceso le permite aproximarse a cualquier función matemática compleja que relacione las entradas con las salidas.

---

## Parte II. Análisis y aplicación

### Pregunta 6: Detección de fraudes bancarios
A lo que entiendo de lo que hemos visto en clase, el árbol de decisión tiene la ventaja de ser rápido y muy fácil de interpretar. La desventaja es que si los patrones de los estafadores son muy complejos, el árbol se puede quedar corto. Por otro lado, la red neuronal multicapa es mucho mejor para encontrar esos patrones ocultos y relaciones complejas entre todas las variables, logrando mayor precisión. Su gran desventaja es que funciona como una 'caja negra': no te explica por qué bloqueó la transacción.

> **¿Cuál usaría?** 
> Yo me iría por la red neuronal. Siento que en fraudes, los estafadores son cada vez más ingeniosos, así que prefiero un sistema con la mayor precisión posible para evitar pérdidas, aunque me cueste un poco más explicarle al cliente el motivo preventivo del bloqueo.

### Pregunta 7: Detección de estudiantes en riesgo de reprobar
Si ambos modelos tienen prácticamente la misma precisión, elegiría 100% el árbol de decisión porque la interpretación de los datos es lo más importante. 

> Como estudiante, si un sistema me avisa que voy a reprobar, quiero saber en qué estoy fallando o qué me está haciendo falta. Con la red neuronal solo obtendría una alerta para avisarme que estoy en riesgo de reprobar y ya. En cambio, con el árbol podría verificar cuáles variables son las que me están llevando por ese camino y cambiar de rumbo en todo caso y evitar llegar a la reprobación.

### Pregunta 8: Sistema de atención prioritaria en hospital
A primera vista pareciera que la red neuronal es la indicada para este tipo de situaciones, sin embargo al haber vidas en riesgo participando en este caso, personalmente, no considero que la mayor precisión sea suficiente para confiar ciegamente en la red neuronal.

> Ya que si usamos la red neuronal la cual es mucho más difícil de interpretar y comete un error, mandando a la sala de espera a alguien que en realidad estaba insertándose por un falso negativo, el doctor no tendría cómo revisar qué falló en el análisis. Esto podría tener consecuencias graves en muchos aspectos, principalmente en la vida del paciente y posteriormente en temas legales para el hospital. En la medicina, el médico necesita poder entender y auditar el razonamiento de la máquina para validarlo con su propia experiencia profesional.

### Pregunta 9: Predicción de retrasos en pedidos
Para saber a qué modelo hacerle caso en ese caso en particular, no podemos fijarnos solo en una predicción suelta. 

> Se deben revisar las métricas de evaluación que nos dieron durante las pruebas del modelo como el dataset de pruebas. También se debe revisar la matriz de confusión, exactitud y el *recall*. Además, revisaría el porcentaje de seguridad de la red neuronal para saber qué tan segura está del resultado que está mostrando. También hay que cerciorarse de que ninguno de los modelos esté sufriendo de sobreajuste, porque si el árbol solo se memorizó los datos viejos, no nos va a servir para predecir pedidos nuevos con precisión.

### Pregunta 10: Sistema de aprobación de créditos
Si la ley o las políticas exigen darle explicaciones a los clientes para evitar demandas por discriminación, me quedaría con el árbol de decisión por ser transparente, aunque el banco pierda algo de predicción.

> Sin embargo, si se pueden usar ambos modelos, el sistema híbrido sería claramente la mejor opción. Usaría la red neuronal como el filtro principal para predecir si se otorga el crédito aprovechando su precisión. Pero, si la red lo rechaza, pasaría esos datos por el árbol de decisión para poder extraer la razón principal del rechazo y así darle una explicación clara y justificada al cliente.

### Explicación final: No hay un algoritmo que sea el mejor para todo
Con todo esto me queda claro que en temas de IA no hay una solución mágica para todo. Si nuestro problema tiene una alta complejidad y contamos con una cantidad de datos muy grande, buscamos maximizar la precisión usando modelos robustos como las Redes Neuronales, aceptando que sacrificamos interpretabilidad.

> Pero, cuando las consecuencias de una decisión incorrecta son muy críticas, lo que más nos importa es la interpretabilidad. Necesitamos auditar y entender por qué la IA decidió eso, y ahí es donde modelos más transparentes como el Árbol de Decisión ganan, incluso si perdemos un poco de precisión.