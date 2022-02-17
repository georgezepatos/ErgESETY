from random import choice
from typing import Union

class Score:
    def __init__(self) -> None:
        self.white: int = 0
        self.black: int = 0
        return

    def __str__(self) -> str: return "WHITE: " + str(self.white) + "\t\tBLACK: " + str(self.black)

class ChessPosition:
    HORIZONTAL = "ABCDEFGH"
    VERTICAL = [x for x in range(1, 9)]
    def __init__(self, horizontal: int, vertical: int) -> None:
        self.horizontal: int = horizontal
        if self.horizontal not in ChessPosition.VERTICAL: print("INVALID HORIZONTAL POSITION")
        self.vertical: int = vertical
        if self.vertical not in ChessPosition.VERTICAL: print("INVALID VERTICAL POSITION")
        return

    def __str__(self) -> str:
        return str(ChessPosition.HORIZONTAL[self.horizontal - 1]) + str(self.vertical)

    def __eq__(self, other) -> bool:
        if self.horizontal == other.horizontal and self.vertical == other.vertical: return True
        return False

    def __sub__(self, other): ...

    @staticmethod
    def random() -> object:
        return ChessPosition(choice(ChessPosition.VERTICAL), choice(ChessPosition.VERTICAL))

class CurrentPositions:
    def __init__(self) -> None:
        self.white_rook: Union[ChessPosition, None] = None
        self.white_bishop: Union[ChessPosition, None] = None
        self.black_queen: Union[ChessPosition, None] = None
        return

class Simulation:
    def __init__(self, games: int) -> None:
        self.positions = CurrentPositions()
        self.score = Score()
        for game in range(games): self.check()
        return

    def __str__(self) -> str:
        return "WHITE ROOK: " + str(self.positions.white_rook) + "\nWHITE BISHOP: " \
               + str(self.positions.white_bishop) + "\nBLACK QUEEN: " + str(self.positions.black_queen)

    def check(self):
        # new positions
        self.positions.white_rook = ChessPosition.random()
        self.positions.white_bishop = ChessPosition.random()
        self.positions.black_queen = ChessPosition.random()

        # white rook
        if self.positions.white_rook.horizontal == self.positions.black_queen.horizontal:
            self.score.white += 1
            self.score.black += 1
        elif self.positions.white_rook.vertical == self.positions.black_queen.vertical:
            self.score.white += 1
            self.score.black += 1

        # white bishop
        if abs(self.positions.white_bishop.horizontal - self.positions.black_queen.horizontal) == \
           abs(self.positions.white_bishop.vertical - self.positions.black_queen.vertical):
            self.score.white += 1
            self.score.black += 1

        # black queen
        if abs(self.positions.white_rook.horizontal - self.positions.black_queen.horizontal) == \
           abs(self.positions.white_rook.vertical - self.positions.black_queen.vertical): self.score.black += 1

        if self.positions.white_bishop.horizontal == self.positions.black_queen.horizontal:
            self.score.black += 1
        elif self.positions.white_bishop.vertical == self.positions.black_queen.vertical:
            self.score.black += 1


if __name__ == "__main__": print(Simulation(100).score)