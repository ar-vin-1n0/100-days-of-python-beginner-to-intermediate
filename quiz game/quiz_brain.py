class QuizBrain:
    def __init__(self,q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        curr_question = self.question_list[self.question_number]

        answer = input(f"Q {self.question_number + 1 } :{curr_question.question} [True/False]: :")
        self.question_number += 1
        self.check_answer(answer, curr_question,)

    def check_answer(self, answer,curr_question):


        if answer.lower() == curr_question.answer.lower():
            self.score += 1
            print(f"Correct! You got it")
        else:
            print(f"Wrong! You got it wrong")
        print(f"the right answer was {curr_question.answer}")

        print(f"ur score is {self.score}/{self.question_number}")


