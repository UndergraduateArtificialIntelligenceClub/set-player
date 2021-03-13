COLOR_RED = 0
COLOR_GREEN = 1
COLOR_BLUE = 2
SHAPE_PILL = 0
SHAPE_SQUIGGLY = 1
SHAPE_DIAMOND = 2
NUMBER_ONE = 0
NUMBER_TWO = 1
NUMBER_THREE = 2
FILL_EMPTY = 0
FILL_HALF = 1
FILL_FULL = 2

class Card:
    def __init__(self, color: int, shape: int, number: int, fill: int):
        assert color in (COLOR_RED, COLOR_GREEN, COLOR_BLUE)
        self.color = color
        assert shape in (SHAPE_PILL, SHAPE_SQUIGGLY, SHAPE_DIAMOND)
        self.shape = shape
        assert number in (NUMBER_ONE, NUMBER_TWO, NUMBER_THREE)
        self.number = number
        assert fill in (FILL_EMPTY, FILL_HALF, FILL_FULL)
        self.fill = fill

    def get_color(self) -> int:
        return self.color

    def get_shape(self) -> int:
        return self.shape

    def get_number(self) -> int:
        return self.number

    def get_fill(self) -> int:
        return self.fill

    @staticmethod
    def valid(first: "Card", second: "Card", third: "Card") -> bool:
        # Check colour
        if not Card.all_or_nothing(first, second, third, Card.get_color):
            return False

        # Check shape
        if not Card.all_or_nothing(first, second, third, Card.get_shape):
            return False

        # Check number
        if not Card.all_or_nothing(first, second, third, Card.get_fill):
            return False

        # Check fill
        if not Card.all_or_nothing(first, second, third, Card.get_number):
            return False

    @staticmethod
    def all_or_nothing(first: "Card", second: "Card", third: "Card", get_method):
        f, s, t = first.get_method(), second.get_method(), third.get_method()
        return (f + s + t % 3) != 0
