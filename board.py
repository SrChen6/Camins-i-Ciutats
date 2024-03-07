from player import Player
from places import BoxSize, Coord, Path

class Board:
    _size: BoxSize
    _initial_resources: list[list[int]]

    def __init__(self, size: BoxSize, initial_resources: list[list[int]]):
        self._size = size
        self._initial_resources = initial_resources

    def get_size(self) -> BoxSize:
        return 

    def get_resources(self, coord: Coord) -> int: ...

    def get_cities(self) -> list[tuple[Player, Coord]]: ...

    def get_paths(self) -> list[tuple[Player, Path]]: ...

    def add_city(self, player: Player, coord: Coord) -> None: ...

    def remove_city(self, coord: Coord) -> None: ...

    def add_path(self, player: Player, path: Path) -> None: ...

    def substract_resource(self, coord: Coord) -> None: ...
