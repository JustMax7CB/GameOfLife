import pygame

FPS = 1
DEAD = WHITE = (255, 255, 255)  # WHITE
ALIVE = BLACK = (0, 0, 0)  # BLACK
ABOUT_TO_DIE = (56, 69, 69)  # GRAYISH
CellSize = 20
WindowDimensions = (20 * CellSize, 10 * CellSize)  # (Rows , Columns)
BoardArr = [[None for i in range(int(WindowDimensions[0] / CellSize))] for j in  # Initialize an array for the board
            range(int(WindowDimensions[1] / CellSize))]
Window = None

print("Rows: ", len(BoardArr), ", Columns: ", len(BoardArr[0]))
print(BoardArr)


def StartUpWindow():
    """
    Function StartUpWindow Creates The Main Window of the game according to window dimensions
    which determined and calculated in the global environment, set background color, and set window title
    """

    global Window
    Window = pygame.display.set_mode(WindowDimensions)
    Window.fill(WHITE)
    pygame.display.set_caption("Conway's game of life!")


def draw_grid():
    """
    Function draw_grid works after the window created and draws Rectangles(pygame.Rect) in the window to create a
    grid by starting from (0,0) and jumping CellSize each direction until the window size.
    """

    Column, Row = 0, 0

    def AddCellToArray(cell, cellColor):

        """
        Function AddCellToArray given the cell which just has been created by pygame.Rect method, and his started up
        color, adds a list of the cell to the board array in format: [pygame.Rect, Color, Row, Column]
        :param cell:
        :param cellColor:
        """

        nonlocal Column, Row
        if Row < len(BoardArr):
            if Column < len(BoardArr[0]):
                BoardArr[Row][Column] = [cell, cellColor, Row, Column]
                Column += 1
            else:
                Row += 1
                Column = 0
                BoardArr[Row][Column] = [cell, cellColor, Row, Column]
                Column += 1
        else:
            print("Error adding cell to array")

    for y in range(0, WindowDimensions[1], CellSize):
        for x in range(0, WindowDimensions[0], CellSize):
            cell = pygame.Rect(x, y, CellSize, CellSize)
            cellColor = WHITE
            AddCellToArray(cell, cellColor)
            pygame.draw.rect(surface=Window, color=cellColor, rect=cell, width=0)
    print(BoardArr)


def CheckCell(cell):
    """
    Function CheckCell given a cell parameter which is a pygame.Rect object from the array which consists the game board
    and checks his surrounding neighbors to determine if he should be alive(Black) or dead(White)
    :param cell:
    """

    # if Alive and has 0/1 neighbors -> Dead
    # if Alive and has 4+ neighbors -> Dead
    # if Alive and has 2/3 neighbors -> Alive
    # if Dead adn has exactly 3 neighbors -> Alive

    NeighborsSum = 0
    ROW = cell[2]
    COLUMN = cell[3]

    print("Checking cell in row: ", ROW, ", column: ", COLUMN)
    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            if row == ROW - 1 and (
                    column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):  # Checks the row above the cell
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW + 1 and (
                    column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):  # Checks the row below the cell
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW and (
                    column == COLUMN - 1 or column == COLUMN + 1):  # Checks 2 cells: left and right to the cell
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
    print("Neighbors Count: ", NeighborsSum)
    if cell[1] == ALIVE and (NeighborsSum == 0 or NeighborsSum == 1):  # Alive and has 0/1 neighbors -> Dead
        ColorCell(cell, DEAD)
    elif cell[1] == ALIVE and (NeighborsSum > 3):  # Alive and has 4+ neighbors -> Dead
        ColorCell(cell, DEAD)
    elif cell[1] == ALIVE and (NeighborsSum == 2 or NeighborsSum == 3):  # Alive and has 2/3 neighbors -> Alive
        ColorCell(cell, ALIVE)
    elif cell[1] == DEAD and NeighborsSum == 3:  # if Dead adn has exactly 3 neighbors -> Alive
        ColorCell(cell, ALIVE)


def ColorCell(cell, color):
    """
    Function ColorCell given a cell which is a pygame.rect object from the board array, and state(color) he should be
    in.
    :param cell:
    :param color:
    """
    Window.fill(color, cell[0])
    cell[1] = color


def play():
    """
    Function play iterates the cells on the board by rows and checks each cell with the CheckCell function
    """

    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            if BoardArr[row][column][1] == ALIVE:
                CheckCell(BoardArr[row][column])


def starter():
    """
    Function to Startup the game by changing the state/color of random chosen cells on the board
    """

    ColorCell(BoardArr[1][8], ALIVE)
    ColorCell(BoardArr[1][9], ALIVE)
    ColorCell(BoardArr[1][10], ALIVE)
    ColorCell(BoardArr[2][7], ALIVE)
    ColorCell(BoardArr[2][8], ALIVE)
    ColorCell(BoardArr[2][9], ALIVE)


def main():
    clock = pygame.time.Clock()
    StartUpWindow()
    draw_grid()
    starter()
    run = True
    while run:
        clock.tick(FPS)
        play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
