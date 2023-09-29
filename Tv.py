from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str,tamanio:float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio = tamanio

    def set_tamanio(self,tamanio:float):
        self.__tamanio = tamanio

    def get_tamanio(self):
        return self.__tamanio
    

    #sobreescribir 'update' calculadora de descento public
    def calculadoraDescuento(self):
        descuento_eficiencia =  super().calculadoraDescuento()
        descuento_total = descuento_eficiencia * 0.95 
        return descuento_total
    #sobreescribir 'update' imprimirCaratecristicas() public
    #def imprimirCaracteristicas(self):
    #    super().imprimirCaracteristicas()
    #    print("Tamanio: ",self.tamanio)

    def __str__(self):
        imp = super().__str__()
        imp += f"\nTamanio: {self.__tamanio}"
        return imp

