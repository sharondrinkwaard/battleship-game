![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome sharondrinkwaard,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!



## notes
from random import randint -- I saw this on a comment on a Github repo and started googling it to learn more about it. https://docs.python.org/3/library/random.html

= Trying to hide the ships: there probably is an better way to do this with less code
Tutor support was busy and I was running out of time so I had to be a bit creative
I decided to create anoter game board so that I have 2.
One for the player moves and one for the ships
Every time I need to display the board without ships, I display the board of the player moves.
Everytime The user gets it right and hits a ship, I place an $ on both of the boards so both boards keep track of what ships are being hit, while keeping the other ships hidden from the player.

## unsolved bugs
- Sometimes the ship placement function places only three ships instead of 4. I haven't discovered why it's doing this yet. As it choses a random int between 1 and 4 within a for loop of range 4, it should place 4 ships at a random location each time the function is called. 
Maybe it prints 2 x's on the same location

- input of the player is not catched yet. When input is bigger than 5 an error occurs and quits the game. FIXED

- When player does not give 2 coordinates, the game breaks. 


## testing
- game input:
- tested when a user puts in a 0 (which is out of range in this game), that it won't break the game but that it is catched properly. 
- Same for when the player puts in a value above 5, I am making sure this won't break the game but continues after giving the player a 2nd try to give valid input. 
- 

## Things to implement
- To stop during the game
- Play against the computer, so computer has his own board (2 game boards in total)