a = input("Ingresa un número "a": ")
a = int(a)
b = input("Ingreso un número "b": ")
b = float(b)
c = a + b

if a == b:
    print("a y b son iguales")
else:
    print("a y b son diferentes")

print("El tipo de dato de "a" es: ", type(a))
print("El tipo de dato de "b" es: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo de dato")
else:
    print("a y b son de diferente tipo de dato")
