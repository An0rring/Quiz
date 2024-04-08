questions = [
    {
        "question": "In What year was the first iPhone released?",
        "options": ["A: 2005", "B: 2008", "C: 2007", "D: 2010"],
        "answer": "C"
    },

    {

        "question": "What is the tallest mountain in the world?",
        "options": ["A: K2", "B: Mount Everest", "C: Mount Kilimanjaro", "D: Denali"],
        "answer": "B"


    },

    {

        "question": "What is the world's largest ocean?",
        "options": ["A: Atlantic Ocean", "B: Indian Ocean", "C: Southern Ocean", "D: Pacific Ocean"],
        "answer": "D"


    },

     {

        "question": "What is the smallest country in the world?",
        "options": ["A: Monaco", "B: Vatican City", "C: Malta", "D: San Marino"],
        "answer": "B"


    },

    {

        "question": "What is the chemical symbol for water?",
        "options": ["A: H2O", "B: W", "C: O2", "D: HO"],
        "answer": "A"


    },

       {

        "question": "What is the currency of Japan?",
        "options": ["A: Dollar", "B: Yuan", "C: Euro", "D: Yen"],
        "answer": "D"


    },

       {

        "question": "What is the longest river in the world?",
        "options": ["A: Nile", "B: Amazon", "C: Yangtze", "D: Mississippi"],
        "answer": "A"


    },

    # Add more questions here
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")


