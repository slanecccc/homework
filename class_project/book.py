class Author:
    def __init__(self, full_name: str, year_birth: str, birthplace: str):
        self. full_name = full_name
        self.year_birth = year_birth
        self.birthplace = birthplace

    def __str__(self):
        return f"{self.full_name} \n" \
               f" - Дата рождения: {self.year_birth} \n" \
               f" - Место рождения: {self.birthplace} "


class Book:
    def __init__(self, title_book: str, year_release: int, publisher: str,
                 genre: str, author: Author, price: int):
        self.title = title_book
        self.release = year_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"Название книги: {self.title} \n" \
               f"Год выпуска: {self.release} \n" \
               f"Издатель: {self.publisher} \n" \
               f"Жанр: {self.genre} \n" \
               f"Автор: {self.author} \n" \
               f"Цена: {self.price} руб."