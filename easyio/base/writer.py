from pathlib import Path


class EasyWriterBase:

    def __init__(self, file_content: bytes, *args, **kwargs):
        ...
