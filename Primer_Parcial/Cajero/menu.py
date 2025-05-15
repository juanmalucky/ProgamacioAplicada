# menu.py

from clase import Cajero

def menu():
    cajero = Cajero(1000)  # Se crea una instancia de Cajero con $1000 de saldo inicial

    while True:
        print("\n==== MENÚ CAJERO ====")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")

        # Pide al usuario que seleccione una opción
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == '1':
            cajero.consultar_saldo()
        elif opcion == '2':
            cajero.depositar()
        elif opcion == '3':
            cajero.retirar()
        else:
            # Muestra un mensaje si la opción no es válida
            print(" Opción inválida. Solo puedes elegir 1, 2 o 3.")
