# Prime number checker
a = int(input("Enter number: "))

for i in range(2, a):
    if a % i == 0:
        print(f"{a} is not a Prime Number.")
        break
else:
    print(f"{a} is a Prime Number.")