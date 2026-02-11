from typing import TextIO

class File:
    '''Контекст менеджер который открывает файл и закрывает по завершению работы с ним'''
    def __init__(self, path: str, mode: str, enc: str='utf-8'):
        self.path = path
        self.mode = mode
        self.enc = enc
        self.file = None


    def __enter__(self) -> TextIO:
        self.file = open(self.path, self.mode, encoding=self.enc)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if exc_type is TypeError:
            print('Файл не записан передан неверный тип данных!')
            return True
        return False

with File("test_2.txt", 'r') as f:#Почему open  с маленькой а у нас с большой?
    text = f.read()
    print(text)

with File("test_2.txt", 'a') as f:
    f.write(5)

with File("test_2.txt", 'r') as f:
    text = f.read()
    print(text)