num = int(input("Enter The Value: "))
odd = 0
even = 0
i = 1

# First while loop for even numbers
while i <= num:
    if i % 2 == 0:
        print("even is: ", i, end="")
        even += 1
    i += 1

i = 1

while i <= num:
    if i % 2 != 0:
        print("\t\t\t\tOdd is :", i)
        odd += 1
    i += 1

print("\nNumber of even numbers: ", even)
print("Number of odd numbers: ", odd)


