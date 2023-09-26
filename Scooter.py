from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia,Transporte):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, aro:float,velocidad:int,peso:float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    def set_aro(self,aro:float):
        self.__aro = aro

    def get_aro(self):
        return self.__aro
    


    def set_velocidad(self,velocidad:float):
        self.__velocidad =velocidad

    def get_vevelocidad(self):
        return self.__velocidad
    
    
    
    def set_peso(self,peso:float):
        self.__peso = peso

    def get_peso(self):
        return self.__peso
    