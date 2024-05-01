n = int(input("Enter the number : "))
i = 1
harmonic = 0
while i <= n:
    harmonic += 1 / i
    i += 1
print("The sum of the harmonic series with", n, "is:", harmonic)