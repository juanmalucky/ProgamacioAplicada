times = input("Ingrese el número de veces: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("No hagas nada")
else:
    for i in range(1,times+1):
        print("i = ", i)
