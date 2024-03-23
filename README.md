# Camins i ciutats

## Description

This program is a game slighly similar to Catan™.

### Rules

- Players: the game can be played by any positive number of players

- Board, nodes and edges: the board is composed of a rectangular grid of cells. Each cell has a certain number of initial resources. Every cell has four edges where paths can be built (even the edges at the end of the board). The intersection of edges are nodes, where cities can be built.

- Game start: Every player starts with a city built at the board and an initial amount of cash.

- Turns: The game develops by turns. At each turn the current player makes the following tasks:
    1. Resource gathering: for each cell next to each of the player's city, the player gathers a unit of resources that is transformed into a coin for his cash, subtracting the resources from the cells. The cells can no longer give resources. If a player has more than a city next to a cell, he wins as many coins as cities (as long as there are resources to gather).

    2. Action: the player can choose between three actions:
        - Build a path: the player can build a path on an edge if the following three conditions are given:
            - The edge is not occupied by another path
            - One of the ends of the edge has a city or a path of the same player
            - None of the ends of the edge has a path of another player (altough it can be a city of another player).

        - Build a city: The player can build a city on any node adjacent to his paths where there are no cities. The maximum number of cities is limited for every player.

        - Destroy a city: The player can destroy one of his own cities.

    All the actions have a cost and it will be subtracted from their cash.

    If the player does not have enough cash or tries to execute an illegal move, his turn will be skipped withought executing the action.

- Goal: The player with the most cash when the number of turns reaches the maximum wins.




## Requirements

To execute this programm it is necessary to have installed the programm `Pygame`. To install it, please check this [link](https://www.pygame.org/wiki/GettingStarted).

## Usage

The game requires a set of game conditions as inputs before beginning the game itself:
- `number_turns x`: an integer > 0.
- `path_price x`: an integer greater or equal to 0.
- `city_price x`: an integer greater or equal to 0.
- `destruction_price x`: Any integer (if negative, cash will be given to the player when a city is destroyed)
- `initial_cash x`: an integer greater or equal to 0.
- `max_cities x`: an integer greater or equal to 0.
- `board_size x y`: two integers, both greater than 0.
- The initial resources on the board (as many as the board size).
- `num_players x`: an integer greater or equal to 1.
- `player_color a`: the desired colors for every player, as many inputs as the number of players.
- `player_city x y`: two integers that represent the coordenates of the first city of the player. As many inputs as the number of players.

The board should be visible by now. The following inputs will be the actions of every player.
- `build_path p x1 y1 x2 y2` where `p` is the player's id and `x,y` are two coordenates that represent the place where to build a path.
- `build_city p x y` where `p`is the player's id and `x,y` is the coordenate where a city wants to be built.
- `destroy_city p x y` where `p`is the player's id and `x,y` is the coordenate where a city wants to be destroyed.

An input example would look like this:

```text
number_turns 5
path_price 5
city_price 10
destruction_price 15
initial_cash 100
max_cities 5
board_size 6 8
5 8 9 2 5 4 3 6
1 4 2 5 7 7 9 2
5 8 9 2 5 4 3 6
1 4 2 5 7 7 9 2
5 8 9 2 5 4 3 6
1 4 2 5 7 7 9 2
num_players 3
player_color darkred
player_color darkgreen
player_color purple
player_city 5 6
player_city 4 1
player_city 2 3

build_path 1 5 6 5 7
build_path 2 4 1 4 2
build_path 3 2 3 3 3
build_city 1 5 7
destroy_city 2 4 1
```
## Design decisions

### player.py

- Cash:

    When a game begins, the first thing that the player does is recollect the resources. Then, with the initial cash + the resources gathered, the player executes an action.

### game.py

- Constructor:

    Although the `if(condition)` are not necessary, they are a good indicator of what the input is reading. If the inputs are invalid, the program will raise a ValueError, stoping the execution of the program completely.

- Game over:

    When the game is over (the maximum number of turns was reached), the program will continue executing, but a message of `GAME OVER` will be printed on Terminal, followed by the winner. It won't read any inputs or execute further instructions fron a .inp file.

    To finish the execution, stop the program from Terminal or close the game window.

- Turn:

    If a player enters another player's id, it will be considered that the first player tried to impersonate another player, so his turn will be skipped.

- Path legallity:

    A city will always be on an end of 