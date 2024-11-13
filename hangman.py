import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct! " + " ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
        
        if "_" not in guessed:
            print("Congratulations, you guessed the word!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

hangman()
