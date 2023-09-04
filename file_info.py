from helper.helper import get_file_extension


class FileInfo:
    def __init__(self, track_num, file_full_name, file_title, file_extension):
        self.track_num = track_num
        self.file_full_name = file_full_name
        self.file_title = file_title
        self.file_extension = get_file_extension(file_full_name)
