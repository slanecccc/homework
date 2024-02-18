from copy import *


class Book:
    __instance_type_book = "Бумажный экземпляр"

    def __init__(self, title_book: str, year_release: int, genre: str) -> None:
        self.__title: str = self.__validate_name_book(title_book)
        self.__release: int = self.__validate_year_release(year_release)
        self.__genre: str = self.__validate_genre(genre)

    def __str__(self) -> str:
        return f"Название книги: {self.__title} \n" \
               f"Год выпуска: {self.__release} \n" \
               f"Жанр: {self.__genre}"
    
    @classmethod
    def add_file_book(cls, name_file: str):
        list_text = Book.__read_file_book(name_file)
        name_book = list_text[0]
        year_release = int(list_text[1])
        genre = list_text[2]
        return cls(name_book, year_release, genre)

    @property
    def type_book(self):
        return self.__instance_type_book

    def make_eBook(self):
        self.__instance_type_book = "Электронный экземпляр"

    @staticmethod
    def __read_file_book(name_file: str):
        try:
            with open(name_file, 'r', encoding= 'utf-8') as file:
                text = file.readlines()
                text = [word.rstrip("\n") for word in text]
        except FileNotFoundError:
            print(f"Данного файла {name_file} не существует")
        else:
            return text

    @staticmethod
    def __validate_name_book(book: str):
        if len(book) == 0:
            raise ValueError("Название книги не может быть пустым")
        return book

    @staticmethod
    def __validate_year_release(year: int):
        if year < 1455:
            raise ValueError("Год выпуска книги не может быть раньше 1455 года.")
        return year

    @staticmethod
    def __validate_genre(genre: str):
        if len(genre) == 0:
            raise ValueError("Жанр не может быть пустым")
        return genre

    @property
    def title_book(self):
        return self.__title

    @title_book.setter
    def title_book(self, title: str):
        self.__title = self.__validate_name_book(title)

    @property
    def year_release(self):
        return self.__release

    @year_release.setter
    def year_release(self, year: int):
        self.__release = self.__validate_year_release(year)

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = self.__validate_genre(genre)
