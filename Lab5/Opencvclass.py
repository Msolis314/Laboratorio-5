from abstractclass import Imagen
import cv2 as cv
class OpenCv(Imagen):
    def __init__(self, path):
        super().__init__(path)
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