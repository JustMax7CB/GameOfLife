import pygame

ALIVE = WHITE = (255, 255, 255)  # WHITE
DEAD = BLACK = (0, 0, 0)  # BLACK
CellSize = 15
WindowDimensions = (50 * CellSize, 20 * CellSize)
BoardArr = [[None for i in range(int(WindowDimensions[0]/CellSize))] for j in range(int(WindowDimensions[1]/CellSize))]
Window = None

print(len(BoardArr), ", ", len(BoardArr[0]))
print(BoardArr)

def StartUpWindow():
    global Window
    Window = pygame.display.set_mode(WindowDimensions)
    Window.fill(WHITE)
    pygame.display.set_caption("Conway's game of life!")


def draw_grid():
    ArrayX, ArrayY = 0, 0

    def AddCell(cell):
        nonlocal ArrayY, ArrayX
        if ArrayX < len(BoardArr):
            if ArrayY < len(BoardArr[ArrayX]):
                BoardArr[ArrayX][ArrayY] = cell
                ArrayY += 1
            else:
                ArrayX += 1
                ArrayY = 0
                BoardArr[ArrayX][ArrayY] = cell
                ArrayY += 1
        else:
            print("Error adding cell to array")

    for x in range(0, WindowDimensions[0], CellSize):
        for y in range(0, WindowDimensions[1], CellSize):
            cell = pygame.Rect(x, y, CellSize, CellSize)
            AddCell(cell)
            pygame.draw.rect(surface=Window, color=BLACK, rect=cell, width=1)


def ColorCell():
    for i in range(5):
        Window.fill(BLACK, BoardArr[i][0])




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
