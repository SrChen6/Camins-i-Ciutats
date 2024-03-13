import places
from player import Player
from board import Board
from yogi import read


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
        if read(str) == "number_turns":  self._num_turns = read(int)

        if read(str) == "path_price": self._path_price = read(int)

        if read(str) == "city_price": self._city_price = read(int)

        if read(str) == "destruction_price": self._destr_price = read(int)

        if read(str) == "initial_cash": cash_o = read(int)

        if read(str) == "max_cities": self._max_city = read(int)

        if read(str) == "board_size":
            size = [read(int) for _ in range(2)]
            resources = [[read(int) for _ in range(size[1])]for _ in range(size[0])]
            self._board = Board(size, resources, [], [])

        if read(str) == "num_players": self._num_players = read(int)
        
        self._players = []
        for n in range(self._num_players): # color
            if read(str) == "player_color":
                self._players.append(Player(n, cash_o, read(str)))
        self._players = self.get_players()

        for player in self._players: #first city
            if read(str) == "player_city":
                self._board._citites.append([player, [read(int),read(int)]])

        self._current_turn = 0


    def get_board(self) -> Board:
        """Returns the information of the board (size and resources)"""
        return self._board


    def get_players(self) -> list[Player]:
        """Returns a list of all the players"""
        return self._players


    def get_current_player(self) -> Player:
        """Returns the id, the cash and the color of a single player"""
        return self._players[self._current_turn%self._num_players + 1]


    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""
        return self._num_turns == self._current_turn


    def next_turn(self) -> None:
        """takes input of the next turn"""
        self._current_turn += 1
        action = read(str)
        player = self.get_current_player()
        valid_action = True
        if read(int) == player._id: #Corregir los casos de accion invalida
            coord = tuple[read(int), read(int)]
            match action:
                case "build_path":
                    coord2 = tuple[read(int), read(int)]
                    if Board._legal_path(tuple[coord, coord2]):
                        self._board.add_path(player, tuple[coord, coord2])
                        player.update_cash(-self._path_price)
                    else:
                        print("You are not allowed to build a path here. Turn cancelled.") #esta bé que escrigui 3 vegades el invalid input?
                case "build_city":
                    if Board._legal_city(coord):
                        self._board.add_city(player, tuple[read(int), read(int)])
                        player.update_cash(-self._city_price)
                    else:
                        print("You are not allowed to build a city here. Turn cancelled.")
                case "destroy_city":
                    if Board._legal_destruction(coord):
                        self._board.remove_city(tuple[read(int), read(int)])
                        player.update_cash(-self._destr_price)
                    else:
                        print("There is no city to destroy here. Turn cancelled.")
        else:
            print("Wrong player, turn cancelled")

