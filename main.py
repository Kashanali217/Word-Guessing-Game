import random

welcome_message = """Welcome to Word Guessing Game
Made by Kashan Ali"""
print(welcome_message.center(170))

instructions = """In this game, there is a list of words present, out of which our interpreter will choose 1 random word.
The user first will be asked to guess any alphabet. If the random word contains that alphabet,
it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. 
The user will be given 10 turns to guess the complete word.
"""
print(instructions)

list_of_words = ["lengths", "lucky", "luxury", "subway", "avenue", "transcript", "microwave", "unknown", "psyche", "witchcraft"]
random_word = random.choice(list_of_words)
dash = "_" * len(random_word)

print(dash)

turns = 10
while turns > 0 and "_" in dash:
    user_input = input(f"Guess any alphabet. Turns left: {turns}\n")
    
    if len(user_input) != 1:
        print("Please enter 1 character.")
        continue
    
    if user_input in random_word:
        for i in range(len(random_word)):
            if random_word[i] == user_input:
                dash = dash[:i] + user_input + dash[i+1:]
        print(dash)
    else:
        print("Incorrect guess. Try again.")
    
    turns -= 1

if "_" not in dash:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you ran out of turns. The word was {random_word}.")
