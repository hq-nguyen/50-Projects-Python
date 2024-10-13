import random

class Question:
    def __init__(self, question, options, correct_answer, explanation):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

class QuestionManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.questions = self.load_questions()

    def load_questions(self):
        questions = []
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                question_text = lines[i].strip()
                options = lines[i+1].strip().split(',')
                correct_answer = lines[i+2].strip()
                explanation = lines[i+3].strip()
                questions.append(Question(question_text, options, correct_answer, explanation))
        return questions

    def get_random_question(self):
        return random.choice(self.questions)
    

# def test_load_questions():
#     # Initialize QuestionManager with the path to your question file
#     question_manager = QuestionManager('./Level_1/milionaire/questions.txt')
    
#     # Load questions
#     questions = question_manager.load_questions()

#     # Print out the loaded questions for verification
#     for i, question in enumerate(questions, 1):
#         print(f"Question {i}: {question.question}")
#         print(f"Options: {', '.join(question.options)}")
#         print(f"Correct Answer: {question.correct_answer}")
#         print(f"Explanation: {question.explanation}")
#         print("-" * 30)

# if __name__ == "__main__":
#     test_load_questions()
