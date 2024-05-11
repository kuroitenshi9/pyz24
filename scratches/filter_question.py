import question
from fileloader import load_questions_from_file

question_list = load_questions_from_file('questions.json')

def difficulty_filtr(level):
    def filter_questions(question):
        return question.difficulty == level
    return filter_questions


question_list = load_questions_from_file('questions.json')
easy_questions = filter(difficulty_filtr('hard'), question_list)

for e in easy_questions:
    print(e)
