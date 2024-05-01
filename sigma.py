sum = 0
s = int(input("Enter the value of s: "))
i = 1
while i <= s:
    print(i, "+ ", end="")
    sum = i + sum
    i += 1
print("\b\b= ", sum)
