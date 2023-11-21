import os
from PIL import Image
import cv2 as cv

class Imagen:
    
    def __init__(self, path):
        self.path_imagen=path
    
    def mostrar_imagen(self):
        pass
    
    def path_exist(self):
        try: 
            path_true = os.path.normpath(self.path_imagen)
            if os.path.exists(path_true):
                return path_true
            else:
                raise FileNotFoundError(f'El archivo "{path_true}" no existe.')
        except FileNotFoundError as e:
            print(f'Error:{e}')

class Pil(Imagen):
    
    def __init__(self, path_imagen):
        super().__init__(path_imagen)
    
    def mostrar_imagen(self):
        path= self.path_exist()
        try:
            ima = Image.open(path)
            ima.show()
        except Exception as e:
            print(f'Error:{e}')

class OpenCv(Imagen):
    
    def __init__(self, path_imagen):
        super().__init__(path_imagen)
    
    def mostrar_imagen(self):
        """Funcion para mostrar la imagen"""
        path = self.path_exist()

        try:
            image=cv.imread(path)
            if image is None:
                raise Exception(f'Error al leer la imagen de "{path}".')
            #abrir la imagen y crear una ventana temporal
            window= "temp_window"
            cv.imshow(window,image)
            #Supuestamente es necesario para que no explote
            cv.waitKey(0)
            #Limpiar
            cv.destroyAllWindows()
        except Exception as e:
            print(f'Error:{e}')

        
