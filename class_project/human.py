from copy import deepcopy


class FullName:
    def __init__(self, name: str, surname: str, patronymic: str) -> None:
        self.__name: str = self.__validate_name(name)
        self.__surname: str = self.__validate_name(surname)
        self.__patronymic: str = self.__validate_name(patronymic)

    def __str__(self) -> str:
        return f"{self.__name} {self.__surname} {self.__patronymic}"

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValueError("ФИО не может быть пустым")
        return name


class Person:
    def __init__(self, full_name: FullName, age: int, phone: str) -> None:
        self.__name: FullName = deepcopy(full_name)
        self.__age: int = age
        self.__phone: str = self.__validate_phone(phone)

    def __str__(self):
        return f"ФИО: {self.__name} \n" \
               f"Возраст: {self.__age} \n" \
               f"Контактный телефон: {self.__phone} \n" \


    @classmethod
    def add_birth_day(cls, full_name: FullName, birth_day: str, phone: str):
        return cls(deepcopy(full_name), birth_day, phone)

    @staticmethod
    def __validate_date(date: int):
        if date <= 0:
            raise ValueError("Возраст не может быть равен нулю или быть отрицательным")
        return date

    @staticmethod
    def __validate_phone(phone: str):
        if len(phone) == 0:
            raise ValueError("Контактный телефон не может быть пустым")

        return phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        if len(phone) == 0:
            raise "Контактный телефон не может быть пустым"
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: FullName):
        if not isinstance(name, FullName):
            raise ValueError("Не верное ФИО.")
        self.__name = deepcopy(name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age
