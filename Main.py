import pygame
FPS = 1
DEAD = WHITE = (255, 255, 255)  # WHITE
ALIVE = BLACK = (0, 0, 0)  # BLACK
ABOUT_TO_DIE = (56, 69, 69)  # GRAYISH
CellSize = 10
WindowDimensions = (80 * CellSize, 40 * CellSize)
BoardArr = [[None for i in range(int(WindowDimensions[0] / CellSize))] for j in
            range(int(WindowDimensions[1] / CellSize))]
Window = None

print(len(BoardArr), ", ", len(BoardArr[0]))


def StartUpWindow():
    global Window
    Window = pygame.display.set_mode(WindowDimensions)
    Window.fill(WHITE)
    pygame.display.set_caption("Conway's game of life!")


def draw_grid():
    Column, Row = 0, 0

    def AddCellToArray(cell, cellColor):
        nonlocal Column, Row
        if Row < len(BoardArr):
            if Column < len(BoardArr[0]):
                BoardArr[Row][Column] = [cell, cellColor]
                Column += 1
            else:
                Row += 1
                Column = 0
                BoardArr[Row][Column] = [cell, cellColor]
                Column += 1
        else:
            print("Error adding cell to array")

    for y in range(0, WindowDimensions[1], CellSize):
        for x in range(0, WindowDimensions[0], CellSize):
            cell = pygame.Rect(x, y, CellSize, CellSize)
            cellColor = WHITE
            AddCellToArray(cell, cellColor)
            pygame.draw.rect(surface=Window, color=cellColor, rect=cell, width=0)


def CheckCell(cell):
    # if Alive and has 0/1 neighbors - Dead
    # if Alive and has 4+ neighbors - Dead
    # if Alive and has 2/3 neighbors - Alive
    # if Dead adn has exactly 3 neighbors - Alive
    NeighborsSum, COLUMN, ROW = 0, 0, 0
    for column in range(len(BoardArr[0])):
        for row in range(len(BoardArr)):
            if BoardArr[row][column] == cell:
                ROW = row
                COLUMN = column
                print(cell)
                print(BoardArr[row][column])
                break
    print(ROW, COLUMN)
    for column in range(len(BoardArr[0])):
        for row in range(len(BoardArr)):
            if row == ROW - 1 and (column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW + 1 and (column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW and (column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
    print(row, column, NeighborsSum)
    if cell[1] == ALIVE and (NeighborsSum == 0 or NeighborsSum == 1):
        ColorCell(cell, DEAD)
    elif cell[1] == ALIVE and (NeighborsSum > 3):
        ColorCell(cell, DEAD)
    elif cell[1] == ALIVE and (NeighborsSum == 2 or NeighborsSum == 3):
        ColorCell(cell, ALIVE)
    elif cell[1] == DEAD and NeighborsSum == 3:
        ColorCell(cell, ALIVE)


def ColorCell(cell, color):
    Window.fill(color, cell[0])
    cell[1] = color


def play():
    for row in range(len(BoardArr[0])):
        for column in range(len(BoardArr)):
            if BoardArr[column][row][1] == ALIVE:
                CheckCell(BoardArr[column][row])
def start():
    ColorCell(BoardArr[23][22], ALIVE)
    ColorCell(BoardArr[23][23], ALIVE)
    ColorCell(BoardArr[23][24], ALIVE)
    ColorCell(BoardArr[24][21], ALIVE)
    ColorCell(BoardArr[24][22], ALIVE)
    ColorCell(BoardArr[25][22], ALIVE)
    ColorCell(BoardArr[26][22], ALIVE)
    ColorCell(BoardArr[25][23], ALIVE)
    ColorCell(BoardArr[13][13], ALIVE)
    ColorCell(BoardArr[13][12], ALIVE)
    ColorCell(BoardArr[12][13], ALIVE)
    ColorCell(BoardArr[12][14], ALIVE)
    ColorCell(BoardArr[13][11], ALIVE)
    ColorCell(BoardArr[15][12], ALIVE)

def main():
    clock = pygame.time.Clock()
    StartUpWindow()
    draw_grid()
    start()
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
