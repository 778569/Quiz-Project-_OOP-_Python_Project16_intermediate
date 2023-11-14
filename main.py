from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:

    question_text = question["text"]
    question_answer = question["answer"]
    # List_data = question_data[item]
    new_question = Question(q_text = question_text,q_answer= question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your Final Score :{quiz.score}/12.")
