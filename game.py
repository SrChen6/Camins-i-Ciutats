import places
from player import Player
from board import Board
import yogi


class Game:
    _num_turns: int
    _path_price: int
    _city_price: int
    _destr_price: int
    _cash_o: int
    _max_city: int

    def __init__(self): 
        """Constructor of the Game class"""
        self._num_turns = read(int)
        self._path_price = read(int)
        self._city_price = read(int)
        self._destr_price = read(int)
        self._cash_o = read(int)
        self._max_city = read(int)


    def get_board(self) -> Board:
        """Returns the information of the board (size and resources)"""
        
        

    def get_players(self) -> list[Player]:
        """Returns the number of players and their colors"""

    def get_current_player(self) -> Player:
        """Returns the id, the cash and the color of a single player"""

    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""


    def next_turn(self) -> None: ...
