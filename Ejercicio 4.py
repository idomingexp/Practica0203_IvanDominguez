a = input("Dime los numeros ganadores de la loteria separados por espacios:")
a = a.split(" ")
for x in range(len(a)):
    print(min(a))
    a.remove(min(a))
input()