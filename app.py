def calculateGrade(average):
  if average >= 90:
    return "O"

  elif average >= 80:
    return "A+"

  elif average >= 70:
    return "A"

  elif average >= 60:
    return "B+"

  elif average >= 50:
    return "B"

  elif average >= 40:
    return "C"
  else:
    return "Fail"


name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
print("Enter subject name and marks: ")
subjects = dict()
total = 0
for i in range(n):
  subject_name, marks = input().split()
  subjects[subject_name] = marks
  total += int(marks)

average = total / n

grade = calculateGrade(average)

print()
print("RESULT")
print(f"Student: {name}")
print()
for subject in subjects:
  print(f"{subject} - {subjects[subject]}")
print()
print(f"AVERAGE: {average:.2f}")
print(f"GRADE: {grade}")