import argparse
from abstractclass import Pil
from abstractclass import OpenCv

class PersonalisedExcep(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def parse_arguments():
    """Función para pasar argumentos posicionales desde la línea de comandos
    No recibe parámetros
    Devuelve los argumentos
    """
    parser = argparse.ArgumentParser(description="Procesamiento de Imágenes")
    parser.add_argument("--biblioteca", choices=["PIL", "OpenCV"], required=True,
    help="Especifica la biblioteca a utilizar (PIL o OpenCV)")
    parser.add_argument("--imagen", required=True, help="Ruta a la imagen a procesar")
    return parser.parse_args()

def main():
    try:
        # Interfaz del programa
        args = parse_arguments()

        if args.biblioteca == 'PIL':
            ima_ob = Pil(args.imagen)
        elif args.biblioteca == "OpenCV":
            ima_ob = OpenCv(args.imagen)
        else:
            raise PersonalisedExcep("Biblioteca no válida: Debe ser 'PIL' o 'OpenCV'")

        ima_ob.mostrar_imagen()

    except PersonalisedExcep as pe:
        print(f'Error: {pe}')

    except FileNotFoundError as fnfe:
        print(f'Error: El archivo no ha sido encontrado - {fnfe}')

    except Exception as e:
        print(f'Error en el procesamiento de la imagen: {e}')

if __name__ == "__main__":
    main()

