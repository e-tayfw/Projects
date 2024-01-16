from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler Program")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score_label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}", padx=20, pady=20, fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # canvas_text
        self.quiz_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            font=FONT,
        )

        # Buttons

        right_img = PhotoImage(file="quizzler-app/images/true.png")
        self.right_btn = Button(
            image=right_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.true_passed,
        )
        self.right_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="quizzler-app/images/false.png")
        self.false_btn = Button(
            image=false_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.false_passed,
        )
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You are done with the quiz")
            self.right_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_passed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
