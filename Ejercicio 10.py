a = [50, 75, 46, 22, 80, 65, 8]
m = mx = a[0]
for x in range(len(a)):
    if a[x] > mx:
        mx = a[x]
    if a[x] < m:
        m = a[x]
print("El precio mayor es {} y el menor es {}".format(mx, m))
input()