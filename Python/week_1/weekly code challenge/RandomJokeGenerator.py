import random

print("\n Random joke Generator")

jokes = [ 
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
    {
        "joke": "Why do programmers prefer dark mode?",
        "answer": "Because light attracts bugs!!"
    },
    {
        "joke": "How many programmers does it take to change a light bulb?",
        "answer": "None, that's a hardware problem."

    },
    {
        "joke": "Why do Python programmers prefer functions to snakes?",
        "answer": "Because they’re easier to debug!"
    },
    {
        "joke": "Why do programmers hate nature?",
        "answer": "It has too many bugs."
    },
    {
        "joke": "What’s the object-oriented way to become wealthy?",
        "answer": "Inherit it."
    },
    {
        "joke": "Debugging is like being the detective in a crime movie...",
        "answer": "…where you’re also the murderer"  
    },
    {
        "joke": "What's a programmer’s favorite hangout place?",
        "answer": "The Foo Bar.!"
    },
    {
        "joke": "Why did the Python programmer have to leave the restaurant?",
        "answer": "Because they kept asking for their script to be executed!!"
    },
    {
        "joke": "Why do Java developers wear glasses?",
        "answer": "Because they don’t see sharp."
    },
    {
        "joke": "Why was the programmer always calm?",
        "answer": "Because they knew how to handle exceptions."
    },
    {
        "joke": "Programming is like a relationship.",
        "answer": "You break up with one mistake, and you’re left debugging it for months."
    },
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
    {
        "joke": "Why did the Python break up with the JavaScript?",
        "answer": "Because it didn’t like promises!"
    },
        {
        "joke": "A SQL query walks into a bar, goes up to two tables, and says…",
        "answer": "'Can I join you?'"
    },
    

]

def RandomJokeGenerator(jokes):
    random_joke = random.choice(jokes)
    print(f"\nJoke: {random_joke['joke']}")
    print(f"Answer: {random_joke['answer']}")


RandomJokeGenerator(jokes)