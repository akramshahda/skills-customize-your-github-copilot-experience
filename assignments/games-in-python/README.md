# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Implement Word Selection

#### Description
Create a system to randomly select a secret word from a predefined list for the player to guess.

#### Requirements
Completed program should:

- Define a list of at least 10 words for the game
- Use Python's `random` module to select a word
- Hide the selected word from the player during gameplay

### 🛠️ Build Game Logic

#### Description
Implement the core game mechanics including letter guessing, progress tracking, and game state management.

#### Requirements
Completed program should:

- Accept single letter guesses from the player
- Display current progress using underscores for unguessed letters (e.g., `_ _ _ _`)
- Track the number of incorrect guesses remaining
- Validate input to prevent duplicate guesses or invalid entries
- Continue gameplay until the word is guessed or attempts are exhausted

### 🛠️ Display Game Results

#### Description
Provide clear feedback to the player about the game outcome and their performance.

#### Requirements
Completed program should:

- Display a win message when the word is successfully guessed
- Display a lose message and reveal the word when attempts run out
- Show the final number of attempts used
