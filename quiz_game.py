questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. New York"],
        "answer": "A"
    },
    {
        "prompt": "Who is the leader of the Guns N Roses?",
        "options": ["A. Slash", "B. Axl Rose", "C. Steven Adler"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 2", "B. 3", "C. 5"],
        "answer": "A"
    },
    {
        "prompt": "What is the currency of Japan?",
        "options": ["A. Euro", "B. Dollar", "C. Yen"],
        "answer": "C"
    }
]

def play_game(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, or C): ")
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"You scored {score} out of {len(questions)}.")

play_game(questions)