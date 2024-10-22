# Clicker

Juego simple pero desafiante, que pueda ayudar a muchas personas a mejorar sus habilidades de percepción y memoria visual, 
ya que hacer clic es lo que esperamos del jugador.

El tablero del Clicker consta de botones y cada uno de los botones contiene un número aleatorio diferente del rango 1..999.

Hay un temporizador que inicialmente muestra 0 y se inicia cuando el usuario hace clic en el tablero por primera 
vez. Esperamos que el jugador haga clic en todos los botones en el orden impuesto por los números, desde el más 
bajo hasta el más alto.

Para este proyecto se tomó como idea uno de los Laboratorios de Práctica del curso GUI Programming in Python, emitido
por el Python Institute, se amplió y mejoró con la idea de practicar elemnetos avanzados en Python.


## Tabla de Contenidos

- Instalación
- Uso
- Contribuir
- Licencia

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/rmelim/Clicker
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd Clicker
    ```
3. Sólo si va a modificar código para contribuir con el mismo:

    3.1. Crea un entorno virtual:
    ```bash
    python -m venv nombre_entorno
    ```
    3.2. Activa el entorno virtual:
    - En Windows:
        ```bash
        nombre_entorno\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source nombre_entorno/bin/activate
        ```
## Uso

Se debe instanciar el objeto Clicker presente en el módulo clicker. 

Por ejemplo:

```python
from clicker import Clicker

game = Clicker(size=5)
game.start()
```

## Contribuir
Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del proyecto.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Envía tus cambios (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Mira el archivo LICENSE para más detalles.
