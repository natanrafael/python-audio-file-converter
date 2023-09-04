from menu.menu import Menu
from strategy import Context


def build_menu(options):
    initial_menu = Menu()

    for item in options:
        initial_menu.add_item(str(item), options[item])

    return initial_menu
