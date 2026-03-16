# Python Hangman CLI Game

This is a playground directory to attempt to generate a simple project using `Ollama` and `OpenCode

## Specifications

The hangman game has the following requirements:

### Functional
- Allows the user to set the difficulty via three options: Easy, Medium, and Hard
  - Easy will have words less than 6 characters long.
  - Medium will have words 6-12 characters long.
  - Hard will have words over 12 characters long.
- Selects a word randomly from a text file containing words, use regular expressions to filter the word list.
  - If the word list is missing, use `NLTK` to generate a 2000-noun word list and save it locally.
- The game will show the initial guess as a string composed of underscores, as long as the chosen word.
- If the user inputs a single character, check if the character exists in the word to guess, if so, place it in the game output replacing the corresponding underscores. If not, show the character in another line stating used characters.
- The player is allowed to make 7 mistakes before losing.
- The user will win if they guess all the correct characters in the word.
- The user will lose if they miss to guess the word 7 times.
- Allow the user to guess the complete word at any given time; if successful, they win, otherwise they lose.
- Allow the user to play again if desired, confirm that they want to keep using the initial settings or they want to modify them.


### Stack
- Use `uv` to manage the virtual environment and dependencies where this project will be developed.
- Use `Python` as programming language.
- Use `NLTK` to generate the word list.
- Use `ruff` for code formatting and linting following `PEP8` practices.
- Use `pytest` for unit testing.
