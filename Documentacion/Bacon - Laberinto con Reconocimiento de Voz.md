

# Bacon - Laberinto con Reconocimiento de Voz



## Comandos



El programa incia por definición con 8 columnas y 8 filas, las cuales pueden ser actualizadas por separado con los comandos:



```
COLUMNAS 7
```



```
FILAS 6
```



Los bloques son de tamaño automático, ya que se ajusta al tamaño de la ventana.



**Empezar**

Usando este comando el agente inteligente espera las posiciones donde inciará en el laberinto. Por tanto debe pronunciar las palabras en el siguiente orden:



```
EMPEZAR COLUMNA 1 FILA 10
```



**Final**

Usando este comando el agente inteligente espera las posición donde finalizará en el laberinto. Por tanto debe pronunciar las palabras en el siguiente orden:



```
FIN COLUMNA 4 FILA 4
```



De esta manera, el programa inicia el plano de trabajo con obstaculos creados aleatoriamente, garantizando que existe al menos 1 solución para que el agente llegue a su destino. 

![](/Users/vainilla/Documents/speechMaze/Documentacion/images/ejemplo1.jpg)



**Diagonales No**

Comando para deshabilitar el uso de diagonales en la solución del laberinto.



**Diagonales Si**

Comando para habilitar el uso de diagonales en la solución del laberinto.



**Correr**

Muestra la solución para que el agente llegue a su destino.

![](/Users/vainilla/Documents/speechMaze/Documentacion/images/ejemplo2.png)

**Limpiar**

Limpia la cuadrícula.

Se pueden actualizar las dimensiones con los comandos ``columnas``y ``filas``. Además es el momento indicado para habilitar o deshabilitar el permiso para utilizar diagonales.





