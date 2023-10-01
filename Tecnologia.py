
class Tecnologia:
    def __init__(self,marca:str,voltaje:int,eficiencia:str,precio:float):
        self.__marca = marca
        self.__voltaje = voltaje
        
        self.__eficiencia = eficiencia
        self.__precio = precio

    def set_marca(self,marca:str):
        self.__marca = marca

    def get_marca(self):
        return self.__marca
    
    def set_voltaje(self,voltaje:int):
        self.__voltaje = voltaje

    def get_voltaje(self):
        return self.__voltaje
    
    def set_eficiencia(self,eficiencia:str):
        self.__eficiencia = eficiencia

    def get_eficiencia(self):
        return self.__eficiencia
    
    def set_precio(self,precio:float):
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
  
    #crear una calculadora de descuento.
    def calculadoraDescuento(self):
      if self.eficincia in ['A','B']:
          return self.precio * 0.5
      elif self.eficiencia in ['C', 'D']:
          return self.precio * 0.7
      elif self.eficiencia in ['E','F']:
          return self.precio * 0.9
      else: 
          return self.precio

    def cotizar(self):
        descuento = self.calculadoraDescuento
        precio_descuento = self.get_precio * (1 - descuento)
        return precio_descuento


    #tecnologias(marca:str,voltaje:int,precio:float,eficiencia:str)
    def imprimirCaracteristicas(self):
        print("Marca: ", self.__marca)
        print("voltaje: ", self.__voltaje)
        print("Eficiencia: ", self.__eficiencia)
        print("Precio: ", self.__precio) 
               

    def __str__(self):
        imp = f"Voltaje: {self.__voltaje}"
        imp += f"\nPrecio: {self.__precio}"
        imp += f"\nEficiencia: {self.__eficiencia}"
        imp += f"\nMarca: {self.__marca}"
        imp += f"\nCotizar: {self.cotizar}"
        return imp