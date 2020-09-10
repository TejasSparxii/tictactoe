# tictactoe# **Tic Tac Toe AI**
Tic Tac Toe is a pencil paper game for two players, who takes turn marking the spaces in 3X# grid.The player who succedes in placing three of their marked places in a horizontal, vertical, or a diagonal row wins the game!!!


![](https://i.imgur.com/UzPGTaZ.gif)



---

## ***Features***
* Human as player 1
* AI as player 2
* AI plays the bestest move to minimise the chances of winning of human
* This is done by use of a recursive minimax function

## *****Descripion of User defined function used*****
Total three user defined funtion are created and they are ***main()***,***win()***,***minimax()***
* ## *main()*
It's the leading function which in collaboration with other funtion runs the program smoothly. This is the function where input is taken from a human player and then passed to the minimax funtion to make AI play the bestest move.I bet u can't win with this Ai!!!!
* ## *win()*
This is the function where checking is done weather AI or Human has won or the game is a draw. It checks weather the winner has won horizontally, vertically or diagonally.
* ## *minimax()*
This function is the AI brain of the game. it recursively calls itself and plays the whole game itself after input from human player and makes itself educated about what next human player move can be .


---

 It will recursively generate the game tree by exploring all possible moves for each board state and upon reaching a terminal state, we will assign a value of 1 for winning, -1 for losing and 0 for draw. Then based on these terminal states, for each explored turn either maximizer or minimizer will pick the most appropriate move. Doing so will propagate these outcomes all the way up to the root of the tree.![](https://i.imgur.com/pTNgsKK.png)
First, we check whether the current state is terminal and return a score if it is. If it’s not a terminal state, for all possible moves, we make the move, switch players, call minimax with the new board state, add its return value to a list of scores and undo the move.
After exhausting all possible moves, we will either return the maximum or minimum of our scores list, depending on whether we’re maximizing or minimizing.
***Gameplay with AI Vedio link:***[https://drive.google.com/file/d/1NoPzvvqYoZBcufjSB0ElOixFZaH3xvic/view?usp=sharing](https://)
