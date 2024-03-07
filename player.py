class Player:
    _id: int
    _cash: int
    _color: str

    def __init__(self, id: int, cash: int, color: str):
        self._id = id
        self._cash = cash
        self._color = color

    def get_id(self) -> int:
        return self._id

    def get_cash(self) -> int:
        return self._cash

    def get_color(self) -> str:
        return self._color

    def update_cash(self, value: int) -> None: ...
