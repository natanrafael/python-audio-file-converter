from builder.command import Command
from builder.interface import BuilderInterface


class Builder(BuilderInterface):
    def __init__(self) -> None:
        self._command = None
        self.reset()

    def reset(self) -> None:
        self._command = Command()

    @property
    def command(self) -> Command:
        command = self._command
        self.reset()
        return command

    def add_ffmpeg(self, letter: str, complement: str = ""):
        # ffmpeg -f flac
        # ffmpeg -i
        self._command.add("ffmpeg -" + letter + " " + complement)

    def add_file_info(self, input: str, complement: str = ""):
        # add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_full_name))
        # add_backslash_to_special_character(concat_dir(folder_info.path, "temp.flac"))
        # add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_title + ".flac"))
        self._command.add(complement + " \'" + input + "\'")

    def remove_file(self, input: str):
        self._command.add("rm -fo \'" + input + "\'")

    def add_title_metadata(self, file_title: str):
        # file_info.file_title
        self._command.add("-metadata title=\"" + file_title + "\"")

    def add_artist_metadata(self, author_name: str):
        # folder_info.author_name
        self._command.add("-metadata artist=\"" + author_name + "\"")

    def add_album_metadata(self, album_name: str):
        # folder_info.album_name
        self._command.add("-metadata album=\"" + album_name + "\"")

    def add_album_artist_metadata(self, author_name: str):
        # folder_info.author_name
        self._command.add("-metadata album_artist=\"" + author_name + "\"")

    def add_genre_metadata(self, genre: str):
        # folder_info.genre
        self._command.add("-metadata genre=\"" + genre + "\"")

    def add_track_num_metadata(self, track_num: int):
        # file_info.track_num
        self._command.add("-metadata track=\"" + str(track_num) + "\"")

    def add_mapping(self):
        self._command.add("-map 1 -map 0:a -c copy")
        self._command.add("-metadata:s:v title=\"Album cover\"")
        self._command.add("-disposition:v attached_pic")

    def add_image_info(self, image_output: str):
        # add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_title + '.flac'))
        self._command.add("-f flac \'" + image_output + "\'")

    def add_command_division(self):
        self._command.add(";")

    def add_custom_command(self, custom):
        self._command.add(custom)