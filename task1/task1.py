import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
mas = []

for i in range(1, n + 1, 1):
    mas.append(i)

index = 0
join = ""

while True:
    join += str(mas[index])
    index += m-1
    if index > (n-1):
        index = index % n
    if mas[index] == 1:
        break

print(join)