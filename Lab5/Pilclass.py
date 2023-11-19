from abstractclass import Imagen
from PIL import Image

class Pil(Imagen):

    def __init__(self, path):
        super().__init__(path)
    
    def mostrar_imagen(self):
        try:
            path= self.path_exist()
            ima = Image.open(path)
            ima.show()
        except FileNotFoundError:
            print(f'El archivo no se encuentra en la ruta proporcionada: {self.path}')
        except Exception as e:
            print(f'Error inesperado: {e}')

        
