GameName = "Simple Quiz Game"
print(GameName)

questions =[
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["a) Semicolon `;`", "b) Parentheses `()`", "c) Indentation", "d) Curly braces `{}`"],
        "answer": "c"
    },
        {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) def", "c) function", "d) lambda"],
        "answer": "b"
    },
        {
        "question": "What is the correct syntax to output 'Hello, World!' in Python?",
        "options": ["a) print('Hello, World!')", "b) echo('Hello, World!')", "c) printf('Hello, World!')", "d) Console.Write('Hello, World!')"],
        "answer": "a"
    },
    {
        "question": "Which of the following data types is not supported in Python?",
        "options": ["a) String", "b) Integer", "c) Character", "d) Boolean"],
        "answer": "c"
     },
         {
        "question": "How do you start a comment in Python?",
        "options": ["a) //", "b) /* */", "c) <!-- -->", "d) #"],
        "answer": "d"
    },
        {
        "question": "What does the `len()` function do in Python?",
        "options": ["a) Returns the number of characters in a string", "b) Adds items to a list", "c) Removes items from a list", "d) Sorts a list"],
        "answer": "a"
    },
    {
        "question": "Who played the character of Jack in Titanic?",
        "options": ["a) Brad Pitt " , "b) Tom Cruise" , "c) Leonardo DiCaprio" ,"d) Matt Damon"],
        "answer": "c"
    },
    {
        "question": "In The Matrix, what color pill does Neo take?",
        "options": ["a) Blue" ,"b) Red", "c) Green", " d) Yellow"],
        "answer": "b"
    },
    {
        "question": "What is the highest-grossing movie of all time (as of 2024)?",
        "options": ["a) Titanic" ," b) Avengers: Endgame" , "c) Avatar" , "d) Star Wars: The Force Awakens"],
        "answer": "c"
    },
    
]

def SimpleQuizGame(questions):
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is '{q['answer']}'.")
    
    print(f"\nYou scored {score} out of {len(questions)}.")

SimpleQuizGame(questions)