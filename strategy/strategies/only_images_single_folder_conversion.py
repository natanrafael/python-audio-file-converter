import subprocess

from builder.builder import Builder
from builder.director import Director
from folder_info import FolderInfo
from strategy import Strategy


class OnlyImagesSingleFolderConversion(Strategy):
    def __init__(self, input_menu):
        self._input_menu = input_menu

    def execute_concrete_strategy(self):
        print("starting single folder conversion (only images).")

        folder_info = FolderInfo()

        while True:
            if folder_info.path is not None:
                director = Director()
                builder = Builder()
                director.builder = builder

                for file in folder_info.files:
                    director.build_conversion_command_without_image(folder_info, file)
                    query = builder.command.prepare_command()
                    subprocess.run(["powershell", "-Command", query], capture_output=False)

                self._input_menu.show()
                choice = int(input("select an option > "))

                if choice == self._input_menu.index:
                    print('break')
                    break

                self._input_menu.execute_conversion_info_change(choice, folder_info)
            else:
                FolderInfo.gather_info_to_images_only(folder_info)


