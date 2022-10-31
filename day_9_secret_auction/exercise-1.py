student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    student_grade = student_scores[student]
    # print(student_grade)
    if student_grade > 91:
        student_grades[student] = "Outstanding"
    elif student_grade > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_grade > 70:
        student_grades[student] = "Acceptable"
    elif student_grade < 70:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
