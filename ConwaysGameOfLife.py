import pygame
DEAD = WHITE = (255, 255, 255)  # WHITE
ALIVE = BLACK = (0, 0, 0)  # BLACK

####################### Customizable ##########################
FPS = 0
CellSize = 10
WindowDimensions = (50 * CellSize, 40 * CellSize)  # (Rows , Columns)
Program = 4
###############################################################

######################################## Programs: ############################################
#
#                            |*|
#   1)    |*|        2)  |*|*|       3) Pulsar       4) Gosper glider gun   5) Spaceship
#       |*|*|*|            |*|
#
###############################################################################################


BoardArr = [[None for i in range(int(WindowDimensions[0] / CellSize))] for j in  # Initialize an array for the board
            range(int(WindowDimensions[1] / CellSize))]
Window = None

print("Rows: ", len(BoardArr), ", Columns: ", len(BoardArr[0]))


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
            pygame.draw.rect(surface=Window, color=cellColor, rect=cell, width=1)


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

    NeighborsSum = 0  # Initializing number of neighbors of the checked cell
    ROW = cell[2]  # Getting the Row coordinate of the checked cell
    COLUMN = cell[3]  # Getting the Column coordinate of the checked cell

    print("Checking cell in row: ", ROW, ", column: ", COLUMN)
    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            if row == ROW - 1 and (
                    column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):  # Checks the row above the checked cell
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW + 1 and (
                    column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):  # Checks the row below the checked cell
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW and (
                    column == COLUMN - 1 or column == COLUMN + 1):  # Checks 2 cells: left and right to the checked cell
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
    global ruleA, ruleB  # Arrays to determine which cells need to be changed (ruleA -> Dead(White) , ruleB -> Alive(Black))
    """
    Function play iterates the cells on the board by rows and checks each cell with the CheckCell function
    """

    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            CheckCell(BoardArr[row][column])
    for cell in ruleA:
        ColorCell(cell, DEAD)
    ruleA.clear()
    for cell in ruleB:
        ColorCell(cell, ALIVE)
    ruleB.clear()


def starter(program):
    Program1 = [(8, 7), (8, 8), (8, 9), (7, 8)]
    Program2 = [(23, 25), (23, 26), (24, 26), (22, 27)]
    Program3 = [(10, 10), (11, 10), (12, 10), (8, 12), (8, 13), (8, 14), (13, 12), (13, 13), (13, 14), (10, 15),
                (11, 15), (12, 15),
                (16, 10), (17, 10), (18, 10), (15, 12), (15, 13), (15, 14), (20, 12), (20, 13), (20, 14), (16, 15),
                (17, 15), (18, 15),
                (10, 17), (11, 17), (12, 17), (8, 18), (8, 19), (8, 20), (13, 18), (13, 19), (13, 20), (10, 22),
                (11, 22), (12, 22),
                (16, 17), (17, 17), (18, 17), (15, 18), (15, 19), (15, 20), (20, 18), (20, 19), (20, 20), (16, 22),
                (17, 22), (18, 22)]
    Program4 = [(10, 3), (10, 4), (11, 13), (11, 4),
                (10, 13), (11, 13), (12, 13), (13, 14), (14, 15), (14, 16), (9, 14), (8, 15), (8, 16), (11, 17),
                (9, 18), (10, 19), (11, 19), (12, 19), (13, 18), (11, 20),
                (8, 23), (9, 23), (10, 23), (8, 24), (9, 24), (10, 24), (7, 25), (11, 25),
                (6, 27), (7, 27),
                (11, 27), (12, 27),
                (8, 37), (9, 37), (8, 38), (9, 38)]
    Program5 = [(6, 22), (7, 22), (8, 22), (9, 23), (6, 23), (6, 24), (6, 25), (6, 26), (7, 27),
                (19, 22), (20, 22), (21, 22), (18, 23), (21, 23), (21, 24), (21, 25), (21, 26), (20, 27),
                (10, 25), (10, 26), (11, 27), (12, 28), (13, 29), (14, 29), (15, 28), (16, 27), (17, 26), (17, 25),
                (15, 30), (12, 30),
                (10, 30), (10, 31), (11, 32), (12, 32),
                (17, 30), (17, 31), (16, 32), (15, 32),
                (10, 33), (9, 33), (10, 34), (9, 34), (8, 34), (8, 35), (7, 35), (7, 36), (9, 36), (9, 37),
                (8, 37), (10, 37), (9, 38), (8, 38), (10, 38), (8, 39), (9, 39), (11, 35), (12, 34),
                (17, 33), (18, 33), (17, 34), (18, 34), (19, 34), (19, 35), (20, 35), (20, 36), (18, 36), (18, 37),
                (17, 37), (19, 37), (18, 38), (17, 38), (19, 38), (18, 39), (19, 39), (16, 35), (15, 34)]

    if program == 1:
        for x, y in Program1:
            ColorCell(BoardArr[x][y], ALIVE)
    elif program == 2:
        for x, y in Program2:
            ColorCell(BoardArr[x][y], ALIVE)
    elif program == 3:
        for x, y in Program3:
            ColorCell(BoardArr[x][y], ALIVE)
    elif program == 4:
        for x, y in Program4:
            ColorCell(BoardArr[x][y], ALIVE)
    elif program == 5:
        for x, y in Program5:
            ColorCell(BoardArr[x][y], ALIVE)

    """
    Function to Startup the game by changing the state/color of random chosen cells on the board
    *** each program described in the beginning of the file ***
    """


def main():
    """
    Main function of the game, initializing the window, drawing the grid on the window, starting up the game according
    to set program and running until user closes the window.
    """
    clock = pygame.time.Clock()
    StartUpWindow()
    draw_grid()
    starter(Program)
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
