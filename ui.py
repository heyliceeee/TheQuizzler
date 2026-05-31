import os
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362" # color of the theme
FONT = ("Arial", 20, "italic") # font of the text
dir_path = os.path.dirname(os.path.realpath(__file__)) # get the path of the current file

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain # create a quiz_brain object
        self.window = Tk() # create a window
        self.score_label = None  # create a label
        self.canvas = None # create a canvas
        self.question_text = None # create a canvas
        self.right_btn = None # create a button
        self.wrong_btn = None # create a button
        self.create_window() # create the window
        self.create_labels() # create the labels
        self.create_canvas() # create the canvas
        self.create_btns() # create the buttons
        self.get_next_question() # get the next question
        self.window.mainloop() # continuously run the program

    def true_pressed(self):
        """
        when the user presses the true button, check if the answer is correct
        """
        is_right = self.quiz.check_answer("True") # check if the user's answer is correct, if it is, increase the score by 1
        self.give_feedback(is_right) # give feedback to the user
    def false_pressed(self):
        """
        when the user presses the true button, check if the answer is false
        """
        is_right = self.quiz.check_answer("False")  # check if the user's answer is correct, if it is, increase the score by 1
        self.give_feedback(is_right)  # give feedback to the user
    def give_feedback(self, is_right):
        """
        change the background color of the window and get the next question after 1 second
        :param is_right: is the answer correct?
        """
        if is_right: # if the answer is correct
            self.canvas.config(bg="green") # change the background color of the canvas to green
        else: # if the answer is wrong
            self.canvas.config(bg="red") # change the background color of the canvas to red
        self.window.after(1000, self.get_next_question) # get the next question after 1 second
    def get_next_question(self):
        """
        get the next question from the quiz_brain object and display it on the canvas
        """
        self.canvas.config(bg="white") # change the background color of the canvas to white
        if self.quiz.still_has_questions(): # if there are still questions left
            self.score_label.config(text=f"Score: {self.quiz.score}") # set the score label to the current score
            q_text = self.quiz.next_question() # get the next question
            self.canvas.itemconfig(self.question_text, text=q_text) # set the text of the question
            
        else: # if there are no more questions
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!") # display a message
            self.right_btn(state="disabled") # disable the true button
            self.wrong_btn(state="disabled") # disable the false button
    def create_window(self):
        """
        create a window, set a title, and set the padding
        """
        self.window.title("Quizzler") # set the title of the window
        self.window.config(padx=20, pady=20)  # set the padding of the window
        self.window.tk.call("tk_setPalette", THEME_COLOR)  # set the background color of the window
    def create_labels(self):
        """
        create the labels, set the text, and place them on the window
        """
        self.score_label = Label(text=f"Score: 0", font=("Arial", 15), fg="white", bg=THEME_COLOR)  # create a label
        self.score_label.grid(column=1, row=0) # place the label on the window
        self.score_label.config(justify="right") # set the alignment of the label
    def create_canvas(self):
        """
        create the canvas, set the background color, and place it on the window
        """
        self.canvas = Canvas(width=300, height=250, bg="white") # create a canvas
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", width=280, fill=THEME_COLOR, font=FONT) # create a text
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50) # place the canvas on the window
    def create_btns(self):
        """
        create the buttons, set the text, and place them on the window
        """
        right_img = PhotoImage(file=f"{dir_path}/images/true.png") # get the path of the image
        self.right_btn = Button(command=self.true_pressed, image=right_img, bg=THEME_COLOR, highlightthickness=0)  # create the button
        self.right_btn.image = right_img # set the image of the button
        self.right_btn.grid(column=0, row=2)  # place the button on the window

        wrong_img = PhotoImage(file=f"{dir_path}/images/false.png") # get the path of the image
        self.wrong_btn = Button(command=self.false_pressed, image=wrong_img, bg=THEME_COLOR, highlightthickness=0) # create the button
        self.wrong_btn.image = wrong_img # set the image of the button
        self.wrong_btn.grid(column=1, row=2) # place the button on the window