import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current progress of the secret word."""
    # ASCII-Art basierend auf den Fehlern anzeigen
    print(STAGES[mistakes])

    # Erstelle die Anzeige des Wortes (Buchstaben oder Unterstriche)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0  # Startzustand: 0 Fehler

    print("Welcome to Snowman Meltdown!")

    # Zeige den Anfangs Spielzustand
    display_game_state(mistakes, secret_word, guessed_letters)

    # Erster Test-Prompt (Logik wird später erweitert)
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    print("You guessed:", guess)

if __name__ == "__main__":
    play_game()