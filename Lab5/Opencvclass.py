from abstractclass import Imagen
import cv2 as cv

class OpenCv(Imagen):

    def __init__(self, path):
        super().__init__(path)
    
    def mostrar_imagen(self):
        """Funcion para mostrar la imagen"""
        try:
            path = self.path_exist()
            image=cv.imread(path)
            #abrir la imagen y crear una ventana temporal
            if image is None:
                raise ValueError("No se pudo cargar la imagen.")
            
            window= "temp_window"
            cv.imshow(window,image)
            #Supuestamente es necesario para que no explote
            cv.waitKey(0)
            
        except Exception as e:
            print(f'"Error {e}"')

        finally:
            #Limpiar aunque se produzca una excepciòn.
            cv.destroyAllWindows()
