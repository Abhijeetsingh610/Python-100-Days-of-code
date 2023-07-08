class Quiz:

    def __init__(self , q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_q(self):
        return len(self.question_list) > self.question_num

    def next_q(self):
        current_q = self.question_list[self.question_num]
        self.question_num += 1
        user_input = input(f"Q : {self.question_num} : {current_q.text} (True/False):")
        self.check_ans(user_input , current_q.answer)



    def check_ans(self , user_input , correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Correct Answer!")

        else:
            print("Wrong Answer")

        print(f"the correct answer was : {correct_answer} .")
        print(f"Current Score is : {self.score}/{self.question_num}")


