from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Transporte):
    def __init__(self, costeDespacho_base: int,aro:float,velocidad:float,peso:float):
        super().__init__(costeDespacho_base)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

       
    def set_aro(self,aro:float):
        self.__aro = aro

    def get_aro(self):
        return self.__aro
    


    def set_velocidad(self,velocidad:float):
        self.__velocidad =velocidad

    def get_velocidad(self):
        return self.__velocidad
    
    
    
    def set_peso(self,peso:float):
        self.__peso = peso

    def get_peso(self):
        return self.__peso
    
    def cotizar(self):
        valor_por_kg = 300
        costo_despacho = 4000 + (self.peso * valor_por_kg)
        descuento = self.calcular_descuento()
        precio_descuento = self.precio * (1 - descuento)
        precio_total = precio_descuento + costo_despacho
        return precio_total

    #def __str__(self):
     #   imp = super().__str__()
     #   imp += super().__str__()
     #   imp += f"\nAro: {self.__aro}"
     #   imp += f"\nVelocidad: {self.__velocidad}"
     #   imp += f"\nPeso: {self.__peso}"