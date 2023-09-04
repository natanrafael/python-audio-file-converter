from folder_info import FolderInfo
from menu import build_menu
from strategy import Context
from strategy.strategies.exit_program import ExitProgram
from strategy.strategies.only_images_single_folder_conversion import OnlyImagesSingleFolderConversion
from strategy.strategies.single_folder_conversion import SingleFolderConversion


def recovery_initial_menu_dict_options():
    initial_menu_dict = {
        'Convert single folder': SingleFolderConversion(
            build_menu(
                recovery_single_folder_menu_dict_options()
            )
        ),
        'Convert single folder (Only images)': OnlyImagesSingleFolderConversion(
            build_menu(
                recovery_single_folder_only_images_menu_dict_options()
            )
        ),
        'Exit Program': ExitProgram(None)
    }

    return initial_menu_dict


def recovery_single_folder_menu_dict_options():
    single_folder_menu_dict = {
        'Update path information': FolderInfo.update_path,
        'Update author name information': FolderInfo.update_author_name,
        'Update genre information': FolderInfo.update_genre,
        'Update output format information': FolderInfo.update_output_format,
        'Return to initial Menu': ''
    }

    return single_folder_menu_dict


def recovery_single_folder_only_images_menu_dict_options():
    simple_single_folder_menu_dict = {
        'Update path information': FolderInfo.update_path,
        'Return to initial Menu': ''
    }

    return simple_single_folder_menu_dict


def initialize_menu(input_menu):
    while True:
        input_menu.show()
        choice_index = int(input("select an option > "))

        if choice_index > input_menu.index:
            print("SELECT A VALID OPTION FROM THE MENU")
            continue

        context = Context()
        choice = input_menu.call_strategy(choice_index)

        if context.strategy is not None:
            context.strategy = choice
        else:
            context = Context(choice)

        context.execute_strategy()


def check_ffmpeg():
    import shutil
    path_ffmpeg = shutil.which('ffmpeg')

    if path_ffmpeg is not None:
        return True

    print("FFmpeg is mandatory for this code to work")
    print("https://www.gyan.dev/ffmpeg/builds/")
    print("INSTALL ANY version of it, and make sure that the package is accessible via CMD/Powershell")
    print("Remember to add it to the 'Path' environment variable of the OS.")
    print("")
    print("PS. is intended to make the code do it automatically in future versions.")

    return False


if __name__ == "__main__":
    ffmpeg_exists = check_ffmpeg()
    if ffmpeg_exists:
        initial_menu = build_menu(recovery_initial_menu_dict_options())
        initialize_menu(initial_menu)
    else:
        print("The code can't continue without ffmpeg installed and properly configured.")
