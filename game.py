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
    _players: list[Player]

    _current_turn: int


    def __init__(self): 
        """Constructor of the Game class"""
        if read(str) == "number_turns":  self._num_turns = read(int)
        if self._num_turns < 1:
            raise ValueError('The number of turns must be geater than 0')
        
        if read(str) == "path_price": self._path_price = read(int)
        if self._path_price < 0:
            raise ValueError('The price to build a path must be greater or equal to 0')

        if read(str) == "city_price": self._city_price = read(int)
        if self._city_price < 0:
            raise ValueError('The price to build a city must be greater or equal to 0')

        if read(str) == "destruction_price": self._destr_price = read(int)

        if read(str) == "initial_cash": cash_o = read(int)
        else:
            cash_o = 0
        if cash_o < 0:
            raise ValueError('The initial cash must be greater or equal to 0')

        if read(str) == "max_cities": self._max_city = read(int)
        if self._path_price < 1:
            raise ValueError('The price of the paths must be greater or equal to 0')


        if read(str) == "board_size":
            size = places.BoxSize((read(int), read(int)))
        else:
            size = places.BoxSize((1,1))          
        if  size[0] < 1 or size[1] < 1:
            raise ValueError('The size of the board must be 1x1 or greater')
        else:
            resources = [[read(int) for _ in range(size[1])]for _ in range(size[0])]
            self._board = Board(size, resources, [], [])


        if read(str) == "num_players": self._num_players = read(int)
        if self._num_players == 1:
            print("No friends?")
        elif self._num_players < 1:
            raise ValueError('The number of players must be one or greater')
        
        self._players = []
        for n in range(self._num_players): # color
            if read(str) == "player_color":
                self._players.append(Player(n + 1, cash_o, read(str)))
        self._players = self.get_players()

        for player in self._players: #first city
            if read(str) == "player_city":
                coord = places.Coord((read(int),read(int)))
                if not self._in_board(coord):
                    raise ValueError('The city must be in the board')
                self._board.get_cities().append((player, coord))
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
        print(self._num_turns, self._current_turn)
        return self._num_turns == self._current_turn

    def _path_dist_1(self, path: places.Path) -> bool:
        """Given a path, returns if the path has lengh 1"""
        x1, y1 = path[0][0], path[0][1]
        x2, y2 = path[1][0], path[1][1]
        return abs((x1 - x2) + (y1 - y2)) == 1

    def _connected_path(self, path: places.Path) -> bool:
        """Given a path, returns if the path is connected to one of the 
        current player's path"""
        for player_path in self._board.get_paths():
            print(player_path[1],path)
            if path[0] in player_path[1] or path[1] in player_path[1]:
                return player_path[0] == self.get_current_player()
        return False

    def _connected_city_path(self, path: places.Path) -> bool:
        """Given a path, returns if the path is connected to a city of the same player"""
        for player_city in self._board.get_cities():
            if path[0] in player_city or path[1] in player_city:
                return player_city[0] == self.get_current_player()
        return False

    def _legal_path(self, path: places.Path) -> bool:
        """Condicions path
        In the board
        lenght = 1
        Not occupied
        Path/city of the same player on one of the ends
        None of the ends has a path of another player
        """
        if not (self._in_board(path[0]) and self._in_board(path[1])):
            return False
        if not self._path_dist_1(path):
            return False
        for player_path in self._board.get_paths(): #checks if path occupied
            coord1, coord2 = player_path[1][0], player_path[1][1]
            if (coord1, coord2) == path or (coord2, coord1) == path:
                return False
        if not self._connected_city_path(path) and not self._connected_path(path):
            return False
        return True

    def _legal_city(self, coord: places.Coord) -> bool:
        """Conditions city
        In board
        Not occupied
        Next to a path
        """
        if self.get_current_player().get_cash() < self._city_price:
            return False
        if not self._in_board(coord):
            return False
        for player_city in self._board.get_cities(): #Checks if coord occupied
            if coord == player_city[1]:
                return False
        for player_path in self._board.get_paths(): #Checks if connected to a path
            if coord == player_path[1][0] or coord == player_path[1][1]:
                return True
        return False

    def _legal_destruction(self, coord: places.Coord) -> bool:
        """Conditions destruction
        Occupied by the same player"""
        if self.get_current_player().get_cash() < self._destr_price:
            return False
        for player_city in self._board.get_cities():
            if coord == player_city[1] and player_city[0] == self.get_current_player():
                return True
        return False

    def _resource_update(self, player: Player) -> None:
        """Given a player, subtracts the resources around all his cities"""
        for player_city in self._board.get_cities():
            if player_city[0] == player:
                dr = player_city[1]
                dl = places.Coord((dr[0], dr[1] - 1))#check tuple changing
                ur = places.Coord((dr[0] - 1, dr[1]))
                ul = places.Coord((dr[0] - 1, dr[1] - 1))
                if self._in_board(dr) and dr[0] < self._board.get_size()[0] and dr[1] < self._board.get_size()[1]:
                    self._board.substract_resource(dr)
                if self._in_board(dl) and dl[0] < self._board.get_size()[0]:
                    self._board.substract_resource(dl)
                if self._in_board(ur) and ur[1] < self._board.get_size()[1]:
                    self._board.substract_resource(ur)
                if self._in_board(ul):
                    self._board.substract_resource(ul)


    def _in_board(self, coord: places.Coord) -> bool: 
        """Given a coordenate, returns if it's in the board"""
        if coord[1] >= 0 and coord[1] <= self._board.get_size()[1]:
            in_x = True
        else: in_x = False
        if coord[0] >= 0 and coord[0] <= self._board.get_size()[0]:
            in_y = True
        else: in_y = False
        return in_x and in_y


    def next_turn(self) -> None:
        """takes input of the next turn"""
        if self.is_game_over():
            print("GAME OVER") #Print the stats when the game ends\\TODO
        else:
            player = self.get_current_player()
            self._resource_update(player)
            action = read(str)
            input_id = read(int)
            print(f"Player {player.get_id()}: you have {player.get_cash()} cash")
            match action:
                case "build_path":
                    coord1 = (read(int), read(int))
                    coord2 = (read(int), read(int))
                    if self._legal_path(places.Path((coord1, coord2))):
                        self._board.add_path(player, (coord1, coord2))
                        player.update_cash(-self._path_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: You are not allowed to build a path on {coord1, coord2}. Turn cancelled.")
                case "build_city":
                    coord = (read(int), read(int))
                    if self._legal_city(coord):
                        self._board.add_city(player, coord)
                        player.update_cash(-self._city_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: You are not allowed to build a city on {coord}. Turn cancelled.")
                case "destroy_city":
                    coord = (read(int), read(int))
                    if self._legal_destruction(coord):
                        self._board.remove_city(coord)
                        player.update_cash(-self._destr_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: There is no city to destroy on {coord}. Turn cancelled.")
                case _:
                    pass
            if input_id != player.get_id():
                print(f"Player {player.get_id()}: you entered player {input_id}'s id. Your turn will be skipped")
            self._current_turn += 1

