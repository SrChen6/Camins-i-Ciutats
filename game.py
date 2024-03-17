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
        #afegir condicions
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
        """Returns the player of this turn"""
        return self._players[(self._current_turn%self._num_players)]


    def is_game_over(self) -> bool: 
        """Returns if the game ends this round"""
        return self._num_turns == self._current_turn

    def _legal_path(self, path: places.Path) -> bool:
        """Condicions path
        In the board
        lenght = 1
        Not occupied
        Path/city of the same player on one of the ends
        None of the ends has a path of another player
        """
        return True

    def _legal_city(self, coord: places.Coord) -> bool:
        """Conditions city
        In board
        Next to a path
        Not occupied
        """
        return True

    def _legal_destruction(self, coord: places.Coord) -> bool:
        """Conditions destruction
        Occupied by the same player"""
        return True

    def _resource_update(self, player: Player) -> None:
        """Given a player, subtracts the resources from all its cities"""
        player_citites_coord = [coord for coord in Board._citites[1] if Board._citites[0] == player]
        print(player_citites_coord)
        for coord in player_citites_coord:
            #Check if in board
            Board.substract_resource(coord)
            Board.substract_resource(places.Coord(coord[0] - 1, coord[1]))
            Board.substract_resource(places.Coord(coord[0], coord[1] - 1))
            Board.substract_resource(places.Coord(coord[0] - 1, coord[1] - 1))

    def _in_board(self, coord: places.Coord) -> bool: #needs to be tested
        """Given a coordenate, returns if it's in the board"""
        if coord[0] >= 0 and coord[0] <= self._board.get_size()[0]:
            in_x = True
        if coord[1] >= 0 and coord[1] <= self._board.get_size()[1]:
            in_y = True
        return in_x and in_y


    def next_turn(self) -> None:
        """takes input of the next turn"""

        action = read(str)
        player = self.get_current_player()
        self._resource_update(player)
        if read(int) == player._id + 1:
            match action:
                case "build_path":
                    coord1 = (read(int), read(int))
                    coord2 = (read(int), read(int))
                    if self._legal_path(places.Path((coord1, coord2))):
                        self._board.add_path(player, (coord1, coord2))
                        player.update_cash(-self._path_price)
                    else:
                        print("You are not allowed to build a path here. Turn cancelled.")
                case "build_city":
                    coord = (read(int), read(int))
                    if self._legal_city(coord):
                        self._board.add_city(player, coord)
                        player.update_cash(-self._city_price)
                    else:
                        print("You are not allowed to build a city here. Turn cancelled.")
                case "destroy_city":
                    coord = (read(int), read(int))
                    if self._legal_destruction(coord):
                        self._board.remove_city(coord)
                        player.update_cash(-self._destr_price)
                    else:
                        print("There is no city to destroy here. Turn cancelled.")
        else:
            print("Wrong player, turn cancelled")
        self._current_turn += 1

