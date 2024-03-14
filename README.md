# Talana Kombat
Prueba para postular al cargo de Software Developer Engineer en Talana. Espero les guste :)

# Instalación

1. Instalar [Python](https://www.python.org/downloads/)
2. Ubicarse en la raiz del proyecto
3. Ejecutar `py main.py 'cadena_de_diccionario' o nombre de archivo,json`

# Detalles de la solución

En base a los requisitos del problema planteado, se decidió optar por una aplicación de línea de comandos utilizando únicamente Python. Esto se debe a que el requisito principal es construir una solución que narre la pelea e informe el resultado final. Esta solución, dada su estructura, puede ser fácilmente adaptada en una próxima versión para ser desplegada en una API. Esto permitiría que fuera consultada por un cliente que proporcionara una GUI con la información necesaria.

La solución ejecuta una simulación de combate entre dos jugadores utilizando la información proporcionada como argumento de la línea de comandos. Los datos del combate se extraen de un diccionario JSON, se realizan algunas acciones de preparación y luego se ejecuta el combate. Si ocurre algún error durante el proceso, se imprime un mensaje de error.

Este código define una función principal `main()` que lleva a cabo una simulación de combate entre dos jugadores en un juego. Aquí hay una explicación detallada del código:

1. Se inicializa un diccionario vacío `fight_json` que contendrá la información del combate.

2. Dentro de un bloque `try`, el programa intenta realizar las siguientes acciones:

* Verifica si se proporcionó un único argumento en la línea de comandos.
* Si no se proporciona un solo argumento, imprime un mensaje de uso y sale del programa con un código de error.
* Llama a la función `get_and_validate_input()` para validar y obtener la cadena JSON proporcionada como argumento de la línea de comandos. El resultado se almacena en `fight_json`.
* Se extraen los datos de los jugadores (`player1` y `player2`) del diccionario `fight_json`.
* Se establecen los nombres de los jugadores como 'Tony' y 'Arnaldor', respectivamente.
* Calcula el número de rondas del combate, tomando el máximo de la longitud de los movimientos de cada jugador.
* Determina qué jugador empieza el combate utilizando la función `who_starts()`.
* Inicializa la energía de cada jugador en 6 unidades.
* Llama a la función `execute_rounds()` para ejecutar el combate con los jugadores y el número de rondas calculado.

3. Dentro del bloque `except`, cualquier excepción que se produzca durante la ejecución del código se captura y se imprime. Esto ayuda a manejar cualquier error que pueda ocurrir durante la simulación del combate.

# Inputs

Los inputs de la solución son recibidos como parametros de línea de comandos, estos pueden ser una cadena de diccionario o el nombre de un archivo `.json`.

Ejemplo de cadena de diccionario:
```
'{\"player1\":{\"movimientos\":[\"D\",\"DSD\",\"S\",\"DSD\",\"SD\"],\"golpes\":[\"K\",\"P\",\"\",\"K\",\"P\"]},\"player2\":{\"movimientos\":[\"SA\",\"SA\",\"SA\",\"ASA\",\"SA\"],\"golpes\":[\"K\",\"\",\"K\",\"P\",\"P\"]}}'
```

Ejemplo de contenido de archivo `.json` (se encuentra tambien en el archivo `data.json`):
```
{
  "player1": {
      "movimientos": ["D", "DSD", "S", "DSD", "SD"],
      "golpes": ["K", "P", "", "K", "P"]
  },
  "player2": {
      "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
      "golpes": ["K", "", "K", "P", "P"]
  }
}
```

Que tengan un buen dia!😊