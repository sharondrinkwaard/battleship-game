# The paramount battleships game
The paramount battleships game is a Python terminal game that runs on Heroku.
Battleship is a strategy type guessing game. It is known worldwide as a pencil and paper game which dates from World War I. And played on ruled grids where each player has warships, which are hidden from the other player.


## How to play
---
The ultimate goal is to destroy all the ships of the other player.
There are a few variations of this game. 
This one has one game board where the computer places 4 ships at a random location.
The player has to fill in 2 coordinates between 1 and 5 and guess where the ships are located. 

An 'M' is printed on the board if the player misses.
An '$' is printed on the board when the player sunk a ship.

When all ships sank, the player wins.
When the player ran out of bullets, the player loses. 
## Features
---
## Features left to implement
---
- Press an exit button to be able to stop while playing the game.
- Play against the computer, so computer has his own board (2 game boards in total) instead of 1 like right now.
- To keep track of the amount of bullets while playing the game so the player knows how many bullets he has left.
- To make sure the same coordinates cannot be placed twice.
- To make sure no ships can be placed twice on the same coordinations
- I want the user to place the ships themselves and choose different sizes of the ships.
- I want to create several difficulty levels by expanding the game board.
## Data Model Design
---
## Libraries
---
- random
    - The random library was imported to access the built-in method of generating a random number selection using the randint() method. 
- os
    - The os library was imported to create a function to utilise the os.system to clear the terminal.
- sys
    - The sys library was imported to create a function to restart my program so that previous data would not be used when restarting the game.
## Testing
---
## Issues And Bugs Found
---
When writing this game, I found several issues on the way that needed to be solved.
- Hiding the ships
    - When placing the ships ('X') on the game board, the ships were shown to the player. So he knew exactly where the ships were placed. I solved this by creating another game board so I have two boards in total. One where the ships are being placed on and one where the player's moves are being tracked. 
    Now the player is not able to see the hidden ships as the other board is being displayed. 

- Catching the input of the player correctly
    - When the given coordinates were bigger than 5, an error occurred saying the list index is out of range and this would break the game. 
    I solved this by writing the code below:

    ![Input bigger than 5](./assets/images/input_bigger_than_5.png)

    - When the given coordinates were smaller than 1, it was replacing the headings by a ship, or missed shot. I used the index 0 for the headings so the player could use the coordinates from 1 and up. This to prevent confusion by the player who might not be familiar with Python indexing.
    I solved this by writing the code below:

    ![Input smaller than 1](./assets/images/input_smaller_than_1.png)

    - When only one coordinate was given instead of two, and when a letter was given instead of a number, the game would break because of an error.
    I solved this by using an try except statement within a while loop. See code below:

    ![Catch invalid input](./assets/images/catch_invalid_input.png)

    - The restart function would restart the game but would not reset the game boards. So the moves of the previous game were displayed.
    I created another function to clear the screen and restart my python module so that the game board is empty when restarting the game.

    ![Reset function](./assets/images/reset_function.png)

### Unsolved bugs
---
- Sometimes the ship placement function places only 3 ships instead of 4. 
This function choses a random integer between 1 and 4 within a for loop of range 4. It should place 4 ships at a random location each time the function is called. And it is placing the ships correctly most of the time. Just so now and then it places only 3 ships because 2 coordinates are the exact same. What happens is the functions places 2 ships on the same location. 
I want to solve this by using an extra if statement or an try except statement. So far I haven't had time yet and will leave this for features left to implement in the future. 
    
## Validator Testing
---
- PEP8 SCREENSHOT
## Deployment
---
## Credits
---



## notes
from random import randint -- I saw this on a comment on a Github repo and started googling it to learn more about it. https://docs.python.org/3/library/random.html

= Trying to hide the ships: there probably is an better way to do this with less code
Tutor support was busy and I was running out of time so I had to be a bit creative
I decided to create anoter game board so that I have 2.
One for the player moves and one for the ships
Every time I need to display the board without ships, I display the board of the player moves.
Everytime The user gets it right and hits a ship, I place an $ on both of the boards so both boards keep track of what ships are being hit, while keeping the other ships hidden from the player.



## testing
- game input:
- tested when a user puts in a 0 (which is out of range in this game), that it won't break the game but that it is catched properly. 
- Same for when the player puts in a value above 5, I am making sure this won't break the game but continues after giving the player a 2nd try to give valid input. 
- When no input is given, the try except code catches the error
- When a letter is given instead of a number, the try except catches the error
- when input is the same location as an 'x, a ship ($) is placed on the board so the player can see 
- When the player misses a battleship, an 'M' is printed on the board

## links
https://www.geeksforgeeks.org/reloading-modules-python/
https://www.codegrepper.com/code-examples/python/restart+python+script+automatically - helped me to understand the sys library
https://www.w3schools.com/python/python_try_except.asp - helped me learn about try and except statements
https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f - reminded me of how to write in markdown
https://en.wikipedia.org/wiki/Battleship_(game)#:~:text=The%20game%20of%20Battleship%20is%20thought%20to%20have,played%20by%20Russian%20officers%20before%20World%20War%20I - To learn a bit more about the battleship game which I was not familiar with

