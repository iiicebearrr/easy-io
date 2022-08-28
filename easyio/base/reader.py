from pathlib import Path


class EasyReaderBase:

    def __init__(self, file_path: str, *args, **kwargs):
        if not self.is_file_exists(file_path):
            raise IOError(f"No such file: {file_path}")

        self.file_path = file_path

    @staticmethod
    def is_file_exists(file_path: str):
        file_object = Path(file_path)
        return file_object.exists() and file_object.is_file()
