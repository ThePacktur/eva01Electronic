from Transporte import Transporte


class Bicicleta(Transporte):
    def __init__(self, costeDespacho_base: 400, aro: float, peso: float, precio: float, marca: str):
        super().__init__(costeDespacho_base)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def set_aro(self, aro: float):
        self.__aro = aro

    def get_aro(self):
        return self.__aro

    def set_peso(self, peso: float):
        self.__peso = peso

    def get_peso(self):
        return self.__peso

    def set_precio(self, precio: float):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_marca(self, marca: str):
        self.__marca = marca

    def get_marca(self):
        return self.__marca
    # crear calculadora de despacho en float.

    def calcular_precio_total(self):
        descuento_eficiencia = super().get_costeDespacho_base() * self.__precio  
        costo_despacho = 4000 + self.__peso * 400
        precio_total = self.__precio - descuento_eficiencia + costo_despacho
        return precio_total

    def __str__(self):
        descuento = super().get_costeDespacho_base() * 100
        costo_despacho = 4000 + self.__peso * 400
        precio_total = self.calcular_precio_total
        imp =  f"\nTipo de bicicleta: {super().__str__()}"
        imp += f"\nAro: {self.__aro}"
        imp += f"\nPeso: {self.__peso}"
        imp += f"\nDescuento eficiencia: {descuento}"
        imp += f"\nCosto total de despacho: {costo_despacho} "
        imp += f"\nPrecio total: {precio_total}"
        return imp