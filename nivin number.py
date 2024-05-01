a = int(input("Enter the number: "))
sum = 0

while a > 0:
    reminder = a % 10
    sum = sum + reminder
    a = a // 10

if a % sum == 0:
    print("This is a Niven number")
else:
    print("This is not a Niven number")
