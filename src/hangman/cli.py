import sys
from typing import Optional

from hangman.word_selector import select_random_word
from hangman.game import HangmanGame


DIFFICULTIES = ["easy", "medium", "hard"]


def get_difficulty() -> Optional[str]:
    print("\nSelect difficulty:")
    for i, diff in enumerate(DIFFICULTIES, 1):
        print(f"  {i}. {diff.capitalize()}")
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return DIFFICULTIES[int(choice) - 1]
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess() -> str:
    while True:
        guess = input("\nEnter a letter or guess the full word: ").strip()
        if guess:
            return guess


def play_game(difficulty: Optional[str] = None, keep_settings: bool = False) -> None:
    if not keep_settings:
        difficulty = get_difficulty()

    word = select_random_word(difficulty)
    game = HangmanGame(word)
    diff_display = difficulty.capitalize() if difficulty else "Random"

    print(f"\n{'=' * 40}")
    print("HANGMAN")
    print(f"{'=' * 40}")
    print(f"Difficulty: {diff_display}")
    print(f"Word length: {len(word)} characters")
    print(f"Max mistakes: {game.MAX_MISTAKES}")
    print(f"{'=' * 40}\n")

    while not game.game_over:
        print(f"Word: {game.get_display()}")
        print(f"Mistakes: {game.mistakes} / {game.MAX_MISTAKES}")
        print(f"Remaining: {game.get_remaining_mistakes()}")
        print(f"Used letters: {game.get_used_letters() or '(none)'}")

        guess = get_guess()

        if len(guess) == 1:
            try:
                game.guess_letter(guess)
            except ValueError as e:
                print(f"\nError: {e}")
        else:
            if game.guess_word(guess):
                print(f"\nCongratulations! You guessed the word: {game.word}")
            else:
                print(f"\nSorry, the word was: {game.word}")
                game.game_over = True
                game.won = False

    if game.won:
        print("\nCongratulations! You won!")
        print(f"The word was: {game.word}")
    else:
        print("\nGame over! You lost.")
        print(f"The word was: {game.word}")


def main() -> None:
    print("Welcome to Hangman!")

    while True:
        play_game()

        while True:
            response = input("\nPlay again? (y/n): ").strip().lower()
            if response in ["y", "yes"]:
                while True:
                    keep = (
                        input("Keep using the same difficulty? (y/n): ").strip().lower()
                    )
                    if keep in ["y", "yes"]:
                        play_game(keep_settings=True)
                        break
                    elif keep in ["n", "no"]:
                        play_game(keep_settings=False)
                        break
                break
            elif response in ["n", "no"]:
                print("\nThanks for playing!")
                sys.exit(0)


if __name__ == "__main__":
    main()
