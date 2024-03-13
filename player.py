class Player:
    _id: int
    _cash: int
    _color: str

    def __init__(self, id: int, cash: int, color: str):
        """Constructor of the Player class"""
        self._id = id
        self._cash = cash
        self._color = color

    def get_id(self) -> int:
        """Returns the information of a player (the number)"""
        return self._id

    def get_cash(self) -> int:
        """Returns the cash of a player"""
        return self._cash

    def get_color(self) -> str:
        """Returns the color of a player"""
        return self._color

    def update_cash(self, value: int) -> None:
        """Updates the cash of a player"""
        self._cash += value