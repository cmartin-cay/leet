"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""


class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle
        print(self.rectangle)


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j]=newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

rect = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(rect.getValue(0, 2))
rect.updateSubrectangle(*[0,0,3,2,5])
print(rect.getValue(0, 0))