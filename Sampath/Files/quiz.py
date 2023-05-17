questions = [
    {
        "question": "What is the capital of AndhraPradesh?",
        "options": ["Hyderabad", "kakinada", "Vijayawada", "Amravathi"],
        "answer": "Paris"
    },
    {
        "question": "Who is the son of Legartah Lothbroke and Ragner Lorthbroke?",
        "options": ["Bjorn", "Ivar", "ubbe", "Sigaurd"],
        "answer": "Bjorn"
    },
    {
        "question": "Who is the fourth hokage?",
        "options": ["Hashirama", "Thobirama", "Hiruzen", "Minato"],
        "answer": "Minato"
    }
]
def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = input("Your answer (enter the option number): ")
    if options[int(user_answer)-1] == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

score = 0
total_questions = len(questions)

print("Welcome to the Quiz!")
print("Answer the following questions:")

for question in questions:
    score = score + ask_question(question["question"], question["options"], question["answer"])
    print()

print("Quiz complete!")
print(f"Your scorre, {score} out of", {total_questions})
