"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

symbols = [
    '!', '@', '#', '$', '%', '&', '*', '+',
    '?', '/', '=', '<', '>', '^', '~', '|',
    ':', ';', '[', ']', '{', '}', '(', ')',
    '-', '_', '.', ',', 'A', 'B', 'C', 'D'
]

tiles = symbols * 2


state = {'mark': None, 'taps': 0}
hide = [True] * 64


def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    state['taps'] += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 26, 'normal'))    
        up()
    goto(-200,200)
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 14, 'bold'))

    if not any(hide):
        up()
        goto(0,0)
        color('green')
        write("Juego terminado", align="center", font=('Arial', 30, 'bold'))


    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
