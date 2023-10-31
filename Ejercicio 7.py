import string
a = list(string.ascii_lowercase)
for x in range (len(a), 1, -1):
    if x%3 == 0:
        a.pop(x-1)
print(a)
input()