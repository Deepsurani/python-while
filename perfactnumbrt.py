
num = int(input("Enter a number: "))
n = 0
i = 1

while i < num:
    if num % i == 0:
        n += i
    i += 1
if n == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
