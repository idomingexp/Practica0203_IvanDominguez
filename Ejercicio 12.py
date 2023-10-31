a = input("Dime una lista de Nº separados por comas:")
a = a.split(",")
m = 0
dt = 0
sc = 0
for x in range(len(a)):
    m = m + int(a[x])
m = m / len(a)
for x in range(len(a)):
    sc = sc + (int(a[x]) - m) ** 2
dt = (sc / len(a)) ** (1/2)
print("La media es; {} y la desviación típica es: {}".format(m, dt))
input()