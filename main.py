# coding: utf-8
"""
MIT License

Copyright (c) 2017 Hajime Nakagami<nakagami@gmail.com>
Copyright (c) 2020 Claude SIMON (https://q37.info/s/rmnmqd49)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys,os

sys.path.append("./webcli")

if ('Q37_XPP' in os.environ):
  sys.path.append(os.path.join(os.environ["HOME"],"epeios/other/libs/webcli/PYH/webcli"))

from webcli import *

print("Hello!")
print("Nice to meet you,", input("What's your name? "), "!")
time.sleep(1.5)
print("Let's play",end="…")
time.sleep(1.5)
print(" REVERSI!","You play the cross (X)!",sep="\n\n")

# Below code comes from:
# https://gist.github.com/nakagami/7a7d799bd4bd4ad8fcea96135c4af179

import random
import itertools

EMPTY = 0
BLACK = -1
WHITE = 1

# http://uguisu.skr.jp/othello/5-1.html
WEIGHT_MATRIX = [
    [30, -12, 0, -1, -1, 0, -12, 30],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [30, -12, 0, -1, -1, 0, -12, 30],
]

class Reversi:
    def __init__(self, orig=None):
        self.board = []
        for i in range(8):
            self.board.append([EMPTY] * 8)

        self.board[3][3] = self.board[4][4] = BLACK
        self.board[4][3] = self.board[3][4] = WHITE

        # copy constructor
        if orig:
            assert isinstance(orig, Reversi)
            for i in range(8):
                for j in range(8):
                    self.board[i][j] = orig.board[i][j]

    def count(self, bwe):
        "Count pieces or empty spaces in the board"
        assert bwe in (BLACK, WHITE, EMPTY)
        n = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bwe:
                    n += 1
        return n

    def _has_my_piece(self, bw, x, y, delta_x, delta_y):
        "There is my piece in the direction of (delta_x, delta_y) from (x, y)."
        assert bw in (BLACK, WHITE)
        assert delta_x in (-1, 0, 1)
        assert delta_y in (-1, 0, 1)
        x += delta_x
        y += delta_y

        if x < 0 or x > 7 or y < 0 or y > 7 or self.board[x][y] == EMPTY:
            return False
        if self.board[x][y] == bw:
            return True
        return self._has_my_piece(bw, x, y, delta_x, delta_y)

    def reversible_directions(self, bw, x, y):
        "Can put piece on (x, y) ? Return list of reversible direction tuple"
        assert bw in (BLACK, WHITE)

        directions = []
        if self.board[x][y] != EMPTY:
            return directions

        for d in itertools.product([-1,1,0],[-1,1,0]):
            if d == (0, 0):
                continue
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx > 7 or ny < 0 or ny > 7 or self.board[nx][ny] != bw * -1:
                continue
            if self._has_my_piece(bw, nx, ny, d[0], d[1]):
                directions.append(d)
        return directions

    def _reverse_piece(self, bw, x, y, delta_x, delta_y):
        "Reverse pieces in the direction of (delta_x, delta_y) from (x, y) untill bw."
        assert bw in (BLACK, WHITE)

        x += delta_x
        y += delta_y
        assert self.board[x][y] in (BLACK, WHITE)

        if self.board[x][y] == bw:
            return

        self.board[x][y] = bw
        return self._reverse_piece(bw, x, y, delta_x, delta_y)

    def put(self, x, y, bw):
        """
        True: Put bw's piece on (x, y) and change board status.
        False: Can't put bw's piece on (x, y)
        """

        assert bw in (BLACK, WHITE)
        directions = self.reversible_directions(bw, x, y)
        if len(directions) == 0:
            return False
        self.board[x][y] = bw
        for delta in directions:
            self._reverse_piece(bw, x, y, delta[0], delta[1])
        return True


    def _calc_score(self, bw, weight_matrix):
        assert bw in (BLACK, WHITE)
        my_score = 0
        against_score = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bw:
                    my_score += weight_matrix[i][j]
                elif self.board[i][j] == bw * -1:
                    against_score += weight_matrix[i][j]
        return my_score - against_score

    def find_best_position(self, bw, weight_matrix):
        "Return the best next position."
        assert bw in (BLACK, WHITE)

        next_positions = {}
        for i in range(8):
            for j in range(8):
                reversi = Reversi(self)
                if reversi.put(i, j, bw):
                    next_positions.setdefault(
                        reversi._calc_score(bw, weight_matrix), []
                    ).append((i, j))
        if next_positions:
            next_position = random.choice(next_positions[max(next_positions)])
        else:
            next_position = None
        return next_position


#-------------------------------------------------------------------------------
BLACK_MARK = 'X'
WHITE_MARK = 'O'


def print_board(reversi):
    print('\n   a b c d e f g h \n  +-+-+-+-+-+-+-+-+')
    for i, row in enumerate(reversi.board):
        print(' %d|' % (i+1), end='')
        for r in row:
            print('{}|'.format({EMPTY: ' ', BLACK: BLACK_MARK, WHITE: WHITE_MARK}[r]), end='')
        print('\n  +-+-+-+-+-+-+-+-+')
    print()


def input_position(player):
    while True:
        s = input('{}? [a-h][1-8]'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
        if s == '' or (len(s) == 2 and s[0] in list('abcdefgh') and s[1] in list('12345678')):
            break
    if s == '':
        return None

    y, x = ord(s[0]) - 97, ord(s[1]) - 49
    #print('input_position=', x, y)
    return x, y


def print_position(player, xy):
    if xy is None:
        print('{}: skip'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
    else:
        print('{}: {}{}'.format(
            BLACK_MARK if player == BLACK else WHITE_MARK,
            chr(xy[1]+97),
            chr(xy[0]+49)
        ))


def start_game():
    reversi = Reversi()
    weight_matrix = WEIGHT_MATRIX

    player = BLACK
    while not (
        reversi.count(EMPTY) == 0 or
        reversi.count(BLACK) == 0 or
        reversi.count(WHITE) == 0
    ):
        print_board(reversi)
        xy = input_position(player)
        while xy and not reversi.put(xy[0], xy[1], player):
            xy = input_position(player)

        print_board(reversi)
        xy = reversi.find_best_position(player * -1, weight_matrix)
        if xy:
            reversi.put(xy[0], xy[1], player * -1)
        print_position(player * -1, xy)

    print_board(reversi)
    if reversi.count(player) > reversi.count(player * -1):
        print('You win!')
    elif reversi.count(player) < reversi.count(player * -1):
        print('You lose!')


if __name__ == "__main__":
  start_game()