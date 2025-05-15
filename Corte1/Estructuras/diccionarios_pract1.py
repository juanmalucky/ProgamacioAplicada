# Diccionarios de sensores y cámaras
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print("Sensores:", sensors)
print("Número de cámaras:", num_cameras)

# Diccionario de traducciones
dictionary = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print("Traducciones:", dictionary)

# Diccionario con listas (hijos de familias)
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
print("Hijos de familias:", children)

# Diccionario vacío
my_empty_dictionary = {}
print("Diccionario vacío:", my_empty_dictionary)

# Menú de comida
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Menú antes:", menu)
menu["cheesecake"] = 8
print("Menú después:", menu)

# Actualización de diccionarios
sensors.update({"guest room": 25, "patio": 34})
print("Sensores actualizados:", sensors)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print("Usuarios antes:", user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print("Usuarios después:", user_ids)

# Sobreescribir valores en un diccionario
menu["oatmeal"] = 5
print("Menú con valores sobrescritos:", menu)

oscar_winners = {
    "Best Picture": "La La Land", 
    "Best Actor": "Casey Affleck", 
    "Best Actress": "Emma Stone", 
    "Animated Feature": "Zootopia"
}
print("Ganadores del Oscar antes:", oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print("Ganadores del Oscar después:", oscar_winners)

# Comprensión de diccionarios
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
students = {key: value for key, value in zip(names, heights)}
print("Alturas de estudiantes:", students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}
print("Bebidas y cafeína:", drinks_to_caffeine)

# Diccionario con listas de reproducción
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
plays.update({"Purple Haze": 1, "Respect": 94})
print("Reproducciones de canciones:", plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print("Biblioteca de música:", library)
