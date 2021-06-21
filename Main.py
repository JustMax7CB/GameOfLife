import pygame

FPS = 1
DEAD = WHITE = (255, 255, 255)  # WHITE
ALIVE = BLACK = (0, 0, 0)  # BLACK
ABOUT_TO_DIE = (56, 69, 69)  # GRAYISH
CellSize = 20
WindowDimensions = (20 * CellSize, 10 * CellSize)  # (Rows , Columns)
BoardArr = [[None for i in range(int(WindowDimensions[0] / CellSize))] for j in
            range(int(WindowDimensions[1] / CellSize))]
Window = None

print("Rows: ", len(BoardArr), ", Columns: ", len(BoardArr[0]))
print(BoardArr)


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
    # if Alive and has 0/1 neighbors - Dead
    # if Alive and has 4+ neighbors - Dead
    # if Alive and has 2/3 neighbors - Alive
    # if Dead adn has exactly 3 neighbors - Alive

    NeighborsSum = 0
    ROW = cell[2]
    COLUMN = cell[3]

    print(ROW, COLUMN)
    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            if row == ROW - 1 and (column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW + 1 and (column == COLUMN or column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
            elif row == ROW and (column == COLUMN - 1 or column == COLUMN + 1):
                if BoardArr[row][column][1] == ALIVE:
                    NeighborsSum += 1
    print("Neighbors Count: ", NeighborsSum)
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
    for row in range(len(BoardArr)):
        for column in range(len(BoardArr[0])):
            if BoardArr[row][column][1] == ALIVE:
                CheckCell(BoardArr[row][column])


def start():
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
