# task 7

amount = int(input("Enter amount: "))
for i in [100, 50, 20, 10, 5, 1]:
    count = amount // i
    if count > 0:
        print(count, "x", i)
        amount = amount % i