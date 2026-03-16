class HangmanGame:
    MAX_MISTAKES = 7

    def __init__(self, word: str):
        self.word = word.lower()
        self.guessed_letters: set[str] = set()
        self.mistakes = 0
        self.game_over = False
        self.won = False

    def get_display(self) -> str:
        display = []
        for char in self.word:
            if char in self.guessed_letters:
                display.append(char)
            else:
                display.append("_")
        return " ".join(display)

    def guess_letter(self, letter: str) -> bool:
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Please enter a single alphabetic character")
        if letter in self.guessed_letters:
            raise ValueError(f"Letter '{letter}' already guessed")
        if self.game_over:
            raise ValueError("Game is over")

        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.mistakes += 1
            if self.mistakes >= self.MAX_MISTAKES:
                self.game_over = True
                self.won = False
        else:
            if all(c in self.guessed_letters for c in self.word):
                self.game_over = True
                self.won = True
        return letter in self.word

    def guess_word(self, guess: str) -> bool:
        guess = guess.lower()
        if not guess.isalpha():
            raise ValueError("Please enter a valid word (alphabetic characters only)")
        if self.game_over:
            raise ValueError("Game is over")

        if guess == self.word:
            self.guessed_letters.update(set(self.word))
            self.game_over = True
            self.won = True
            return True
        else:
            self.mistakes = self.MAX_MISTAKES
            self.game_over = True
            self.won = False
            return False

    def get_used_letters(self) -> str:
        return " ".join(sorted(self.guessed_letters))

    def get_remaining_mistakes(self) -> int:
        return self.MAX_MISTAKES - self.mistakes
