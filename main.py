from Tecnologia import Tecnologia
from Transporte import Transporte
from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter



def menu():
    opcion: "n"
    while opcion!='n':
        print("Bienvenido")
        print("-------------")
        print("puedes realizar las siguentes opciones: ")
        print("ingrea 1 para Registrar elemento (Tvs,Consolas,Scooters o Bicicletas) a la lista")
        print("ingresa 2 para cotizar elementos (Tvs,Consolas,Scooters o Bicicletas) ")
        op = input("Ingreese la opcion a eleccionar: ")
        if op.lower()=="1" or op.lower()=="2":
            cotizarElementos(int(op))
        else:
            print("la opcion es invalida ")
        opcion = input("Desea realizar otra opcionb: s/n")

        
def cotizarElementos(opcion:int):
    if opcion == 1:
        registrarElementos()
    else:
        imprimirCaracteristicas()


def registrarElementos():
    pass

def imprimirCaracteristicas():
    pass

menu()
