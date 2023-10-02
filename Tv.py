from Tecnologia import Tecnologia


class Tv(Tecnologia):
    def __init__(self, marca: str, voltaje: int, eficiencia: str, precio: float, tamanio: float):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__tamanio = tamanio

    def set_tamanio(self, tamanio: float):
        self.__tamanio = tamanio

    def get_tamanio(self):
        return self.__tamanio

    # sobreescribir 'update' calculadora de descento public
    def calculadora_precio_total(self):
        descuento_eficiencia = super().calculadoraDescuento()
        precio_total = self.__precio - descuento_eficiencia
        return precio_total

    # sobreescribir 'update' imprimirCaratecristicas() public
    # def imprimirCaracteristicas(self):
    #    super().imprimirCaracteristicas()
    #    print("Tamanio: ",self.tamanio)

    def __str__(self):
        descuento = self.calculadoraDescuento() * 100
        precio_total = self.calculadora_precio_total
        imp =  f"\nTipo de TVs: {super().__str__()}"
        imp += f"\nTamanio: {self.__tamanio}"
        imp += f"\nDescuento aplicado: {descuento}"
        imp += f"\nValor total despues del descuento: {precio_total}"
        return imp
