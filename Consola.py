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
    
    def calculadoraDescuento(self):
        descuento_eficiencia = super().calculadoraDescuento()
        descuento_total = descuento_eficiencia
        if self.version == "Lite":
            descuento_total += super().get_precio() * 0.05
        return descuento_total

    def imprimirCaracteristicas(self):
        super().imprimirCaracteristicas()
        print("Nombre de la Consola: ",self.nombreConsola)
        print("Version: ", self.version)
    def __str__(self):
        imp = super().__str__()
        imp += f"Nombre consola: {self.nombreConsola}"
        imp += f"Version: {self.version}"
        return imp
    