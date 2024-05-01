one = int(input("Enter The First Value: "))
sec = int(input("Enter The Second Value: "))
i = one

while i <= sec:
    j = 1
    while j <= 10:
        print(i, "X", j, "=", i*j)
        j += 1
i += 1
