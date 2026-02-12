from typing import TextIO, Optional

class File:
    """Контекст менеджер который открывает файл и закрывает по завершению работы с ним"""
    def __init__(self, path: str, mode: str, enc: str='utf-8') -> None:
        self.path = path
        self._mode = mode
        self.enc = enc
        self.file: Optional[TextIO] = None


    def __enter__(self) -> TextIO:
        """Магический метод для реализации контекстменеджера."""
        try:
            self.file = open(self.path, self.mode, encoding=self.enc)
        except FileNotFoundError:
            with open(self.path, "w", encoding=self.enc) as f:
                pass
            self.file = open(self.path, self.mode, encoding=self.enc)
        return self.file

    def __exit__(self, *args) -> bool:
        """Метод для закрытия файла
        *args - (exc_type, exc_val, exc_tb)"""
        if self.file:
            self.file.close()
        return True
        # if exc_type is TypeError:
        #     print('Файл не записан передан неверный тип данных!')
        #     return True
        # return False
    @property
    def mode(self) -> str:
        """Геттер для mode"""
        return self._mode

    @mode.setter
    def mode(self, mode) -> None:
        """Сеттер для mode"""
        if not isinstance(mode, str):
            raise TypeError("Режим должен быть строкой!")
        self._mode = mode



with File("test_2.txt", 'r') as f:
    text = f.read()
    print(text)

with File("test_2.txt", 'a') as f:
    f.write("5")

with File("test_2.txt", 'r') as f:
    text = f.read()
    print(text)