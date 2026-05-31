import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Returns True or False depending on whether there are still questions left."""
        return self.question_number < len(self.question_list)
    def next_question(self):
        """Advances the quiz to the next question."""
        self.current_question = self.question_list[self.question_number] # Assigns the current question to the next question in the list
        self.question_number += 1 # Increments the question number
        q_text = html.unescape(self.current_question.text) # Unescapes the question text
        return f"Q.{self.question_number}: {q_text}"
    def check_answer(self, user_answer):
        """Checks if the user's answer is correct."""
        correct_answer = self.current_question.answer # Gets the correct answer from the current question
        if user_answer == correct_answer: # Checks if the user's answer is the same as the correct answer
            self.score += 1 # If it is, increments the score
            return True
        else:
            return False