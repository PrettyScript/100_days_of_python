from question_model import Question 
from data import question_data

question_bank = []

for question in question_data:
    questions = Question(question['text'], question['answer'])
    question_bank.append(questions)

print(question_bank)