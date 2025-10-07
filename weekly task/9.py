# task 9

n = 2*4 - 1
for i in range(n):
    for j in range(n):
        num = 4 - min(i, j, n-1-i, n-1-j)
        print(num, end="")
    print()