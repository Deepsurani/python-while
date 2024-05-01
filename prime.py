a = int(input("Enter the value: "))

x = 0
i = 2
while i <= a/2:
    if a % i == 0:
        x = 1
        break
    i += 1

if x == 0:
    print(str(a) + " is a prime number")
else:
    print(str(a) + " is not a prime number")
