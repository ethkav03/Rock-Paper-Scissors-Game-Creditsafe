# Rock Paper, Scissors Game - Creditsafe
A basic implementation of a game of Rock, Paper, Scissors

## Task Description
Implement a console-based Rock, Paper, Scissors game where the user plays against the computer. Additionally, the computer should keep track of the number of wins after a certain number of games.

## Rules
- The user selects Rock, Paper, or Scissors.
- The computer randomly selects Rock, Paper, or Scissors.
- The winner is determined based on the following rules:
 - Rock crushes Scissors (Rock wins against Scissors)
 - Scissors cuts Paper (Scissors wins against Paper)
 - Paper covers Rock (Paper wins against Rock)
 - If both the user and the computer choose the same, it's a tie.

## How To Play
When the game begins it will play N number of rounds based on what number was provided on invocation. The user will then pick a number between 0 and 2 (inclusive) each round to pick a number.
|Number|Hand|
|---|---|
|0|Rock|
|1|Paper|
|2|Scissors|

After all the rounds are played the winner is determined.

## Sample Invocation
**$** python3 rock_paper_scissors.py 5