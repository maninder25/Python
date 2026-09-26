# Student Result Management System

student_name = input("Enter Student Name: ")

num_eng = int(input("Enter marks for English: "))
num_py = int(input("Enter marks for Python: "))
num_ma = int(input("Enter marks for Maths: "))
num_comp = int(input("Enter marks for Computer: "))
num_stats = int(input("Enter marks for Statistics: "))

obt_marks = num_eng + num_py + num_ma + num_comp + num_stats
total_marks = 500
percentage = obt_marks / total_marks * 100

result = "Pass" if percentage >= 50 else "Fail"

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("--------------------------------")
print("Student Result")
print("--------------------------------")
print("Student Name:", student_name)
print(f"Total: {obt_marks} / 500")
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Status:", result)