from math import ceil

for i in range(int(input())):
    n = int(input())
    n = (n**2 + n + 1) / 2
    print(ceil(n))