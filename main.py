from class_project.module_class import *


def main():
    manufacturer = Manufacturer("Ford", "США")
    try:
        auto = Automobile("Camaro", 1999, manufacturer, 150.5, "Красный", 10000000)
    except ValueError as e:
        print(e)
    else:
        print(auto)

    try:
        stadium = Stadium("Динамо", 2000, "Россия", "Ростов", 50000)
    except ValueError as e:
        print(e)
    else:
        print(stadium)


if __name__ == '__main__':
    main()
