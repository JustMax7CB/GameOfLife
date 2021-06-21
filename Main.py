import pygame

ALIVE = WHITE = (255, 255, 255)  # WHITE
DEAD = BLACK = (0, 0, 0)  # BLACK
CellSize = 40
WindowDimensions = (10 * CellSize, 5 * CellSize)
BoardArr = [[None for i in range(int(WindowDimensions[0] / CellSize))] for j in
            range(int(WindowDimensions[1] / CellSize))]
Window = None

print(len(BoardArr), ", ", len(BoardArr[0]))
print(BoardArr)


def StartUpWindow():
    global Window
    Window = pygame.display.set_mode(WindowDimensions)
    Window.fill(WHITE)
    pygame.display.set_caption("Conway's game of life!")


def draw_grid():
    Column, Row = 0, 0

    def AddCellToArray(cell):
        nonlocal Column, Row
        if Row < len(BoardArr):
            if Column < len(BoardArr[0]):
                BoardArr[Row][Column] = cell
                Column += 1
            else:
                Row += 1
                Column = 0
                BoardArr[Row][Column] = cell
                Column += 1
        else:
            print("Error adding cell to array")

    for y in range(0, WindowDimensions[1], CellSize):
        for x in range(0, WindowDimensions[0], CellSize):
            cell = pygame.Rect(x, y, CellSize, CellSize)
            AddCellToArray(cell)
            pygame.draw.rect(surface=Window, color=BLACK, rect=cell, width=1)


def ColorCell():
    Window.fill(BLACK, BoardArr[2][4])
    Window.fill(BLACK, BoardArr[4][9])


def main():
    pygame.init()
    StartUpWindow()
    run = True
    while run:
        draw_grid()
        ColorCell()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
