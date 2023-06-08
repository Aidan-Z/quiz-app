from question_model import Question
from quiz_brain import QuizBrain
import requests
import pprint as pp
from ui import QuizInterface


response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=medium&type=boolean")
response.raise_for_status()
data = response.json()




question_bank = []

for i in data['results']:
    question_text = i['question']
    question_answer = i['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
