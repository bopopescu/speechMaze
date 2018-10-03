# Lecciones Aprendidas

**Samantha Arburola**

Proyecto No.1 - Inteligencia Artificial

Laberinto con Agente Inteligente y Reconocimiento de Voz





El reconocimiento de voz es una de las formas de comunicación con las máquinas que se está sobreponiendo con más fuerza a otras formas de interacción más tradicionales, sobre todo los botones físicos, aunque también está desplazando a la funcionalidad táctil en algunos casos.



Hoy día se está acompañando a estos comandos de una capa de lenguaje natural.  Lo que lleva a entrenan a un agente para reconocer patrones, acentos, dialectos e incluso idiomas.

No es tan sencillo como indicar al sistema que reconozca castellano, francés o mandarín, es preciso entender la lengua sino los distintos acentos con que se habla e incluso entender las formas de expresarse, que pueden ser diferentes en cada hablante.



La manipulación de las ondas de voz, discrepando ruidos del audio grabado es otro de los retos del reconocimiento de voz.



Para este proyecto se utilizó el Google Speech Recognition API para la librería Speech Recognition de Python, la ventaja de utilizar ambas es el acceso a la gran base de datos de Google, la cual es actualizada practicamente cada hora cuando los usuarios dan comandos de voz a las aplicaciones de Google, lo cual colabora disminuyendo en el tiempo de entrenamiento del agente de voz de este proyecto.



Este tiene 2 fuentes de conocimiento:

* **Aprendizaje deductivo**: se basa en la transferencia de los conocimientos que un experto humano posee a un sistema informático.

- **Aprendizaje inductivo**:  se basa en que el sistema pueda, automáticamente, conseguir los conocimientos necesarios a partir de ejemplos reales sobre la tarea que se desea modelizar, basandose en pruebas de Markov y redes neuronales.



Esto implica la decodificación acústico-fonético con  fuentes de información acústica, fonética, fonológica y léxica, con lo procedimientos interpretativos. La entrada al decodificador es la señal vocal convenientemente representada; para ello es necesario que ésta se someta a un preproceso de parametrización.