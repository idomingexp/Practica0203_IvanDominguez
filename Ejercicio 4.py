n = int(input("Dime cuantos Nº ganadores hay:"))
a = []
for x in range(n):
    b = int(input("Dime un número ganador:"))
    a.append(b)
a.sort()
print(a)
input()
