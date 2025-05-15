################# LISTAS ####################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print("Lista inicial:", my_lista)
print("Tipo:", type(my_lista))
print("Elemento en índice 2:", my_lista[2])
print("Tamaño de la lista:", len(my_lista))
print("Primeros dos elementos:", my_lista[:2])

# Agregar elementos
my_lista.append('Blanco')
print("Lista después de append:", my_lista)

my_lista.insert(3, 'Negro')
print("Lista después de insert en índice 3:", my_lista)

my_lista.extend(['Marrón', 'Gris'])
print("Lista después de extend:", my_lista)

# Índice de un elemento
print("Índice de 'Azul':", my_lista.index('Azul'))

# Eliminar elementos
my_lista.remove('Marrón')
print("Lista después de remove('Marrón'):", my_lista)

my_lista.insert(8, 'Marrón')
print("Lista después de insertar 'Marrón' en índice 8:", my_lista)

# Extraer el último elemento con pop()
eliminado = my_lista.pop()
print("Elemento eliminado con pop():", eliminado)
print("Lista después de pop:", my_lista)
print("Nuevo tamaño de la lista:", len(my_lista))

# Multiplicar lista
my_lista_3 = my_lista * 3
print("Lista multiplicada por 3:", my_lista_3)

# Ordenar listas
my_lista.sort()
print("Lista ordenada:", my_lista)

# Lista numérica
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Lista numérica original:", my_NumList)

my_NumList.sort()
print("Lista numérica ordenada ascendente:", my_NumList)

my_NumList.sort(reverse=True)
print("Lista numérica ordenada descendente:", my_NumList)

################# TUPLAS ####################
print("\n############ TUPLAS #########")

# Convertir lista a tupla
my_tupla = tuple(my_lista)
print("Tupla creada a partir de lista:", my_tupla)

# Acceder a elementos
tuple_values = (my_tupla[0], my_tupla[2])
print("Elementos en índice 0 y 2:", tuple_values)

# Comprobar si un elemento está en la tupla
print("'Rojo' en tupla:", 'Rojo' in my_tupla)
print("Número de veces que 'Rojo' aparece en la tupla:", my_tupla.count('Rojo'))

# Tupla con un solo elemento
my_tupla_unitaria = ('Blanco',)
print("Tupla con un solo elemento:", my_tupla_unitaria)

# Empaquetado de tupla
my_tupla = ('Gaspar', 5, 8, 1999)
print("Tupla empaquetada:", my_tupla)

# Desempaquetado de tupla
nombre, dia, mes, año = my_tupla
print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {año}")

# Convertir tupla en lista
my_lista2 = list(my_tupla)
print("Tupla convertida en lista:", my_lista2)
