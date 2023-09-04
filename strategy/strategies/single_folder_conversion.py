import os
import re
import subprocess

from builder.builder import Builder
from builder.director import Director
from folder_info import FolderInfo
from strategy import Strategy


class SingleFolderConversion(Strategy):
    def __init__(self, input_menu):
        self._input_menu = input_menu

    def execute_concrete_strategy(self):
        print("starting single folder conversion.")

        folder_info = FolderInfo()

        while True:
            if folder_info.path is not None:
                director = Director()
                builder = Builder()
                director.builder = builder

                exist_cover = os.path.exists(folder_info.path + "\\cover.png")

                if True:
                    nome_para_retirar = 'Diabolus in Musica, '

                    for file in folder_info.files:
                        novo_nome = file.file_full_name.replace(str(nome_para_retirar), '')
                        command = "Rename-Item -LiteralPath \"" + folder_info.path + "\\" + file.file_full_name + "\" -NewName \"" + novo_nome + "\""
                        subprocess.run(["powershell", "-Command", command], capture_output=False)

                if True:
                    p = re.compile('(?<!\S)\d{1}\..*')

                    for file in folder_info.files:
                        print(p.sub('0'+file.file_full_name, file.file_full_name))
                        novo_nome = p.sub('0'+file.file_full_name, file.file_full_name)
                        command = "Rename-Item -LiteralPath \"" + folder_info.path + "\\" + file.file_full_name + "\" -NewName \"" + novo_nome + "\""
                        subprocess.run(["powershell", "-Command", command], capture_output=False)

                    FolderInfo.refresh_file_sort(folder_info)

                for file in folder_info.files:
                    director.build_conversion_command_with_image(folder_info, file, exist_cover)
                    query = builder.command.prepare_command()
                    subprocess.run(["powershell", "-Command", query], capture_output=False)

                self._input_menu.show()
                choice = int(input("select an option > "))

                if choice == self._input_menu.index:
                    print('break')
                    break

                self._input_menu.execute_conversion_info_change(choice, folder_info)
            else:
                FolderInfo.gather_info(folder_info)
