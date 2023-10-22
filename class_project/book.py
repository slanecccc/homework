from copy import *
import re


class Author:
    def __init__(self, full_name: str, year_birth: str, birthplace: str):
        self.__full_name: str = self.__validate_name(full_name)
        self.__year_birth: str = self.__validate_year_birth(year_birth)
        self.__birthplace: str = self.__validate_place(birthplace)

    def __str__(self):
        return f"{self.__full_name} \n" \
               f" - Дата рождения: {self.__year_birth} \n" \
               f" - Место рождения: {self.__birthplace} "

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValueError("Имя автора не может быть пустым")
        return name

    @staticmethod
    def __validate_year_birth(year: str):
        val = re.match(r'([0-2]{1}[0-9]{1}|[3]{1}[0-1]{1})\.(0{1}[1-9]{1}|1{1}[0-2]{1})'
                       r'\.[1-2]{1}\d{3}', year)
        if val is None:
            raise ValueError("Не верно указана дата рождения. Пример ввода 12.12.1999")
        return year

    @staticmethod
    def __validate_place(place: str):
        if len(place) == 0:
            raise ValueError("Место рождения не может быть пустым")
        return place


class Book:
    def __init__(self, title_book: str, year_release: int, publisher: str,
                 genre: str, author: Author, price: int):
        self.__title: str = self.__validate_name_book(title_book)
        self.__release: int = self.__validate_year_release(year_release)
        self.__publisher: str = self.__validate_publisher(publisher)
        self.__genre: str = self.__validate_genre(genre)
        self.__author: Author = deepcopy(author)
        self.__price: int = self.__validate_price(price)

    def __str__(self):
        return f"Название книги: {self.__title} \n" \
               f"Год выпуска: {self.__release} \n" \
               f"Издатель: {self.__publisher} \n" \
               f"Жанр: {self.__genre} \n" \
               f"Автор: {self.__author} \n" \
               f"Цена: {self.__price} руб."

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
    def __validate_publisher(publisher: str):
        if len(publisher) == 0:
            raise ValueError("Издатель не может быть пустым")
        return publisher

    @staticmethod
    def __validate_genre(genre: str):
        if len(genre) == 0:
            raise ValueError("Жанр не может быть пустым")
        return genre

    @staticmethod
    def __validate_price(price: int):
        if price <= 0:
            raise ValueError("Цена не может быть отрицательной или равно нулю")
        return price
