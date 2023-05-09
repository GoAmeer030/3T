# Tic Tac Toe AI - Documentation

## Introduction

This document explains the Tic Tac Toe AI. Tic Tac Toe is a two-player game played on a three-by-three grid. Players take turns placing their symbols, which are usually "X" and "O", on the board. The first player to get three of their symbols in a row, column, or diagonal wins. The game ends in a tie if there are no more empty spaces on the board. This game is popular among kids and adults alike due to its simple rules, but it can be quite challenging to master.

This AI is designed to play Tic Tac Toe against a human opponent. The AI can play at three levels: beginner, intermediate, and advanced. In the beginner level, the AI plays randomly. In the intermediate level, the AI uses the minimax algorithm to play optimally. In the advanced level, the AI uses the minimax algorithm with alpha-beta pruning to play optimally.

## Requirements

This AI is written in Python 3 and requires the following libraries:

-   `pygame`
-   `numpy`

To install these libraries, you can use pip:

```
pip install pygame numpy
```

## Running the AI

To run the AI, run the `tictactoe_ai.py` file. You will be prompted to choose the level of the AI:

```
Choose the level of the AI:
1. Beginner
2. Intermediate
3. Advanced
```

Enter the number corresponding to the level you want to play against. The game board will appear on the screen, and you can start playing.

## Board Class

The `Board` class represents the game board. It has the following methods:

### `__init__(self)`

This method initializes the board. It creates a three-by-three array of zeros to represent the empty spaces on the board.

### `final_state(self, show=False)`

This method checks if the game has ended and returns the winner. If the `show` parameter is `True`, it also displays the winning row, column, or diagonal on the screen.

### `mark_sqr(self, row, col, player)`

This method marks a square on the board with the given player's symbol.

### `empty_sqr(self, row, col)`

This method returns `True` if the square at the given row and column is empty, and `False` otherwise.

### `get_empty_sqrs(self)`

This method returns a list of tuples representing the empty squares on the board.

### `isfull(self)`

This method returns `True` if the board is full, and `False` otherwise.

### `isempty(self)`

This method returns `True` if the board is empty, and `False` otherwise.

## AI Class

The `AI` class represents the AI player. It has the following methods:

### `__init__(self, level=1, player=2)`

This method initializes the AI player. The `level` parameter sets the level of the AI, and the `player` parameter sets the player number.

### `rnd(self, board)`

This method returns a random empty square on the board.

### `minimax(self, board, maximizing)`

This method implements the minimax algorithm. It returns the best move for the AI to make and its corresponding score. The `maximizing` parameter determines whether the AI is trying to maximize its score or minimize its opponent's score.

### `eval(self, main_board)`

This method evaluates the current state of the board and returns a score for the AI. The score is positive if the AI is winning, negative if the AI is losing, and zero if the game is tied.

## Conclusion

In conclusion, this code implements a Tic Tac Toe game with a simple AI opponent. The game has been developed using the Pygame library and follows a traditional design with a user interface for the players to interact with. The AI opponent has been implemented using the Minimax algorithm, and the algorithm's depth can be adjusted to vary the level of difficulty.
