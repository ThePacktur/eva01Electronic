from Transporte import Transporte


class Bicicleta(Transporte):
    def __init__(self, costeDespacho_base: int, aro: float, peso: float, precio: float, marca: str):
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

    def calcularDespacho(self):
        precio_despocho = super().get_costeDespacho_base()
        peso_total += precio_despocho + self.precio * 400
        return peso_total

    def cotizar(self):
        return self.calcularDespacho

    def __str__(self):
        imp = super().__str__()
        imp += f"\naro: {self.__aro}"
        imp += f"\npeso: {self.__peso}"
        imp += f"\nmarca: {self.__marca}"
        return imp
