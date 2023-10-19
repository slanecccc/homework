from class_project.human import *
from class_project.book import *


def main():

    full_name = FullName("Горячев", "Константин", "Сергеевич")
    home_address = HomeAddress("Россия", "Ярославль", "Ньютона", 49, 5)
    person = Person(full_name, "30.12.1999", "+7(905)556-43-43", home_address)
    print(person)

    book = Book("Колобок", 1999, "Ромашка", "Ужасы", "Толстой А.Н.", 99999)
    print(book)


if __name__ == '__main__':
    main()