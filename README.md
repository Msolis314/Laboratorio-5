# Laboratorio #5
## Diagrama de diseño
![diagrama](https://raw.githubusercontent.com/mareyes1/Lab2/main/diagrama_lab5_v2.png)
## Dependencias
Se utilizan las siguientes bibliotecas:

* El módulo `os` de la biblioteca estándar: Proporciona una interfaz para interactuar con el sistema operativo, permitiendo realizar operaciones relacionadas con éste, como la manipulación de archivos y directorios.
* De la biblioteca `Pillow` (`PIL`) se utiliza el módulo `Image`: Proporciona métodos para abrir (`open()`) y mostrar (`show()`) una imagen.
* La biblioteca `OpenCV` (`cv2`): Proporciona métodos alternativos para leer (`imread()`) y mostrar (`imshow()`) una imagen.

Estas se importan en el archivo `abstractclass.py`. A su vez, el archivo `args.py` importa los módulos `Pil` y `OpenCv` de `abstractclass`.

Las excepciones se manejan por medio de `FileNotFoundError` para el caso de que el path proporcionado no exista. Además, se manejan por medio de la clase `PersonalisedExcep` en caso de que la biblioteca especificada no sea una opción válida (PIL u OpenCV). También, se incluye una excepción para imprimir un mensaje de error si se presenta un fallo en procesamiento de la imagen.
## Uso del programa
Se requiere de los archivos `abstractclass.py` y `args.py` para el funcionamiento.

El programa se ejecuta de la siguiente forma:

`>> python3 args.py --image <path_a_la_imagen> --biblioteca <PIL | OpenCV>`
