from copy import deepcopy
from datetime import date
import re


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
        return cls(full_name, Person.__calc_age(cls.__validate_birth_day(birth_day)), phone)

    @staticmethod
    def __calc_age(birth_day: str):
        current_day = date.today()  # Текущая дата в формате
        data = list(map(int, birth_day.split("-")))
        birth_day = date(*data)
        if birth_day.month < current_day.month:
            return current_day.year - birth_day.year
        elif birth_day.month > current_day.month:
            return current_day.year - birth_day.year - 1
        elif birth_day.month == current_day.month:
            if birth_day.day <= current_day.day:
                return current_day.year - birth_day.year
            elif birth_day.day > current_day.day:
                return current_day.year - birth_day.year - 1

    @staticmethod
    def __validate_birth_day(day: str):
        if re.match(r'\d{4}-(0[1-9]|1[1-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])',day):
            return day
        else:
            raise ValueError("Дата рождения введена некорректно. Формат должен быть ГГГГ-ММ-ДД")


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
