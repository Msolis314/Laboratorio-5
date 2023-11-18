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
            open(path_true)
            return path_true
        except FileNotFoundError as e:
            print(f'Error:{e}')

class Pil(Imagen):
    def __init__(self, path_imagen):
        super().__init__(path_imagen)
    def mostrar_imagen(self):
        path= self.path_exist()
        ima = Image.open(path)
        ima.show()
class OpenCv(Imagen):
    def __init__(self, path_imagen):
        super().__init__(path_imagen)
    def mostrar_imagen(self):
        """Funcion para mostrar la imagen"""
        path = self.path_exist()
        image=cv.imread(path)
        #abrir la imagen y crear una ventana temporal
        window= "temp_window"
        cv.imshow(window,image)
        #Supuestamente es necesario para que no explote
        cv.waitKey(0)
        #Limpiar

        cv.destroyAllWindows()

        