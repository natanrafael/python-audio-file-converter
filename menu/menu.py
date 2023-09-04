from helper.helper import *
from strategy import Strategy


class Menu:
    def __init__(self):
        self._options = {}
        self.index = -1

    def add_item(self, call_name, strategy):
        self.index = self.index + 1
        self._options[self.index] = {'call_name': call_name, 'strategy': strategy}

    def show(self):
        add_title()

        for option in range(len(self._options)):
            print(option, " - ", self._options[option]['call_name'])

        insert_linebreak()

    def execute_conversion_info_change(self, n, obj):
        self._options[n]['strategy'](obj)

    def call_strategy(self, n):
        return self._options[n]['strategy']
