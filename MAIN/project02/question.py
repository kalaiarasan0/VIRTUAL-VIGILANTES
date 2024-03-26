## Python Quiz Application with Object-Oriented Design
class Question:
  def __init__(self, text, choices, answer):
    self.text = text
    self.choices = choices
    self.answer = answer

  def is_correct_answer(self, choice):
    return choice.upper() == self.answer.upper()

  def display(self):
    print(self.text)
    for i, choice in enumerate(self.choices):
      print(f"{chr(65+i)}. {choice}")


