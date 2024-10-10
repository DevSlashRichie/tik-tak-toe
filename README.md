# Tik-Tak-Toe

### Contexto

El juego "Tic-Tac-Toe" es una versión digital del clásico juego de lápiz y papel que enfrenta a dos jugadores.
El objetivo del juego es que uno de los jugadores logre alinear tres de sus símbolos (X o O) en una fila, columna o diagonal dentro de una cuadrícula de 3x3.

En esta versión digital, desarrollada en Python 3 y ejecutada en terminal, los jugadores alternan turnos para colocar su símbolo en una de las nueve posiciones disponibles.
El programa verifica automáticamente si un jugador ha ganado o si es un empate esto cuando todas las casillas están ocupadas y no hay un ganador.

Además de las funcionalidades básicas, esta implementación permite almacenar el historial de partidas en un archivo de texto, lo que facilita a los jugadores revisar los resultados anteriores.

### Instrucciones

Clona el repositorio en tu máquina local:

```bash
git clone git@github.com:DevSlashRichie/tik-tak-toe.git
```

Necesitarás instalar la dependecia "matplotlib" para poder utilizar el programa.

Se recomienda utilizar [poetry](https://python-poetry.org/docs/) para instalar las dependencias.

Para instalar las dependencias con poetry, ejecutar en terminal:

```bash
poetry install
```

Para correr el programa, ejecutar en terminal:

```bash
poetry run python tiktaktoe.py
```

Si no utilizas poetry, puedes instalar la dependencia con pip:

```bash
pip install matplotlib
```

Para correr el programa, ejecutar en terminal:

```bash
python tiktaktoe.py
```

El primer jugador deberá introducir su nombre y elegir entre las opciones 'X' o 'O'.
El segundo jugador deberá introducir su nombre y se le asignará el símbolo restante.

Los jugadores deberán ingresar un número del 1 al 9 para seleccionar la posición en la que desean colocar su símbolo.
Al finalizar la partida, se mostrará el resultado y se preguntará si desean jugar otra vez.

### Algortimo

| **Etapa**   | **Descripción**                                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entrada** | - Jugador 1: Introduce su nombre                                                                                                                                               |
|             | - Jugador 2: Introduce su nombre.                                                                                                                                              |
| **Proceso** | **1. Inicialización:**                                                                                                                                                         |
|             | - Crear un tablero vacío representado por una matriz 3x3.                                                                                                                      |
|             |                                                                                                                                                                                |
|             | **2. Bucle de Juego:**                                                                                                                                                         |
|             | - Repetir hasta que haya un ganador o un empate:                                                                                                                               |
|             | 1. Mostrar el tablero: Imprimir el tablero actual en pantalla.                                                                                                                 |
|             | 2. Entrada del Jugador:                                                                                                                                                        |
|             | - Solicitar al jugador actual (X o O) que ingrese una posición (fila y columna) para colocar su símbolo. Se elegirá al azar si O o X comienza en caso de la primera iteración. |
|             | - Validar la entrada:                                                                                                                                                          |
|             | - Verificar que la posición esté dentro de los límites de la matriz.                                                                                                           |
|             | - Verificar que la posición esté vacía.                                                                                                                                        |
|             | - Si la entrada es inválida, solicitar una posición válida.                                                                                                                    |
|             | 3. Actualizar Tablero:                                                                                                                                                         |
|             | - Colocar el símbolo del jugador actual (X o O) en la posición seleccionada.                                                                                                   |
|             | 4. Verificación de Ganador:                                                                                                                                                    |
|             | - Revisar filas, columnas y diagonales para verificar una alineación ganadora.                                                                                                 |
|             | - Si hay un ganador, declarar al jugador y terminar el juego.                                                                                                                  |
|             | - Guardar resultado en archivo de texto.                                                                                                                                       |
|             | 5. Verificación de Empate:                                                                                                                                                     |
|             | - Si todas las casillas están llenas y no hay ganador, declarar un empate.                                                                                                     |
|             | 6. Cambiar de Turno:                                                                                                                                                           |
|             | - Alternar entre Jugador 1 (X) y Jugador 2 (O).                                                                                                                                |
| **Salida**  | - Tablero final: Visualización del tablero al final del juego.                                                                                                                 |
|             | - Resultado del juego: Declaración del ganador o indicación de empate.                                                                                                         |
