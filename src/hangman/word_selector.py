import os
import re
import random
from typing import Optional

try:
    import nltk
except ImportError:
    nltk = None


WORD_LIST_FILE = "data/words.txt"
MIN_NOUNS = 2000


def ensure_nltk_data() -> None:
    if nltk is None:
        raise RuntimeError("NLTK is not installed")
    try:
        nltk.data.find("corpora/wordnet")
    except LookupError:
        nltk.download("wordnet", quiet=True)
    try:
        nltk.data.find("corpora/omw-1.4")
    except LookupError:
        nltk.download("omw-1.4", quiet=True)


def get_nouns_from_nltk() -> list[str]:
    if nltk is None:
        raise RuntimeError("NLTK is not installed")
    ensure_nltk_data()
    from nltk.corpus import wordnet

    nouns = set()
    for synset in wordnet.all_synsets(pos=wordnet.NOUN):
        for lemma in synset.lemmas():
            name = lemma.name()
            if re.match(r"^[a-z]{2,}$", name):
                nouns.add(name.lower())

    nouns_list = list(nouns)
    if len(nouns_list) < MIN_NOUNS:
        raise RuntimeError(
            f"Could not get enough nouns from NLTK: {len(nouns_list)} < {MIN_NOUNS}"
        )
    return nouns_list


def save_word_list(words: list[str], filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        for word in words:
            f.write(word + "\n")


def load_word_list(filepath: str) -> list[str]:
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]


def generate_word_list() -> list[str]:
    words = load_word_list(WORD_LIST_FILE)
    if words:
        return words
    words = get_nouns_from_nltk()
    save_word_list(words, WORD_LIST_FILE)
    return words


def filter_words_by_difficulty(words: list[str], difficulty: str) -> list[str]:
    if difficulty == "easy":
        return [w for w in words if len(w) < 6]
    elif difficulty == "medium":
        return [w for w in words if 6 <= len(w) <= 12]
    elif difficulty == "hard":
        return [w for w in words if len(w) > 12]
    return words


def select_random_word(difficulty: Optional[str] = None) -> str:
    words = generate_word_list()
    if difficulty:
        words = filter_words_by_difficulty(words, difficulty)
    if not words:
        raise ValueError(f"No words available for difficulty: {difficulty}")
    return random.choice(words)
