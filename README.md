# Tic-Tac-Toe
#### Video Demo:  <https://youtu.be/JjnbPlZguTM>
#### Description:
Sample Tic-Tac-Toe game with tabulate function visuals. Should be 2 players and wins player if one of column or row or diagonal will filled with player's symbols (X or O)

### Questions / Answer
1. How may players shoould play? only 2 players
2. Do we need payers names? Yes, ignore alphabetical case and transform in upper case
3. How may rounds payers should play? Request from user 1,2...max 10
4. Count score if rounds are more then 1? Yes
5. What use for visualisation of the game? Tabulate form
6. Grid of the game? only 9x9
7. What to use for play as input? Coordinate system like A1 B3 and other

### Rules of the game
- Add first player name. if you will leave it as empty code will ask again till you add the name
- Add second player name. if you will leave it as empty code will ask again till you add the name
- Add round number. need to add ineger from 1 to 10
- The game will give you symbols X and O, for player 1 is symbol X and for second O
- Game starts first player
- Each of player should add cordinates like A1 or C3
- Winns who firs will fill one row or column or diagonal with player's symbol(x or o)
- If round number is more then 1 starts next round of the game
- After each round you will see scores of players.

#### Used libraries
- tabulate - for visualisation of the game
- numpy - for getting unique values from arrayes

#### User Requested variables
player1 - Request First player name
player2 - Request Second player name
rounds - Request number of rounds
symbol1 - Already declared in code as "X"
symbol2 - Already declared in code as "O"


## Pseudo code
### part collecting data for start the game
#### Functuin to get players names and symbols
player1 = input("Player1").strip().upper()
player2 = input("Player2").strip().upper()
check both players and ask again if one of them is empty or both names are the same
if everithing is OK declare symbol "X" for player 1 and "O" for player 2
return player1, player2, symbol1, symbol2

#### Function to get round numbers
round = int(input("rounds: "))
exclude extra spaces and ask again if rounds is empty or incorrect value (not in range 1 to 10)

#### Function to generate any possible winn combination
Run on the table anc collect combinations if 3 of items in the combinations are the same and then return unique symbol X or O

### Function for start sicle of the game
initiate empty table data

#### Function generate all possible input values for the game
combinate all values from A,B,C and 1,2,3


