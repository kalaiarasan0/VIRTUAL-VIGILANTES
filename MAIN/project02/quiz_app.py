import time
from quiz_bank import QuizBank

def main():
    # Load questions from a JSON file (replace with your file path)
    quiz_bank = QuizBank(r"D:\virtual internship\MAIN\project02\questions.json")
    while True:
        # Welcome message and category selection
        print("Welcome to the Quiz Application!")
        categories = quiz_bank.get_categories()
        print("Available Categories:")
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")
        print("Press 0 to exit")
        category_choice = int(input("Enter the number of your chosen category: "))
        if category_choice == 0:
            print("Exiting program...")
            break
        elif category_choice not in range(1, len(categories)+1):
            print("Invalid category selection.")
            return

        category = categories[category_choice - 1]
        questions = quiz_bank.get_questions(category)

        # Start timer
        start_time = time.time()

        # Quiz loop
        score = 0
        for question in questions:
            question.display()
            answer_choice = input("Enter your answer (A, B, C, D): ").upper()
            if question.is_correct_answer(answer_choice):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print(f"The correct answer is: {question.choices[ord(question.answer) - ord('A')]}")

            # Display elapsed time periodically
            if len(questions) > 5 and (len(questions) - questions.index(question)) % 2 == 0:
                elapsed_time = int(time.time() - start_time)
                print(f"Time elapsed: {elapsed_time // 60} minutes {elapsed_time % 60} seconds")

        # Display results
        end_time = time.time()
        elapsed_time = int(end_time - start_time)
        print(f"\nQuiz Results - Category: {category}")
        print(f"Score: {score} out of {len(questions)}")
        print(f"Time Taken: {elapsed_time // 60} minutes {elapsed_time % 60} seconds")
        break  # Exit the while loop after displaying the results

if __name__ == "__main__":
    main()
