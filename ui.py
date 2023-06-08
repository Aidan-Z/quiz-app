from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_b: QuizBrain):
        self.score = 0
        self.quiz = quiz_b
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("340x540")
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="QUESTION",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.score_keep = Label(text=f'Score: {self.score}', font=("Arial", 20, "italic"), bg=THEME_COLOR)
        self.score_keep.grid(row=0, column=1, pady=20)

        tic_img = PhotoImage(file="images/false.png")
        self.tic = Button(image=tic_img, command=self.f_a)
        self.tic.grid(row=2, column=1, pady=20, padx=20)

        check_img = PhotoImage(file="images/true.png")
        self.check = Button(image=check_img, command=self.t_a)
        self.check.grid(row=2, column=0, pady=20, padx=20)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='END OF QUIZ')
            self.tic.config(state='disabled')
            self.check.config(state='disabled')

    def f_a(self):
        self.g_feedbakc(self.quiz.check_answer("False"))

    def t_a(self):
        self.g_feedbakc(self.quiz.check_answer("True"))

    def g_feedbakc(self, is_right):
        self.window.after(500, self.get_next_q)
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.score_keep.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')

