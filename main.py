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
            nombre = input("Ingrese el nombre del Tv: ")
            precio = float(input("Ingrese el precio del Tv: "))
            marca = input("Ingrese la marca del Tv: ")
            tv = Tv(nombre, precio, marca)
            productos.append(tv)
            print("Tv registrado exitosamente.")

        elif opcion == 2:
            nombre = input("Ingrese el nombre de la Consola: ")
            precio = float(input("Ingrese el precio de la Consola: "))
            plataforma = input("Ingrese la plataforma de la Consola: ")
            consola = Consola(nombre, precio, plataforma)
            productos.append(consola)
            print("Consola registrada exitosamente.")

        elif opcion == 3:
            aro= float(input("Ingrese el aro del Scooter: "))
            velocidad = int(input("Ingrese la velocidad del Scooter: "))
            peso = float(input("Ingrese el peso del Scooter: "))
            scooter = Scooter(aro, velocidad, peso)
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
            for producto in productos:
                total += producto.cotizar()
            print("El total a cotizar es:", total)

        elif opcion == 6:
            print("Gracias por usar el programa.")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
