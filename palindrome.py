num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    reverse_num += num % 10
    num //= 10
    if num > 0:
        reverse_num *= 10

if num == reverse_num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
