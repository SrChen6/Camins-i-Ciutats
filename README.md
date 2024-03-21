# Camins i ciutats

## Description

This program is a game slighly similar to Catan™.

### Rules

At the beginning of a game, all the players will have a city on the board. Every turn, the player first collects the resources next to his cities and then decides between three actions: build a city, destroy a city or build a path.

The player with the most cash at the end of all the rounds wins the game.

For more information consult [this repository](https://github.com/jordi-petit/ap2-camins-i-ciutats-2024).


## Requirements

To execute this programm it is necessary to have installed the programm `Pygame`. To install it, please check this [link](https://www.pygame.org/wiki/GettingStarted).

## Usage

The game requires a set of game conditions as inputs before beginning the game itself:
- `number_turns x`: an integer greater than 0.
- `path_price x`: an integer greater or equal to 0.
- `city_price x`: an integer greater or equal to 0.
- `destruction_price x`: an integer greater or equal to 0.
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

### board.py

### game.py

### places.py
    
