# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

from random import randint

student_scores = {student:randint(1,100) for student in names}
# print(student_scores)

passed_students ={student:student_score for (key, value) in student_scores if student_score > 60}
print(passed_students)