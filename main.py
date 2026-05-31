from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data: # for each question in the data
    question_text = question["question"] # get the question text
    question_answer = question["correct_answer"] # get the correct answer

    new_question = Question(question_text, question_answer) # create a new Question object
    question_bank.append(new_question) # add the new Question object to the list

quiz = QuizBrain(question_bank) # create a new QuizBrain object

while quiz.still_has_questions(): # while there are still questions left
    quiz.next_question() # ask the next question

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
