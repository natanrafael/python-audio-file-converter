from builder.interface import BuilderInterface
from file_info import FileInfo
from folder_info import FolderInfo
from helper.helper import add_backslash_to_special_character, concat_dir


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderInterface:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderInterface) -> None:
        self._builder = builder

    def build_conversion_command_with_image(self, folder_info: FolderInfo, file_info: FileInfo, exist_cover):
        self.builder.add_ffmpeg("i")
        self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_full_name)))
        self.builder.add_title_metadata(file_info.file_title)
        self.builder.add_artist_metadata(folder_info.author_name)
        self.builder.add_album_metadata(folder_info.album_name)
        self.builder.add_album_artist_metadata(folder_info.author_name)
        self.builder.add_genre_metadata(folder_info.genre)
        self.builder.add_track_num_metadata(file_info.track_num)

        if exist_cover:
            self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, "temp." + folder_info.output_format)))
        else:
            self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_title + '.' + folder_info.output_format)))

        self.builder.add_command_division()

        self.builder.add_custom_command("mv " + file_info.file_full_name.replace(file_info.file_extension, "." + folder_info.output_format) + " " + file_info.file_full_name.replace(file_info.file_extension, '.flac.old'))

        self.builder.add_command_division()

        if exist_cover:
            self.builder.add_ffmpeg("f", folder_info.output_format)
            self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, "temp." + folder_info.output_format)), "-i")
            self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, "cover.png")), "-i")
            self.builder.add_mapping()
            self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_title + '.' + folder_info.output_format)), "-f flac")

            self.builder.add_command_division()

        self.builder.remove_file(add_backslash_to_special_character(concat_dir(folder_info.path, "temp." + folder_info.output_format)))

        self.builder.add_command_division()

        self.builder.remove_file(add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_full_name)))

    def build_conversion_command_without_image(self, folder_info: FolderInfo, file_info: FileInfo):
        self.builder.add_custom_command("Rename-Item "
                                        "\'" + add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_full_name)) + "\' "
                                        "\'temp.old\'")

        self.builder.add_command_division()

        self.builder.add_ffmpeg("f", file_info.file_extension[1:])
        self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, "temp.old")), "-i")
        self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, "cover.png")), "-i")
        self.builder.add_mapping()
        self.builder.add_custom_command("-f " + file_info.file_extension[1:])
        self.builder.add_file_info(add_backslash_to_special_character(concat_dir(folder_info.path, file_info.file_title + file_info.file_extension)))

        self.builder.add_command_division()

        self.builder.remove_file(add_backslash_to_special_character(concat_dir(folder_info.path, "temp.old")))
