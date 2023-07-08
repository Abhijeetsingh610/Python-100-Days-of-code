from question import Question
from data import question_data
from quiz import Quiz

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text , question_answer)
    question_bank.append(new_question)


quiz = Quiz(question_bank)

while quiz.still_q():
    quiz.next_q()

print("\nYour quiz has been completed")
print(f"Your final score is : {quiz.score}/{quiz.question_num}")