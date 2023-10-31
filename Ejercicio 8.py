a = list(input("Dime una palabra:"))
b = a[::-1]
if a == b:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
input()