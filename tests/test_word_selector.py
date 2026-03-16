import pytest
from unittest.mock import patch
from hangman.word_selector import (
    filter_words_by_difficulty,
    load_word_list,
    save_word_list,
    generate_word_list,
    select_random_word,
    WORD_LIST_FILE,
)


class TestFilterWordsByDifficulty:
    def test_easy(self):
        words = ["cat", "elephant", "dog", "giraffe", "a"]
        result = filter_words_by_difficulty(words, "easy")
        assert result == ["cat", "dog", "a"]

    def test_medium(self):
        words = ["cat", "elephant", "dog", "giraffe", "hello"]
        result = filter_words_by_difficulty(words, "medium")
        assert result == ["elephant", "giraffe"]

    def test_hard(self):
        words = ["cat", "elephant", "dog", "internationalization"]
        result = filter_words_by_difficulty(words, "hard")
        assert result == ["internationalization"]

    def test_invalid_difficulty(self):
        words = ["cat", "dog"]
        result = filter_words_by_difficulty(words, "invalid")
        assert result == ["cat", "dog"]


class TestSaveLoadWordList:
    def test_save_and_load(self, tmp_path):
        test_file = tmp_path / "test_words.txt"
        words = ["cat", "dog", "bird"]
        save_word_list(words, str(test_file))
        loaded = load_word_list(str(test_file))
        assert loaded == ["cat", "dog", "bird"]

    def test_load_nonexistent(self, tmp_path):
        test_file = tmp_path / "nonexistent.txt"
        loaded = load_word_list(str(test_file))
        assert loaded == []


class TestGenerateWordList:
    @patch("hangman.word_selector.load_word_list")
    def test_returns_existing_list(self, mock_load):
        mock_load.return_value = ["cat", "dog"]
        result = generate_word_list()
        assert result == ["cat", "dog"]
        mock_load.assert_called_once_with(WORD_LIST_FILE)

    @patch("hangman.word_selector.get_nouns_from_nltk")
    @patch("hangman.word_selector.load_word_list")
    def test_generates_from_nltk(self, mock_load, mock_nltk):
        mock_load.return_value = []
        mock_nltk.return_value = ["cat", "dog", "bird"] * 700
        result = generate_word_list()
        assert len(result) >= 2000
        mock_nltk.assert_called_once()


class TestSelectRandomWord:
    @patch("hangman.word_selector.generate_word_list")
    def test_no_difficulty(self, mock_generate):
        mock_generate.return_value = ["cat", "dog", "elephant"]
        result = select_random_word()
        assert result in ["cat", "dog", "elephant"]

    @patch("hangman.word_selector.generate_word_list")
    def test_with_difficulty(self, mock_generate):
        mock_generate.return_value = ["cat", "elephant", "internationalization"]
        result = select_random_word("easy")
        assert result == "cat"
        result = select_random_word("medium")
        assert result == "elephant"
        result = select_random_word("hard")
        assert result == "internationalization"

    @patch("hangman.word_selector.generate_word_list")
    def test_no_words_for_difficulty(self, mock_generate):
        mock_generate.return_value = ["cat"]
        with pytest.raises(ValueError, match="No words available"):
            select_random_word("hard")
