# cajero.py

class Cajero:
    def __init__(self, saldo_inicial=0):
        # Inicializa el cajero con un saldo predeterminado
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        # Muestra el saldo actual con dos decimales
        print(f"\n Tu saldo actual es: ${self.saldo:.2f}")

    def depositar(self):
        # Permite al usuario ingresar una cantidad para depositar
        try:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            if cantidad <= 0:
                print(" La cantidad debe ser mayor a cero.")
            else:
                self.saldo += cantidad
                print(f" Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        except ValueError:
            # Controla errores si el usuario no ingresa un número válido
            print(" Entrada inválida. Ingresa un número válido.")

    def retirar(self):
        # Permite al usuario ingresar una cantidad para retirar
        try:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad <= 0:
                print(" La cantidad debe ser mayor a cero.")
            elif cantidad > self.saldo:
                print(" Fondos insuficientes.")
            else:
                self.saldo -= cantidad
                print(f" Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        except ValueError:
            # Controla errores si el usuario no ingresa un número válido
            print(" Entrada inválida. Ingresa un número válido.")
