from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Transporte):
    def __init__(self, costeDespacho_base: 400,aro:float,velocidad:float,peso:float):
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
    
    def calcular_precio_total(self):
        descuento_eficiencia = self.__precio * self.__costeDespacho_base
        costo_total_despacho = self.__costeDespacho_baseo + self.__peso
        precio_total = self.__precio - descuento_eficiencia + costo_total_despacho
        return precio_total

    def __str__(self):
        descuento_eficiencia = self.calcular_precio_total() * 100
        costo_total_despacho = self.__costo_despacho + self.__peso
        precio_total = self.calcular_precio_total
        imp =  f"\nTipo de Scooter: ,{super().__str__()}"
        imp += f"\nAro: ,{self.__aro}"
        imp += f"\nVelocidad: ,{self.__velocidad}"
        imp += f"\nPeso: ,{self.__peso}"
        imp += f"\nDescuento eficiencia: {descuento_eficiencia}"
        imp += f"\nCosto total de despacho: {costo_total_despacho} "
        imp += f"\nPrecio total: {precio_total}"
        return imp