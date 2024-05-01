a = int(input("Write any number: "))
ab = a
sum = 0

while a != 0:
    remainder = a % 10
    sum = sum + (remainder ** 3)
    a = int(a / 10)

if sum == ab:
    print("This number is Armstrong:->"+str(ab))
else:
    print("This number is not Armstrong:->" + str(ab))
