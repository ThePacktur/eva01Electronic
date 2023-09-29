class Transporte:
    def __init__(self,costeDespacho_base:int):
        self.__costeDespacho_base = 4000

    def set_costeDespacho_base(self,costeDespacho_base:int):
        self.__costeDespacho_base = costeDespacho_base

    def get_costeDespacho_base(self):
        return self.__costeDespacho_base
    
    
    def __str__(self):
        imp = f"\ncoste base del despacho: {self.__costeDespacho_base}" 
        return imp