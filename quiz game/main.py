from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



question_bank = []

for q in question_data:
    question_text = q["text"]
    answer_text = q["answer"]
    question_bank.append(Question(question_text, answer_text))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


