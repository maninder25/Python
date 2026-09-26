# Factorial Number

a = int(input("Enter number: "))

result = 1
for i in range(a, 0, -1):
    result = result * i
print(f"The factorial of {a} is: {result}")