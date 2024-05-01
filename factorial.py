sum = 0
s = int(input("Enter the value of s: "))
i = 1
while i <= s:
    print("{i} X {sum}", end="\b")
    sum = i * sum
    i += 1
print(" = ",sum)
