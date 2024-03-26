import json
from question import Question

class QuizBank:
  def __init__(self, filename):
    self.questions = self.load_questions_from_file(filename)

  def load_questions_from_file(self, filename):
    with open(filename, 'r') as f:
      data = json.load(f)
      questions = {}
      for category, question_data in data.items():
        questions[category] = [Question(**q) for q in question_data]
      return questions

  def get_categories(self):
    return list(self.questions.keys())

  def get_questions(self, category):
    return self.questions.get(category, [])

