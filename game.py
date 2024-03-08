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
    _board: Board
    _num_players: int

    def __init__(self): 
        """Constructor of the Game class"""
        self._num_turns = yogi.read(int)
        self._path_price = yogi.read(int)
        self._city_price = yogi.read(int)
        self._destr_price = yogi.read(int)
        self._cash_o = yogi.read(int)
        self._max_city = yogi.read(int)
        self._board = get_board()



    def get_board(self) -> Board:
        """Returns the information of the board (size and resources)"""

        size = board.get_size(yogi.read(int), yogi.read(int))
        resources = [[read(int) for _ in range(size[1])]for _ in range(size[0])]
        return Board(size, resources)

        

    def get_players(self) -> list[Player]:
        """Returns the number of players and their colors"""

        self._num_players = read(int)
        return [get_current_player() for _ in range(_num_players)]


    def get_current_player(self) -> Player:
        """Returns the id, the cash and the color of a single player"""


    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""




    def next_turn(self) -> None: ...
