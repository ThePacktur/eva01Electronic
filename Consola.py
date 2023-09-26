from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str,nombreConsola:str,version:str):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def set_nombreConsola(self,nombreConsola:str):
        self.__nombreConsola = nombreConsola

    def get_nombreConsola(self):
        return self.__nombreConsola
    
    def set_version(self,version):
        self.__version = version

    def get_version(self):
        return self.__version
    