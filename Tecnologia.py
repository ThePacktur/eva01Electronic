
class Tecnologia:
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def set_voltaje(self,voltaje:int):
        self.__voltaje = voltaje

    def get_voltaje(self):
        return self.__voltaje

    def set_precio(self,precio:float):
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
    def set_eficiencia(self,eficiencia:str):
        self.__eficiencia = eficiencia

    def get_eficiencia(self):
        return self.__eficiencia
    
    def set_marca(self,marca:str):
        self.__marca = marca

    def get_marca(self):
        return self.__marca
    
    #tecnologias(marca:str,voltaje:int,precio:float,eficiencia:str)
    def imprimirCaracteristicas():
        pass

    #crear una calculadora de descuento.
    def calculadoraDescuento():
        pass
    
    def __str__(self):
        imp = f"Voltaje: {self.voltaje}"
        imp += f"Precio: {self.precio}"
        imp += f"Eficiencia: {self.eficiencia}"
        imp += f"Marca: {self.Marca}"
        return imp