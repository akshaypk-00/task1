n = int(input("Enter n: "))  
size = 2*n - 1
for i in range(size):
    for j in range(size):
        num = n - min(i, j, size-1-i, size-1-j)
        print(num, end="")
    print()