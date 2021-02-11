class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    def moveUp(self):
        self.col = self.col + 1

    def moveDown(self):
        self.col = self.col + 1

    def moveLeft(self):
        self.row = self.row + 1

    def moveRight(self):
        self.row = self.row + 1
