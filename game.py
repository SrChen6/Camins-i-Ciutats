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
            cash_o = 0 #To avoid errors from not initializing
        if cash_o < 0:
            raise ValueError('The initial cash must be greater or equal to 0')

        if read(str) == "max_cities": self._max_city = read(int)
        if self._path_price < 0:
            raise ValueError('The price of the paths must be greater or equal to 0')


        if read(str) == "board_size":
            size = places.BoxSize((read(int), read(int)))
        else:
            size = places.BoxSize((1,1)) #To avoid errors from not initializing
        if  size[0] < 1 or size[1] < 1:
            raise ValueError('The size of the board must be 1x1 or greater')
        else: #read the resources and initialize board
            resources = [[read(int) for _ in range(size[1])]for _ in range(size[0])]
            self._board = Board(size, resources, [], [])

        if read(str) == "num_players": self._num_players = read(int)
        if self._num_players == 1:
            print("No friends?") #just a little easter egg
        elif self._num_players < 1:
            raise ValueError('The number of players must be one or greater')
        
        self._players = []
        for n in range(self._num_players): # color input and initialize players
            if read(str) == "player_color":
                self._players.append(Player(n + 1, cash_o, read(str)))

        for player in self.get_players(): #first cities
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
        return self._num_turns == self._current_turn

    def _path_dist_1(self, path: places.Path) -> bool:
        """Given a path, returns if the path has lengh 1"""
        x1, y1 = path[0][0], path[0][1]
        x2, y2 = path[1][0], path[1][1]
        return abs((x1 - x2) + (y1 - y2)) == 1 #no need for sqrt 

    def _legal_path(self, path: places.Path) -> bool:
        if self.get_current_player().get_cash() < self._path_price:
            return False
        if not (self._in_board(path[0]) and self._in_board(path[1])):
            return False
        if not self._path_dist_1(path):
            return False
        connected = False #connected to the same player's city/path
        has_city = True #when connected to an enemy path there has to be a city between them
        for player_path in self._board.get_paths(): 
            coord1, coord2 = player_path[1][0], player_path[1][1]
            if (coord1, coord2) == path or (coord2, coord1) == path: #checks if path occupied
                return False
            elif (coord1 in path or coord2 in path): 
                if player_path[0] != self.get_current_player():#connected to enemy's path
                    has_city = False #to be checked later on
                else:
                    connected = True
        for player_city in self._board.get_cities():
            if player_city[1] in path:
                has_city = True
                if player_city[0] == self.get_current_player(): #checks if same player's city
                    connected = True
        return connected and has_city

    def _legal_city(self, coord: places.Coord) -> bool:
        """Given a coord, returns if a city can be built on it"""
        if self.get_current_player().get_cash() < self._city_price:
            return False
        if not self._in_board(coord):
            return False
        for player_city in self._board.get_cities(): #Checks if coord occupied
            if coord == player_city[1]:
                return False
        for player_path in self._board.get_paths(): #Checks if connected to a path
            if coord in player_path[1]:
                return True
        return False

    def _legal_destruction(self, coord: places.Coord) -> bool:
        """Given a coord, returns if a city can be destroyed there"""
        if self.get_current_player().get_cash() < self._destr_price:
            return False
        for player_city in self._board.get_cities(): #checks if there is a city from the same player
            if coord == player_city[1] and player_city[0] == self.get_current_player():
                return True
        return False

    def _resource_update(self, player: Player) -> None:
        """Given a player, subtracts the resources around all of his cities"""
        for player_city in self._board.get_cities():
            if player_city[0] == player:
                city_coord = player_city[1]
                for i in range(2):
                    for j in range(2): #checks if in board and if positive
                        resource_coord = places.Coord((city_coord[0] - i, city_coord[1] - j))
                        if self._in_board(resource_coord) and resource_coord[0] < self._board.get_size()[0] and resource_coord[1] < self._board.get_size()[1]:
                            if self._board.get_resources(resource_coord) > 0:
                                self._board.substract_resource(resource_coord)
                                self.get_current_player().update_cash(1)

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
        """Reads the following turn's input and executes the order"""
        if self.is_game_over(): #When the game is over, prints the winner
            winner = max (self._players, key=lambda player: player.get_cash())
            print("*"*20,"GAME OVER","*"*20)
            print(f"Player {winner.get_id()} wins with {winner.get_cash()} cash!")
            
        else:
            player = self.get_current_player()
            self._resource_update(player)
            print("-"*50)
            print(f"Player {player.get_id()}: you now have {player.get_cash()} cash")
            action = read(str)
            input_id = read(int)
            match action:
                case "build_path":
                    coord1 = (read(int), read(int))
                    coord2 = (read(int), read(int))
                    if self._legal_path(places.Path((coord1, coord2))) and player.get_id() == input_id:
                        self._board.add_path(player, (coord1, coord2))
                        player.update_cash(-self._path_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: You are not allowed to build a path on {coord1, coord2}. Turn cancelled.")
                case "build_city":
                    coord = (read(int), read(int))
                    if self._legal_city(coord) and player.get_id() == input_id:
                        self._board.add_city(player, coord)
                        player.update_cash(-self._city_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: You are not allowed to build a city on {coord}. Turn cancelled.")
                case "destroy_city":
                    coord = (read(int), read(int))
                    if self._legal_destruction(coord) and player.get_id() == input_id:
                        self._board.remove_city(coord)
                        player.update_cash(-self._destr_price)
                    elif player.get_id() == input_id:
                        print(f"Player {player.get_id()}: There is no city to destroy on {coord}. Turn cancelled.")
                case _:
                    pass
            if input_id != player.get_id():
                print(f"Player {player.get_id()}: you tried to play with player {input_id}'s id. Your turn will be skipped.")
            print(f"Player {player.get_id()}: you ended your turn with {player.get_cash()} cash")
            print("-"*50)
            self._current_turn += 1

