# wordle_solver
Solving wordle puzzles

# How to Run
In each iteration, the computer is going to guess and the other players answer with if is each character
* in the word?
* in the right place?

# Sample Run
In the run below
* Computer Guesses "audio", players responds with 10200
* Computer Guesses "madly", players responds with 02222
* Computer Guesses "badly", players responds with BINGO!

```
$ python play_game.py
Value for this guess: audio (0: no, 1: wrong_place, 2: perfect)
10200
Value for this guess: madly
 (0: no, 1: wrong_place, 2: perfect)
02222
new_candidates: ['badly\n', 'sadly\n']
Value for this guess: badly
 (0: no, 1: wrong_place, 2: perfect)
```
