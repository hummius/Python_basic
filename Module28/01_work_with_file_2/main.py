import io
import os


class File:
    """
    Класс контекст-менеджер для открытия файла

    Args:
        file_name: имя файла
        mode: режим открытия
    """
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'File':
        if os.path.exists(self.file_name):
            self.file = open(self.file_name, self.mode, encoding='utf-8')
        else:
            self.file = open(self.file_name, 'w', encoding='utf-8')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type in (FileExistsError, FileNotFoundError):
            print(f'Произошла ошибка {exc_type} {exc_val} {exc_tb}')
        return True
