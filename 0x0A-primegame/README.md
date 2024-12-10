# Prime Game

This project implements the **Prime Game** where two players, Maria and Ben, take turns removing prime numbers and their multiples from a set of consecutive integers. The game ends when no prime numbers are left to remove, and the player who cannot make a move loses. Maria always goes first and both players play optimally.

## Requirements

- Python 3.x
- No external libraries (only built-in Python libraries used)

## Function

The `isWinner(x, nums)` function determines the winner of the game for multiple rounds:

- `x`: Number of rounds to play
- `nums`: A list of integers, each representing the upper limit of the set in a round.

The function returns the player with the most wins, or `None` if there is a tie.

## Example

```python
isWinner(3, [4, 5, 1])
# Output: "Ben"
