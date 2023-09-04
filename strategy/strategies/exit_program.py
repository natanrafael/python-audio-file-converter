import sys

from strategy import Strategy


class ExitProgram(Strategy):
    def __init__(self, input_menu):
        self._input_menu = input_menu

    def execute_concrete_strategy(self):
        print("closing program.")
        sys.exit(0)
