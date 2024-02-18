from class_project.human import *
from class_project.book import *


def main():
    try:
        full_name = FullName("Горячев", "Константин", "Сергеевич")
        person = Person(full_name, 30, "+7(905)556-43-43")
        person1 = person.add_birth_day(full_name, "1999-12-30", "+7(905)556-43-43")
        book = Book("Колобок", 1999, "Ужасы")
        # book.add_type_book()
        book1 = Book.add_file_book("book.txt")
        book1.make_eBook()

    except ValueError as e:
        print(e)
    else:
        print(book.type_book)
        print(book1.type_book)
        print(book1)


if __name__ == '__main__':
    main()