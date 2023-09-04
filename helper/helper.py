import re


def get_file_extension(file):
    re.purge()
    pattern = "\.[0-9a-z]+$"
    regex = re.compile(pattern, re.IGNORECASE)

    try:
        return regex.search(file).group()
    except AttributeError:
        return regex.search(file)


def get_folder_name(path: str = ""):
    re.purge()
    pattern = "[a-zA-Zà-üÀ-Ü0-9 \-\.\']+$"
    regex = re.compile(pattern, re.IGNORECASE)

    try:
        return regex.search(path).group()
    except AttributeError:
        return regex.search(path)


def add_backslash_to_special_character(input):
    re.purge()
    pattern = '[\']'

    try:
        test = re.sub(pattern, '\'\'', input)
        return test
    except AttributeError:
        print(Exception)


def concat_dir(x, y):
    return str(x + "\\" + y)


def add_title():
    insert_linebreak()
    print("                    _ _            ______ _ _            _____                          _            ")
    print("     /\            | (_)          |  ____(_) |          / ____|                        | |           ")
    print("    /  \  _   _  __| |_  ___      | |__   _| | ___     | |     ___  _ ____   _____ _ __| |_ ___ _ __ ")
    print("   / /\ \| | | |/ _` | |/ _ \     |  __| | | |/ _ \    | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|")
    print("  / ____ \ |_| | (_| | | (_) |    | |    | | |  __/    | |___| (_) | | | \ V /  __/ |  | ||  __/ |   ")
    print(" /_/    \_\__,_|\__,_|_|\___/     |_|    |_|_|\___|     \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   ")
    insert_linebreak()


def insert_linebreak():
    print('\n')
