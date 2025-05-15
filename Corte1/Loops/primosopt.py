tope_rango = 30

# Código optimizado con break y límite en √n
print("Números primos:")
n = 2  # Empezar en 2
while n < tope_rango:
    primo = True
    for div in range(2, int(n ** 0.5) + 1):  # Solo hasta √n
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    n += 1

# Comparación de ciclos
print("\nComparación de ciclos:")

# Sin break
ciclos_sin_break = 0
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, n):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False
    n += 1

# Con break
ciclos_con_break = 0
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(n ** 0.5) + 1):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break
    n += 1

# Mostrar resultados
print(f'Cantidad de ciclos sin break: {ciclos_sin_break}')
print(f'Cantidad de ciclos con break: {ciclos_con_break}')
print(f'Se optimizó a un {100 * ciclos_con_break / ciclos_sin_break:.2f}% aplicando break')
