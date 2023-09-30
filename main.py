from Tecnologia import Tecnologia
from Transporte import Transporte
from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter


def menu():
    productos = []
    while True:
        print("----- Menú -----")
        print("1. Registrar Tv")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar productos")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            voltaje = int(input("Ingrese el voltaje del Tv (volt): "))
            precio = float(input("Ingrese el precio del Tv: "))
            eficiencia = input("Seleccione la eficiencia de la Tv (A,B,C,D,E or F): ")
            marca = input("Ingrese la marca de la televicion: ")
            tamanio = float(input("Ingrese el tamanio de la televicion: "))
            tv = Tv(voltaje,precio,eficiencia, marca, tamanio)
            productos.append(tv)
            print("Tv registrado exitosamente.")

        elif opcion == 2:
           
            voltaje = int(input("Ingrese el voltaje de la Consola: "))
            precio = float(input("Ingrese el precio de la Consola: "))
            eficiencia = input("Seleccione la eficiencia de la Consola (A,B,C,D,E or F):")
            marca = input("Ingrese la marca de la Consola: ")
            nombreConsola = input("Ingrese el nombre de la Consola: ")
            version = input("Ingrese si la consola es Lite  or normal: ")
            consola = Consola(voltaje ,precio,marca,nombreConsola ,version)
            productos.append(consola)
            print("Consola registrada exitosamente.")

        elif opcion == 3:
            voltaje = int(input("Ingrese el voltaje del scooter: "))
            precio = float(input("Ingrese el precio del scooter: "))
            eficiencia = input("Seleccione la eficiencia del scooter (A,B,C,D,E or F):")
            marca = input("Ingrese la marca del scooter: ")
            aro= float(input("Ingrese el aro del Scooter: "))
            velocidad = int(input("Ingrese la velocidad del Scooter: "))  #error typeError: bicicleta.__init__() missing 2 requered positional argument: 'precio' and 'marca'
            peso = float(input("Ingrese el peso del Scooter: "))
            scooter = Scooter(voltaje,precio,eficiencia,aro, velocidad, peso)
            productos.append(scooter)
            print("Scooter registrado exitosamente.")

        elif opcion == 4:
            aro = float(input("Ingrese el aro de la Bicicleta: "))
            peso = float(input("Ingrese el peso de la Bicicleta: "))
            precio = input("Ingrese el precio de la Bicicleta: ")
            marca = input("Ingrese la marca de la bicicleta: ")
            bicicleta = Bicicleta(aro, peso, precio,marca)
            productos.append(bicicleta)
            print("Bicicleta registrada exitosamente.")

        elif opcion == 5:
            total = 0
            for producto in productos:  #error for producto in productor
                total += producto.cotizar() #attributError: 'TV' object has no attribute 'Cotizar'
            print("El total a cotizar es:", total)

        elif opcion == 6:
            print("Gracias por elegir nuestro programa.")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu() #Traceback (most recent call last)
