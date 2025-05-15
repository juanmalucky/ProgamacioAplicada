from calculadora import Calculadora  # Importamos la clase desde el archivo calculadora.py

# Pedimos al usuario que ingrese dos números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Creamos un objeto de la clase Calculadora con los números dados
calc = Calculadora(a, b)

# Mostramos los resultados de las operaciones
print("El resultado de la suma es:", calc.sumar())
print("El resultado de la resta es:", calc.restar())
print("El resultado de la multiplicacion es:", calc.multiplicar())
print("El resultado de la division es:", calc.dividir())
