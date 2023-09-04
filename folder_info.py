import os

from file_info import FileInfo
from helper.helper import *


class FolderInfo:
    def __init__(self,
                 path: str = None,
                 author_name: str = None,
                 genre: str = None,
                 output_format: str = None):

        self.path: str = path
        self.album_name: str = ""
        self.author_name: str = author_name
        self.genre: str = genre
        self.output_format: str = output_format
        self.files = []

    def gather_info(self):
        try:
            self.update_path()
            self.update_author_name()
            self.update_genre()
            self.update_output_format()
            self.insert_files()
        except Exception as ex:
            print(ex)
        finally:
            self.album_name = get_folder_name(self.path)
            insert_linebreak()

    def gather_info_to_images_only(self):
        try:
            self.update_path()
            self.insert_files()
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def update_path(self):
        try:
            print("Inform the full path to the folder that is desired to convert the files")
            self.path = str(input(" > "))
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def update_author_name(self):
        try:
            print("If you want, enter the name of the artist")
            print("otherwise, press \'Enter\'")
            self.author_name = str(input(" > "))
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def update_genre(self):
        try:
            print("If you want, enter the music genre")
            print("otherwise, press \'Enter\'")
            self.genre = str(input(" > "))
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def update_output_format(self):
        try:
            print("If you want, enter the output file format (file extension)")
            print("Default output format: FLAC")
            print("TYPE THE FORMAT WITHOUT THE DOT")
            print("otherwise, press \'Enter\'")
            self.output_format = str(input(" > ") or "flac")
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def refresh_file_sort(self):
        try:
            self.files = []
            self.insert_files()
        except Exception as ex:
            print(ex)
        finally:
            insert_linebreak()

    def insert_files(self):
        try:
            files = os.listdir(self.path)
            track_num = 1

            for file in files:
                file_extension = get_file_extension(file)

                if file_extension == ".png":
                    continue

                file_title = file.replace(file_extension, '')

                self.files.append(FileInfo(track_num, file, file_title, file_extension))
                track_num = track_num + 1
        except Exception as ex:
            print(ex)
