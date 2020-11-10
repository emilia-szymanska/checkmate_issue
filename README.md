# CHECKMATE ISSUE

## Brief description
The aim of this program is to determine, if white figures have a checkmate possibility. If not, then the black figures' possibilities are analysed.

## Assumptions
* Castles, en passants and promotions are not implemented,
* Input situation is not a checkmate or check situation, it can only become one after the program's work.

## Input
Examples of inputs can be seen in input\_dir directory. Two underscores mean an empty square, the first letter in non-empty squares denotes the figure's color (w - white, b - black), the latter a type of figure (p - pawn, k - knight, r - rook, b - bishop, q - queen, W - king).

## Running the code
To run the program after cloning this repository to your computer, run this command in a terminal:
```
./main.py < input_dir/input1.txt 
```
An example of output:
```
Move your white figure from D5 to G8
Move your white figure from D5 to A8
```

## Author
* **Emilia Szymanska**
