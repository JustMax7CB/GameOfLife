import pygame

FPS = 60
DEAD = WHITE = (255, 255, 255)  # WHITE
ALIVE = BLACK = (0, 0, 0)  # BLACK
ABOUT_TO_DIE = (56, 69, 69)  # GRAYISH
CellSize = 10
WindowDimensions = (50 * CellSize, 30 * CellSize)  # (Rows , Columns)
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
            cellColor = DEAD
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
        ruleA.append(cell)
    elif cell[1] == ALIVE and (NeighborsSum > 3):  # Alive and has 4+ neighbors -> Dead
        ruleA.append(cell)
    elif cell[1] == ALIVE and (NeighborsSum == 2 or NeighborsSum == 3):  # Alive and has 2/3 neighbors -> Alive
        ruleB.append(cell)
    elif cell[1] == DEAD and NeighborsSum == 3:  # if Dead adn has exactly 3 neighbors -> Alive
        ruleB.append(cell)


def ColorCell(cell, color):
    """
    Function ColorCell given a cell which is a pygame.rect object from the board array, and state(color) he should be
    in.
    :param cell:
    :param color:
    """
    Window.fill(color, cell[0])
    cell[1] = color


ruleA = []  # Alive and has 0/1 neighbors OR Alive and has 4+ neighbors -> Dead
ruleB = []  # Alive and has 2/3 neighbors OR Dead and has exactly 3 neighbors -> Alive


def play():
    global ruleA, ruleB
    """
    Function play iterates the cells on the board by rows and checks each cell with the CheckCell function
    """

    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            CheckCell(BoardArr[row][column])
    print("Before: ", ruleA)
    print("Before: ", ruleB)
    for cell in ruleA:
        ColorCell(cell, DEAD)
    ruleA = []
    for cell in ruleB:
        ColorCell(cell, ALIVE)
    ruleB = []


def starter():
    """
    Function to Startup the game by changing the state/color of random chosen cells on the board
    """
    # #    *
    # #   ***
    # #
    # ColorCell(BoardArr[8][7], ALIVE)
    # ColorCell(BoardArr[8][8], ALIVE)
    # ColorCell(BoardArr[8][9], ALIVE)
    # ColorCell(BoardArr[7][8], ALIVE)
    #
    # #      *
    # #    **
    # #     *
    # #
    #
    # ColorCell(BoardArr[23][25], ALIVE)
    # ColorCell(BoardArr[23][26], ALIVE)
    # ColorCell(BoardArr[24][26], ALIVE)
    # ColorCell(BoardArr[22][27], ALIVE)

    ColorCell(BoardArr[10][10], ALIVE)
    ColorCell(BoardArr[11][10], ALIVE)
    ColorCell(BoardArr[12][10], ALIVE)
    ColorCell(BoardArr[8][12], ALIVE)
    ColorCell(BoardArr[8][13], ALIVE)
    ColorCell(BoardArr[8][14], ALIVE)
    ColorCell(BoardArr[13][12], ALIVE)
    ColorCell(BoardArr[13][13], ALIVE)
    ColorCell(BoardArr[13][14], ALIVE)
    ColorCell(BoardArr[10][15], ALIVE)
    ColorCell(BoardArr[11][15], ALIVE)
    ColorCell(BoardArr[12][15], ALIVE)

    ColorCell(BoardArr[16][10], ALIVE)
    ColorCell(BoardArr[17][10], ALIVE)
    ColorCell(BoardArr[18][10], ALIVE)
    ColorCell(BoardArr[15][12], ALIVE)
    ColorCell(BoardArr[15][13], ALIVE)
    ColorCell(BoardArr[15][14], ALIVE)
    ColorCell(BoardArr[13][12], ALIVE)
    ColorCell(BoardArr[20][12], ALIVE)
    ColorCell(BoardArr[20][13], ALIVE)
    ColorCell(BoardArr[20][14], ALIVE)
    ColorCell(BoardArr[16][15], ALIVE)
    ColorCell(BoardArr[17][15], ALIVE)
    ColorCell(BoardArr[18][15], ALIVE)

    ColorCell(BoardArr[10][17], ALIVE)
    ColorCell(BoardArr[11][17], ALIVE)
    ColorCell(BoardArr[12][17], ALIVE)
    ColorCell(BoardArr[8][18], ALIVE)
    ColorCell(BoardArr[8][19], ALIVE)
    ColorCell(BoardArr[8][20], ALIVE)
    ColorCell(BoardArr[13][18], ALIVE)
    ColorCell(BoardArr[13][19], ALIVE)
    ColorCell(BoardArr[13][20], ALIVE)
    ColorCell(BoardArr[10][22], ALIVE)
    ColorCell(BoardArr[11][22], ALIVE)
    ColorCell(BoardArr[12][22], ALIVE)

    ColorCell(BoardArr[16][17], ALIVE)
    ColorCell(BoardArr[17][17], ALIVE)
    ColorCell(BoardArr[18][17], ALIVE)
    ColorCell(BoardArr[15][18], ALIVE)
    ColorCell(BoardArr[15][19], ALIVE)
    ColorCell(BoardArr[15][20], ALIVE)
    ColorCell(BoardArr[20][18], ALIVE)
    ColorCell(BoardArr[20][19], ALIVE)
    ColorCell(BoardArr[20][20], ALIVE)
    ColorCell(BoardArr[16][22], ALIVE)
    ColorCell(BoardArr[17][22], ALIVE)
    ColorCell(BoardArr[18][22], ALIVE)

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
