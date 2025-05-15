import time

cadena = 'Python'

for letra in cadena:
   if letra == 'P':
      continue
   print(letra)
   time.sleep(1)
