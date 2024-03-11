import places
from player import Player
from board import Board
import yogi


class Game:
    _num_turns: int
    _path_price: int
    _city_price: int
    _destr_price: int
    _board: Board
    _max_city: int
    _players = list[Player]

    _current_turn: int



    def __init__(self): 
        """Constructor of the Game class"""
        if yogi.read(str) == "number_turns": # algernativa: asser
            self._num_turns = yogi.read(int)
        if yogi.read(str) == "path_price":
            self._path_price = yogi.read(int)
        if yogi.read(str) == "city_price":
            self._city_price = yogi.read(int)
        if yogi.read(str) == "destruction_price":
            self._destr_price = yogi.read(int)
        if yogi.read(str) == "initial_cash":
            cash_o = yogi.read(int)
        if yogi.read(str) == "max_cities":
            self._max_city = yogi.read(int)
        if yogi.read(str) == "board_size":
            size = [yogi.read(int) for _ in range(2)]
            resources = [[yogi.read(int) for _ in range(size[1])]for _ in range(size[0])]
            self._board = Board(size, resources, [], [])
            print(self._board._resources)
        if yogi.read(str) == "num_players":
            self._num_players = yogi.read(int)
        self._players = []
        for n in range(self._num_players): # color
            if yogi.read(str) == "player_color":
                self._players.append(Player(n, cash_o, yogi.read(str)))
        self._players = self.get_players()
        for player in self._players: #first city
            if yogi.read(str) == "player_city":
                self._board._citites.append([player, [yogi.read(int),yogi.read(int)]])


    def get_board(self) -> Board: # No és la informació inicial, símplement retorna la info
        # tota la lectura inicial es fa dins de init
        """Returns the information of the board (size and resources)"""
        return self._board


    def get_players(self) -> list[Player]:
        """Returns a list of all the players"""
        return self._players


    def get_current_player(self) -> Player:
        """Returns the id, the cash and the color of a single player"""
        #Not sure what it does, input is all colors followed by all cities
        return self._players[self._current_turn%self._num_players + 1]


    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""
        return self._num_turns == self._current_turn


    def next_turn(self) -> None:
        """takes input of the next turn"""
        ...
