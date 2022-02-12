from bottle import Bottle
from color import Colors


def get_start_board():
    """Start board of the game level n

    Modify this function if you want to play new game level

    NOTE: COLORS SHOULD BE INPUTED FROM BOTTOL BOTTOM TO TOP
    """
    N_BOTTLES = 14  # total number of bottles including empty bottles
    global_board = []
    bottles = [[] for _ in range(N_BOTTLES)]

    # the first two bottles are always empty
    bottles[0] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]
    bottles[1] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]

    # Level 3
    # bottles[1] = [Colors.BLUE, Colors.RED, Colors.BLUE, Colors.GREEN]
    # bottles[2] = [Colors.RED, Colors.BLUE, Colors.GREEN, Colors.GREEN]
    # bottles[3] = [Colors.RED, Colors.BLUE, Colors.RED, Colors.GREEN]
    # bottles[4] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]

    # Level 4
    # bottles[1] = [Colors.GREEN, Colors.BLUE, Colors.RED, Colors.GREEN]
    # bottles[2] = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.RED]
    # bottles[3] = [Colors.BLUE, Colors.RED, Colors.GREEN, Colors.BLUE]
    # bottles[4] = [Colors.BLANK, Colors.BLANK, Colors.BLANK, Colors.BLANK]

    # Level 7
    # bottles[2] = [Colors.PURPLE, Colors.GREEN, Colors.RED, Colors.YELLOW]
    # bottles[3] = [Colors.GREEN, Colors.PURPLE, Colors.RED, Colors.YELLOW]
    # bottles[4] = [Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.RED]
    # bottles[5] = [Colors.YELLOW, Colors.BLUE, Colors.GREEN, Colors.BLUE]
    # bottles[6] = [Colors.PURPLE, Colors.PURPLE, Colors.BLUE, Colors.RED]

    # Level 8
    # bottles[2] = [Colors.BLUE, Colors.PURPLE, Colors.PURPLE, Colors.GREEN]
    # bottles[3] = [Colors.BLUE, Colors.GREEN, Colors.GREEN, Colors.YELLOW]
    # bottles[4] = [Colors.YELLOW, Colors.BLUE, Colors.RED, Colors.YELLOW]
    # bottles[5] = [Colors.PURPLE, Colors.GREEN, Colors.RED, Colors.RED]
    # bottles[6] = [Colors.YELLOW, Colors.BLUE, Colors.PURPLE, Colors.RED]

    # Level 9
    # bottles[2] = [Colors.YELLOW, Colors.BLUE, Colors.RED, Colors.BLUE]
    # bottles[3] = [Colors.RED, Colors.PURPLE, Colors.BLUE, Colors.GREEN]
    # bottles[4] = [Colors.RED, Colors.BLUE, Colors.PURPLE, Colors.YELLOW]
    # bottles[5] = [Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.GREEN]
    # bottles[6] = [Colors.PURPLE, Colors.GREEN, Colors.PURPLE, Colors.RED]

    # Level 10
    # bottles[2] = [Colors.SHIT_YELLOW, Colors.BLUE, Colors.SHIT_YELLOW, Colors.PURPLE]
    # bottles[3] = [Colors.BLUE, Colors.PURPLE, Colors.DEEP_GREEN, Colors.SHIT_YELLOW]
    # bottles[4] = [Colors.RED, Colors.RED, Colors.DEEP_GREEN, Colors.PURPLE]
    # bottles[5] = [Colors.GREEN, Colors.YELLOW, Colors.DEEP_GREEN, Colors.YELLOW]
    # bottles[6] = [Colors.RED, Colors.RED, Colors.GREEN, Colors.YELLOW]
    # bottles[7] = [Colors.PURPLE, Colors.BLUE, Colors.GREEN, Colors.YELLOW]
    # bottles[8] = [Colors.SHIT_YELLOW, Colors.GREEN, Colors.BLUE, Colors.DEEP_GREEN]

    # Level 11
    # bottles[2] = [Colors.YELLOW, Colors.RED, Colors.PURPLE, Colors.RED]
    # bottles[3] = [Colors.GREEN, Colors.SHIT_YELLOW, Colors.YELLOW, Colors.BLUE]
    # bottles[4] = [Colors.RED, Colors.DEEP_GREEN, Colors.DEEP_GREEN, Colors.PURPLE]
    # bottles[5] = [Colors.BLUE, Colors.YELLOW, Colors.GREEN, Colors.SHIT_YELLOW]
    # bottles[6] = [Colors.YELLOW, Colors.GREEN, Colors.GREEN, Colors.PURPLE]
    # bottles[7] = [Colors.SHIT_YELLOW, Colors.SHIT_YELLOW, Colors.PURPLE, Colors.BLUE]
    # bottles[8] = [Colors.RED, Colors.BLUE, Colors.DEEP_GREEN, Colors.DEEP_GREEN]

    # Level 12
    # bottles[2] = [Colors.RED, Colors.RED, Colors.PURPLE,Colors.BLUE]
    # bottles[3] = [Colors.PURPLE, Colors.GREEN, Colors.YELLOW, Colors.RED]
    # bottles[4] = [Colors.GREEN, Colors.YELLOW, Colors.PURPLE, Colors.YELLOW]
    # bottles[5] = [Colors.YELLOW, Colors.PURPLE, Colors.BLUE, Colors.GREEN]
    # bottles[6] = [Colors.GREEN, Colors.BLUE, Colors.BLUE, Colors.RED]

    # Level 13
    # bottles[2] = [Colors.RED, Colors.GREEN, Colors.SHIT_YELLOW, Colors.SHIT_YELLOW]
    # bottles[3] = [Colors.GREEN, Colors.YELLOW, Colors.PURPLE, Colors.SHIT_YELLOW]
    # bottles[4] = [Colors.RED, Colors.PURPLE, Colors.DEEP_GREEN, Colors.BLUE]
    # bottles[5] = [Colors.PURPLE, Colors.DEEP_GREEN, Colors.YELLOW, Colors.DEEP_GREEN]
    # bottles[6] = [Colors.PURPLE, Colors.BLUE, Colors.YELLOW, Colors.YELLOW]
    # bottles[7] = [Colors.GREEN, Colors.GREEN, Colors.BLUE, Colors.BLUE]
    # bottles[8] = [Colors.RED, Colors.RED, Colors.DEEP_GREEN, Colors.SHIT_YELLOW]

    # Level 14
    # bottles[2] = [Colors.DEEP_GREEN, Colors.BLUE, Colors.YELLOW, Colors.GREEN]
    # bottles[3] = [Colors.SHIT_YELLOW, Colors.RED, Colors.BLUE, Colors.BLUE]
    # bottles[4] = [Colors.RED, Colors.PURPLE, Colors.BLUE, Colors.SHIT_YELLOW]
    # bottles[5] = [Colors.RED, Colors.YELLOW, Colors.RED, Colors.DEEP_GREEN]
    # bottles[6] = [Colors.GREEN, Colors.GREEN, Colors.SHIT_YELLOW, Colors.GREEN]
    # bottles[7] = [Colors.SHIT_YELLOW, Colors.DEEP_GREEN, Colors.PURPLE, Colors.PURPLE]
    # bottles[8] = [Colors.YELLOW, Colors.YELLOW, Colors.PURPLE, Colors.DEEP_GREEN]

    # Level 16
    # bottles[2] = [Colors.BLUE, Colors.PURPLE, Colors.GREEN, Colors.RED]
    # bottles[3] = [Colors.SHIT_YELLOW, Colors.RED, Colors.BLUE, Colors.YELLOW]
    # bottles[4] = [Colors.SHIT_YELLOW, Colors.GREEN, Colors.YELLOW, Colors.YELLOW]
    # bottles[5] = [Colors.SHIT_YELLOW, Colors.BLUE, Colors.GREEN, Colors.YELLOW]
    # bottles[6] = [Colors.DEEP_GREEN, Colors.DEEP_GREEN, Colors.RED, Colors.PURPLE]
    # bottles[7] = [Colors.PURPLE, Colors.SHIT_YELLOW, Colors.BLUE, Colors.GREEN]
    # bottles[8] = [Colors.PURPLE, Colors.DEEP_GREEN, Colors.RED, Colors.DEEP_GREEN]

    # Level 200
    # bottles[2] = [Colors.DEEP_GREEN, Colors.PURPLE, Colors.GREEN, Colors.PINK]
    # bottles[3] = [Colors.SHALLOW_BLUE, Colors.BROWN, Colors.DEEP_GREEN, Colors.RED]
    # bottles[4] = [Colors.BLUE, Colors.SKY_BLUE, Colors.SHALLOW_BLUE, Colors.SKY_BLUE]
    # bottles[5] = [Colors.BLUE, Colors.PINK, Colors.YELLOW, Colors.DEEP_GREEN]
    # bottles[6] = [Colors.ORANGE, Colors.SHIT_YELLOW, Colors.YELLOW, Colors.YELLOW]
    # bottles[7] = [Colors.BLUE, Colors.SHALLOW_BLUE, Colors.GREEN, Colors.GREEN]
    # bottles[8] = [Colors.BLUE, Colors.SHIT_YELLOW, Colors.SKY_BLUE, Colors.RED]
    # bottles[9] = [Colors.DEEP_GREEN, Colors.SHIT_YELLOW, Colors.BROWN, Colors.GREEN]
    # bottles[10] = [Colors.PURPLE, Colors.SHALLOW_BLUE, Colors.ORANGE, Colors.RED]
    # bottles[11] = [Colors.PURPLE, Colors.RED, Colors.ORANGE, Colors.SKY_BLUE]
    # bottles[12] = [Colors.PURPLE, Colors.SHIT_YELLOW, Colors.YELLOW, Colors.BROWN]
    # bottles[13] = [Colors.ORANGE, Colors.BROWN, Colors.PINK, Colors.PINK]

    # Level 201
    # bottles[2] = [Colors.BLUE, Colors.ORANGE, Colors.PURPLE, Colors.SKY_BLUE]
    # bottles[3] = [Colors.SKY_BLUE, Colors.PURPLE, Colors.SKY_BLUE, Colors.DEEP_GREEN]
    # bottles[4] = [Colors.GREEN, Colors.GREEN, Colors.ORANGE, Colors.RED]
    # bottles[5] = [Colors.YELLOW, Colors.GREEN, Colors.SHIT_YELLOW, Colors.SKY_BLUE]
    # bottles[6] = [Colors.YELLOW, Colors.RED, Colors.BLUE, Colors.SHIT_YELLOW]
    # bottles[7] = [Colors.ORANGE, Colors.BLUE, Colors.RED, Colors.PURPLE]
    # bottles[8] = [Colors.YELLOW, Colors.BLUE, Colors.DEEP_GREEN, Colors.SHIT_YELLOW]
    # bottles[9] = [Colors.YELLOW, Colors.DEEP_GREEN, Colors.SHIT_YELLOW, Colors.ORANGE]
    # bottles[10] = [Colors.DEEP_GREEN, Colors.GREEN, Colors.PURPLE, Colors.RED]

    # Level 202
    bottles[2] = [Colors.PINK, Colors.SHIT_YELLOW, Colors.YELLOW, Colors.YELLOW]
    bottles[3] = [Colors.YELLOW, Colors.SHIT_YELLOW, Colors.SHALLOW_BLUE, Colors.SKY_BLUE]
    bottles[4] = [Colors.ORANGE, Colors.BLUE, Colors.SKY_BLUE, Colors.GREEN]
    bottles[5] = [Colors.DEEP_GREEN, Colors.DEEP_GREEN, Colors.ORANGE, Colors.PURPLE]
    bottles[6] = [Colors.DEEP_GREEN, Colors.GREEN, Colors.SHIT_YELLOW, Colors.PINK]
    bottles[7] = [Colors.DEEP_GREEN, Colors.PINK, Colors.RED, Colors.SHIT_YELLOW]
    bottles[8] = [Colors.PURPLE, Colors.BLUE, Colors.GREEN, Colors.SKY_BLUE]
    bottles[9] = [Colors.BLUE, Colors.BLUE, Colors.GREEN, Colors.ORANGE]
    bottles[10] = [Colors.PINK, Colors.SKY_BLUE, Colors.SHALLOW_BLUE, Colors.BROWN]
    bottles[11] = [Colors.SHALLOW_BLUE, Colors.BROWN, Colors.ORANGE, Colors.PURPLE]
    bottles[12] = [Colors.RED, Colors.YELLOW, Colors.RED, Colors.RED]
    bottles[13] = [Colors.BROWN, Colors.PURPLE, Colors.SHALLOW_BLUE, Colors.BROWN]

    for i in range(N_BOTTLES):
        _bottle = Bottle(i, bottles[i])
        global_board.append(_bottle)

    return global_board


if __name__ == '__main__':
    start_board = get_start_board()

    for bottle in start_board:
        print(bottle.number, bottle.data)