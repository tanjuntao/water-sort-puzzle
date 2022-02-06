from bottle import Bottle
from color import Colors

def get_board():
    N_BOTTLES = 9
    global_board = []
    bottles = [[] for _ in range(N_BOTTLES)]

    bottles[0] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]
    bottles[1] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]

    # Number 3
    # bottles[2] = [Colors.BLUE, Colors.RED, Colors.BLUE, Colors.GREEN]
    # bottles[3] = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.GREEN]
    # bottles[4] = [Colors.RED, Colors.BLUE, Colors.RED, Colors.GREEN]

    # Number 4
    # bottles[1] = [Colors.GREEN, Colors.BLUE, Colors.RED, Colors.GREEN]
    # bottles[2] = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.RED]
    # bottles[3] = [Colors.BLUE, Colors.RED, Colors.GREEN, Colors.BLUE]
    # bottles[4] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]

    # Number

    # Number 7
    # bottles[2] = [Colors.PURPLE, Colors.GREEN, Colors.RED, Colors.YELLOW]
    # bottles[3] = [Colors.GREEN, Colors.PURPLE, Colors.RED, Colors.YELLOW]
    # bottles[4] = [Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.RED]
    # bottles[5] = [Colors.YELLOW, Colors.BLUE, Colors.GREEN, Colors.BLUE]
    # bottles[6] = [Colors.PURPLE, Colors.PURPLE, Colors.BLUE, Colors.RED]

    # Number 8
    # bottles[2] = [Colors.BLUE, Colors.PURPLE, Colors.PURPLE, Colors.GREEN]
    # bottles[3] = [Colors.BLUE, Colors.GREEN, Colors.GREEN, Colors.YELLOW]
    # bottles[4] = [Colors.YELLOW, Colors.BLUE, Colors.RED, Colors.YELLOW]
    # bottles[5] = [Colors.PURPLE, Colors.GREEN, Colors.RED, Colors.RED]
    # bottles[6] = [Colors.YELLOW, Colors.BLUE, Colors.PURPLE, Colors.RED]

    # Number 9
    # bottles[2] = [Colors.YELLOW, Colors.BLUE, Colors.RED, Colors.BLUE]
    # bottles[3] = [Colors.RED, Colors.PURPLE, Colors.BLUE, Colors.GREEN]
    # bottles[4] = [Colors.RED, Colors.BLUE, Colors.PURPLE, Colors.YELLOW]
    # bottles[5] = [Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.GREEN]
    # bottles[6] = [Colors.PURPLE, Colors.GREEN, Colors.PURPLE, Colors.RED]

    # Number 10
    # bottles[2] = [Colors.SHIT_YELLOW, Colors.BLUE, Colors.SHIT_YELLOW, Colors.PURPLE]
    # bottles[3] = [Colors.BLUE, Colors.PURPLE, Colors.DEEP_GREEN, Colors.SHIT_YELLOW]
    # bottles[4] = [Colors.RED, Colors.RED, Colors.DEEP_GREEN, Colors.PURPLE]
    # bottles[5] = [Colors.GREEN, Colors.YELLOW, Colors.DEEP_GREEN, Colors.YELLOW]
    # bottles[6] = [Colors.RED, Colors.RED, Colors.GREEN, Colors.YELLOW]
    # bottles[7] = [Colors.PURPLE, Colors.BLUE, Colors.GREEN, Colors.YELLOW]
    # bottles[8] = [Colors.SHIT_YELLOW, Colors.GREEN, Colors.BLUE, Colors.DEEP_GREEN]

    # Number 11
    bottles[2] = [Colors.YELLOW, Colors.RED, Colors.PURPLE, Colors.RED]
    bottles[3] = [Colors.GREEN, Colors.SHIT_YELLOW, Colors.YELLOW, Colors.BLUE]
    bottles[4] = [Colors.RED, Colors.DEEP_GREEN, Colors.DEEP_GREEN, Colors.PURPLE]
    bottles[5] = [Colors.BLUE, Colors.YELLOW, Colors.GREEN, Colors.SHIT_YELLOW]
    bottles[6] = [Colors.YELLOW, Colors.GREEN, Colors.GREEN, Colors.PURPLE]
    bottles[7] = [Colors.SHIT_YELLOW, Colors.SHIT_YELLOW, Colors.PURPLE, Colors.BLUE]
    bottles[8] = [Colors.RED, Colors.BLUE, Colors.DEEP_GREEN, Colors.DEEP_GREEN]




    # Number 200
    # bottles[2] = [Colors.PINK, Colors.GREEN, Colors.PURPLE, Colors.DEEP_GREEN]
    # bottles[3] = [Colors.RED, Colors.DEEP_GREEN, Colors.BROWN, Colors.SHALLOW_BLUE]
    # bottles[4] = [Colors.SKY_BLUE, Colors.SHALLOW_BLUE, Colors.SKY_BLUE, Colors.BLUE]
    # bottles[5] = [Colors.DEEP_GREEN, Colors.YELLOW, Colors.PINK, Colors.BLUE]
    # bottles[6] = [Colors.YELLOW, Colors.YELLOW, Colors.SHIT_YELLOW, Colors.ORANGE]
    # bottles[7] = [Colors.GREEN, Colors.GREEN, Colors.SHALLOW_BLUE, Colors.BLUE]
    # bottles[8] = [Colors.RED, Colors.SKY_BLUE, Colors.SHIT_YELLOW, Colors.BLUE]
    # bottles[9] = [Colors.GREEN, Colors.BROWN, Colors.SHIT_YELLOW, Colors.DEEP_GREEN]
    # bottles[10] = [Colors.RED, Colors.ORANGE, Colors.SHALLOW_BLUE, Colors.PURPLE]
    # bottles[11] = [Colors.SKY_BLUE, Colors.ORANGE, Colors.RED, Colors.PURPLE]
    # bottles[12] = [Colors.BROWN, Colors.YELLOW, Colors.SHIT_YELLOW, Colors.PURPLE]
    # bottles[13] = [Colors.PINK, Colors.PINK, Colors.BROWN, Colors.ORANGE]



    for i in range(N_BOTTLES):
        _bottle = Bottle(i, bottles[i])
        global_board.append(_bottle)

    return global_board


if __name__ == '__main__':
    board = get_board()
    for bottle in board:
        print(bottle.number, bottle.data)











