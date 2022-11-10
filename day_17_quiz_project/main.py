from question_model import Question 
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    questions = Question(question['text'], question['answer'])
    question_bank.append(questions)

quiz = QuizBrain(question_bank)
while #if quiz still has questions remaining
quiz.next_question()