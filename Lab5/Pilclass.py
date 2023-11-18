from abstractclass import Imagen
from PIL import Image
class Pil(Imagen):
    def __init__(self, path):
        super().__init__(path)
    def mostrar_imagen(self):
        path= self.path_exist()
        ima = Image.open(path)
        ima.show()
        