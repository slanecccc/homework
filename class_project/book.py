class Book:
    def __init__(self, title_book: str, year_release: int, publisher: str,
                 genre: str, author: str, price: int):
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