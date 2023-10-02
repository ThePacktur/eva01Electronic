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
    
    def calculadora_precio_total(self):
        descuento_eficiencia = super().calculadoraDescuento()
        decuento_version = 0.005 if self.__version == 'Lite' else 0
        precio_total = self.__precio - descuento_eficiencia - (self.__precio * decuento_version)
        return precio_total
    

    #def imprimirCaracteristicas(self):
     #   super().imprimirCaracteristicas()
     #   print("Nombre de la Consola: ",self.__nombreConsola)
     #   print("Version: ", self.__version)
    def __str__(self):
        descuento_eficiencia = super().calculadoraDescuento() * 100
        descuento_version = 5 if self.__version == 'Lite' else 0
        precio_total = self.calculadora_precio_total
        imp =  f"\n tipo de consola: {super().__str__()}"
        imp += f"\nNombre consola: {self.__nombreConsola}"
        imp += f"\nVersion: {self.__version}"
        imp += f"\nDescuento aplicado: {descuento_eficiencia + descuento_version}"
        imp += f"\nValor total despues del descuento: {precio_total}"
        return imp
    