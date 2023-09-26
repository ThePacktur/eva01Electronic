from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str,tamanio:float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio = tamanio

    def set_tamanio(self,tamanio:float):
        self.__tamanio = tamanio

    def get_tamanio(self):
        return self.__tamanio
    
