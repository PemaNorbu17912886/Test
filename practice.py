
age = int(input("Enter your age:"))
student = input("Are you a student? (yes/no):")

if age <= 12:
    print("You are eligible for a discount.")
elif 13 <= age <= 18 and is_student == "yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
