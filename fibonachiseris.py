n = int(input("Enter the number of: "))
a, b = 0, 1
print("Fibonacci series upto", n, ":")
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
