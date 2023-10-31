a = ["Matemáticas", "Física","Química", "Historia", "Lengua"]
b= []
c = []
for x in range(len(a)):
    n = float(input("Dime la nota de {}: ".format(a[x])))
    b.append(n)
for y in range(len(b)):
    if b[y] < 5:
        c.append(a[y])
print("Tus asignaturas suspendidas son:", c)
input() 