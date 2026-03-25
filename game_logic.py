# game_logic.py
import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste aus."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt den Fortschritt des Schneemannes und des Wortes an."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Wort: {display_word}")
    print(f"Fehler: {mistakes} / {len(STAGES) - 1}")
    print(f"Geratene Buchstaben: {', '.join(guessed_letters)}")
    print("=" * 30 + "\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Willkommen zu Snowman Meltdown!")

    # Spielschleife
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Rate einen Buchstaben: ").lower().strip()

        # Validierung Buchstaben
        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib nur einen einzelnen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print(f"Du hast '{guess}' bereits versucht!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Gut gemacht! '{guess}' ist im Wort enthalten.")
        else:
            print(f"Leider nein. '{guess}' ist nicht dabei.")
            mistakes += 1

        # Überprüfen, ob alle Buchstaben gefunden wurden mittels Set
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Herzlichen Glückwunsch! Du hast den Schneemann gerettet!")
            return  # Beendet die Funktion und somit das Spiel

    # Ende der Schleife ohne Return = Spiel verloren
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Oje, der Schneemann ist geschmolzen...")
    print(f"Das Wort war: {secret_word}")

def main():
    while True:
        play_game()
        again = input("Noch einmal spielen? (ja/nein): ").lower().strip()
        if again not in ["ja", "j", "yes", "y"]:
            print("Danke fürs Spielen!")
            break

if __name__ == "__main__":
    main()