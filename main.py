#!/usr/bin/env python3

from logic import Game
import curses
from time import sleep


class RenderGame:
    def __init__(self, src):
        self.screen = src
        self.game = Game()
        self.row = 0

    def draw_field(self):
        field = self.game.get_field()
        self.row = 0
        self.screen.erase()
        self.screen.addstr(self.row, 0, "Score: {}".format(self.game.get_score()))
        self.row += 1

        cell_width = len(str(max(
            cell
            for row in field
            for cell in row
        )))

        for row in field:
            self.screen.addstr(self.row, 0, "{}".format(' '.join(str(cell).rjust(cell_width) for cell in row)))
            self.row += 2
        self.row += 2
        self.screen.refresh()

    def render(self):
        while self.game.has_moves():
            self.draw_field()
            self.get_keys()
        print('Game Over!')
        self.stop_game(True)

    def get_keys(self):
        while True:
            try:
                key_code = self.screen.getch()
            except (EOFError, KeyboardInterrupt):
                break
            if 0 < key_code < 256:
                key = chr(key_code)
                if key in "wW":
                    self.game.move_up()
                    break
                elif key in "Ss":
                    self.game.move_down()
                    break
                elif key in "aA":
                    self.game.move_left()
                    break
                elif key in "dD":
                    self.game.move_right()
                    break
                elif key in 'Qq':
                    self.stop_game()
                    break
            if key_code == curses.KEY_UP:
                self.game.move_up()
                break
            elif key_code == curses.KEY_DOWN:
                self.game.move_down()
                break
            elif key_code == curses.KEY_LEFT:
                self.game.move_left()
                break
            elif key_code == curses.KEY_RIGHT:
                self.game.move_right()
                break

    def stop_game(self, game_over=False):
        curses.endwin()
        if game_over:
            print("Game Over")
        print("Score: ", self.game.get_score())
        print("Bye!")
        exit(0)


def main(screen):
    """
        Функция запуска игры
    """
    render = RenderGame(screen)
    render.render()


if __name__ == '__main__':
    curses.wrapper(main)
