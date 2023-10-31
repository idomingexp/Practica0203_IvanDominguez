a = ["Matemáticas", "Física","Química", "Historia", "Lengua"]
b = []
for x in range(len(a)):
    n = input("Dime la nota de {}: ".format(a[x]))
    b.append(n)
for x in range(len(a)):
    print("En {}, has sacado: {}".format(a[x], b[x]))
input()