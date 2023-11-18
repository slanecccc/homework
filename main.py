from class_project.human import *
from class_project.book import *


def main():
    try:
        full_name = FullName("Горячев", "Константин", "Сергеевич")
        person = Person(full_name, 30, "+7(905)556-43-43")
        person1 = person.add_birth_day(full_name, "1999-12-30", "+7(905)556-43-43")
        autor = Author("Толстой А.Н.", "31.11.1812", "Россия")
        book = Book("Колобок", 1999, "Ромашка", "Ужасы", autor, 99999)
    except ValueError as e:
        print(e)
    else:
        print(person)
        print(person1)
        print(book)


if __name__ == '__main__':
    main()