import pytest
from hangman.game import HangmanGame


class TestHangmanGame:
    def test_init(self):
        game = HangmanGame("hello")
        assert game.word == "hello"
        assert game.guessed_letters == set()
        assert game.mistakes == 0
        assert game.game_over is False
        assert game.won is False

    def test_get_display_all_underscores(self):
        game = HangmanGame("hello")
        assert game.get_display() == "_ _ _ _ _"

    def test_get_display_some_letters(self):
        game = HangmanGame("hello")
        game.guess_letter("l")
        assert game.get_display() == "_ _ l l _"

    def test_get_display_all_letters(self):
        game = HangmanGame("hello")
        game.guess_letter("h")
        game.guess_letter("e")
        game.guess_letter("l")
        game.guess_letter("o")
        assert game.get_display() == "h e l l o"

    def test_guess_letter_correct(self):
        game = HangmanGame("hello")
        result = game.guess_letter("l")
        assert result is True
        assert "l" in game.guessed_letters
        assert game.mistakes == 0

    def test_guess_letter_incorrect(self):
        game = HangmanGame("hello")
        result = game.guess_letter("z")
        assert result is False
        assert "z" in game.guessed_letters
        assert game.mistakes == 1

    def test_guess_letter_invalid_not_single(self):
        game = HangmanGame("hello")
        with pytest.raises(ValueError, match="single"):
            game.guess_letter("ab")

    def test_guess_letter_invalid_not_alpha(self):
        game = HangmanGame("hello")
        with pytest.raises(ValueError, match="alphabetic"):
            game.guess_letter("1")

    def test_guess_letter_already_guessed(self):
        game = HangmanGame("hello")
        game.guess_letter("l")
        with pytest.raises(ValueError, match="already guessed"):
            game.guess_letter("l")

    def test_guess_letter_wins_game(self):
        game = HangmanGame("hi")
        game.guess_letter("h")
        game.guess_letter("i")
        assert game.game_over is True
        assert game.won is True

    def test_guess_letter_loses_game(self):
        game = HangmanGame("hi")
        for letter in ["a", "b", "c", "d", "e", "f", "g"]:
            game.guess_letter(letter)
        assert game.game_over is True
        assert game.won is False
        assert game.mistakes == 7

    def test_guess_word_correct(self):
        game = HangmanGame("hello")
        result = game.guess_word("hello")
        assert result is True
        assert game.game_over is True
        assert game.won is True

    def test_guess_word_incorrect(self):
        game = HangmanGame("hello")
        result = game.guess_word("world")
        assert result is False
        assert game.game_over is True
        assert game.won is False

    def test_guess_word_invalid(self):
        game = HangmanGame("hello")
        with pytest.raises(ValueError, match="valid word"):
            game.guess_word("hello1")

    def test_get_used_letters(self):
        game = HangmanGame("hello")
        game.guess_letter("a")
        game.guess_letter("b")
        game.guess_letter("c")
        assert game.get_used_letters() == "a b c"

    def test_get_remaining_mistakes(self):
        game = HangmanGame("hello")
        assert game.get_remaining_mistakes() == 7
        game.guess_letter("z")
        assert game.get_remaining_mistakes() == 6

    def test_word_case_insensitive(self):
        game = HangmanGame("HELLO")
        game.guess_letter("l")
        assert game.get_display() == "_ _ l l _"
