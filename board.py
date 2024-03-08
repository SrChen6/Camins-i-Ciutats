from player import Player
from places import BoxSize, Coord, Path

class Board:
    _size: BoxSize
    _resources: list[list[int]]
    _citites: list[tuple[Player, Coord]]
    _paths: list[tuple[Player, Path]]


    def __init__(self, size: BoxSize, initial_resources: list[list[int]]):
        """Constructor of the Board class"""
        self._size = size
        self._resources = initial_resources

    def get_size(self) -> BoxSize:
        """Returns the size of the board"""
        return self._size

    def get_resources(self, coord: Coord) -> int:
        """Returns the number of resources of a single coordenate"""
        return self._resources

    def get_cities(self) -> list[tuple[Player, Coord]]: 
        """Returns the cities of every player"""
        return self._citites

    def get_paths(self) -> list[tuple[Player, Path]]: 
        """Returns the paths of every player"""
        return self._paths

    def add_city(self, player: Player, coord: Coord) -> None:
        """Adds a city for a player in a coordenate on the board"""
        ...

    def remove_city(self, coord: Coord) -> None:
        """Removes a city for a player in a coordenate on the board"""
        ...

    def add_path(self, player: Player, path: Path) -> None:
        """Adds a path for a player"""
        ...

    def substract_resource(self, coord: Coord) -> None:
        """subtracts 1 unit of resources arount a coordenate"""
        ...