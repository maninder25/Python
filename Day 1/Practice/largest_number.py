# Write a Python program to find the largest of 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a,"is the Largest number.")
elif b > a and b > c:
    print(b,"is the Largest number.")
elif c > a and c > b:
    print(c,"is the Largest number.")
elif a == b and a > c:
    print(a, "is Largest (two numbers are equal)")
elif b == a and b > c:
    print(b, "is Largest (two numbers are equal)")
elif c == a and c > b:
    print(c, "is Largest (two numbers are equal)")
elif b == c and b > a:
    print("First and Second are equal and largest.")
elif a == b == c:
    print("All numbers are equal.")