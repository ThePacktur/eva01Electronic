from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, marca: str, voltaje: int, eficiencia: str, precio: float,nombreConsola:str,version:str):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def set_nombreConsola(self,nombreConsola:str):
        self.__nombreConsola = nombreConsola

    def get_nombreConsola(self):
        return self.__nombreConsola
    
    def set_version(self,version:str):
        self.__version = version

    def get_version(self):
        return self.__version
    
    def calculadoraDescuento(self):
        descuento_eficiencia = super().calculadoraDescuento()
        descuento_total = descuento_eficiencia
        if self.version == "Lite":
            descuento_total += super().get_precio() * 0.05
        return descuento_total

    def cotizar(self):
     return  super().get_precio
    #def imprimirCaracteristicas(self):
     #   super().imprimirCaracteristicas()
     #   print("Nombre de la Consola: ",self.__nombreConsola)
     #   print("Version: ", self.__version)
    def __str__(self):
        imp = super().__str__()
        imp += f"\nNombre consola: {self.__nombreConsola}"
        imp += f"\nVersion: {self.__version}"
        return imp
    