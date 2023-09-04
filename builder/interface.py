from abc import ABC, abstractmethod


class BuilderInterface(ABC):
    @property
    def command(self) -> None:
        pass

    @abstractmethod
    def add_ffmpeg(self, letter: str, complement: str = ""):
        pass

    @abstractmethod
    def add_file_info(self, input: str, complement: str = ""):
        pass

    @abstractmethod
    def add_title_metadata(self, file_title: str):
        pass

    @abstractmethod
    def add_artist_metadata(self, author_name: str):
        pass

    @abstractmethod
    def add_album_metadata(self, album_name: str):
        pass

    @abstractmethod
    def add_album_artist_metadata(self, author_name: str):
        pass

    @abstractmethod
    def add_genre_metadata(self, genre: str):
        pass

    @abstractmethod
    def add_track_num_metadata(self, track_num: int):
        pass

    @abstractmethod
    def add_mapping(self):
        pass

    @abstractmethod
    def add_image_info(self, image_output: str):
        pass

    @abstractmethod
    def add_command_division(self):
        pass

    @abstractmethod
    def remove_file(self, input: str):
        pass

    @abstractmethod
    def add_custom_command(self, custom):
        pass
