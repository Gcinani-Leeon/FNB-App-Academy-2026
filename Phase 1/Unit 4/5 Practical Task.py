name = input("Enter your name: ")

mark1 = float(input("Enter your mark for subject 1: "))
mark2 = float(input("Enter your mark for subject 2: "))
mark3 = float(input("Enter your mark for subject 3: "))

mark_avg = (mark1 + mark2 + mark3) / 3

if mark_avg >= 80:
    grade = "A"
elif mark_avg >= 70:
    grade = "B"
elif mark_avg >= 60:
    grade = "C"
elif mark_avg >= 50:
    grade = "D"
elif mark_avg >= 40:
    grade = "Fail"
else:
    grade = "needs intervention"

print(f"Name: {name}")
print(f"Average Mark: {round(mark_avg, 2)}")
print(f"Grade: {grade}")
