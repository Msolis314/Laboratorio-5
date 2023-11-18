import argparse

from abstractclass import Pil
from abstractclass import OpenCv
class PersonalisedExcep(Exception):
    def __init__(self, mensaje):
        self.mensaje=mensaje
        super().__init__(self.mensaje)
def parse_arguments():
    """Funcion para pasar argumentos posicionales desde la linea de comandos
    No resibe parametros
    devuelve los argumentos
    """
    parser=argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL","OpenCV"])
    parser.add_argument( "--imagen", required=True, help="Path a la imagen")
    return parser.parse_args()

def main():
    #Interfaz del programa
    args = parse_arguments()
    print(args.imagen)
    if args.biblioteca == 'PIL':
        ima_ob = Pil(args.imagen)
    elif args.biblioteca == "OpenCV":
        ima_ob = OpenCv(args.imagen)
    else: 
        raise PersonalisedExcep("Biblioteca no valida")
    
    try:
        ima_ob.mostrar_imagen()
    except Exception as e:
        print(f'Error en el procesamiento de la imagen: {e}')



if __name__ == "__main__":
    main()