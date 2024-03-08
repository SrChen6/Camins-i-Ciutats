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
    _players = list[Player]


    def __init__(self): 
        """Constructor of the Game class"""
        if yogi.read(str) == "number_turns":
            self._num_turns = yogi.read(int)
        if yogi.read(str) == "path_price":
            self._path_price = yogi.read(int)
        if yogi.read(str) == "city_price":
            self._city_price = yogi.read(int)
        if yogi.read(str) == "destruction_price":
            self._destr_price = yogi.read(int)
        if yogi.read(str) == "initial_cash":
            self._cash_o = yogi.read(int)
        if yogi.read(str) == "max_cities":
            self._max_city = yogi.read(int)
        if yogi.read(str) == "board_size":
            self._board = self.get_board()
        if yogi.read(str) == "num_players":
            self._num_players = yogi.read(int)


    def get_board(self) -> Board:
        """Returns the information of the board (size and resources)"""
        size = [yogi.read(int) for _ in range(2)]
        resources = [[yogi.read(int) for _ in range(size[1])]for _ in range(size[0])]
        return Board(size, resources)


    def get_players(self) -> list[Player]:
        """Returns a list of all the players"""
        players: list[Player] = []
        for n in range(self._num_players):
            if yogi.read(str) == "player_color":
                players.append(Player(n, self._cash_o, yogi.read(str)))
            
        for n in range(self._num_players):
        # To add a path, use add_path() in board
            ...

    def get_current_player(self) -> Player:
        """Returns the id, the cash and the color of a single player"""



    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""


    def next_turn(self) -> None: ...
