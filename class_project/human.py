from copy import deepcopy


class FullName:
    def __init__(self, name: str, surname: str, patronymic: str) -> None:
        self.__name = self.__validate_name(name)
        self.__surname = self.__validate_name(surname)
        self.__patronymic = self.__validate_name(patronymic)

    def __str__(self) -> str:
        return f"{self.__name} {self.__surname} {self.__patronymic}"

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValueError("ФИО не может быть пустым")
        return name


class HomeAddress:
    def __init__(self, country: str, city: str, street: str, house_number: int, flat: int):
        self.__country = self.__validate_place(country)
        self.__city = self.__validate_place(city)
        self.__street = self.__validate_place(street)
        self.__house = self.__validate_number(house_number)
        self.__flat = self.__validate_number(flat)

    def __str__(self) -> str:
        return f"{self.__country}, г. {self.__city}, ул.{self.__street}, д.{self.__house}, кв.{self.__flat}"

    @staticmethod
    def __validate_place(place: str):
        if len(place) == 0:
            raise ValueError("Есть не заполненные поля домашнего адреса")

        return place

    @staticmethod
    def __validate_number(num: int):
        if num <= 0:
            raise " Номер дома и квартиры не может быть отрицательным или равен нулю"


class Person:
    def __init__(self, full_name: FullName, date_birth: str, phone: str, home_address: HomeAddress):
        self.__name = deepcopy(full_name)
        self.__birth = self.__validate_date(date_birth)
        self.__phone = self.__validate_phone(phone)
        self.__address = deepcopy(home_address)

    def __str__(self):
        return f"ФИО: {self.__name} \n" \
               f"Дата рождения: {self.__birth} \n" \
               f"Контактный телелефон: {self.__phone} \n" \
               f"Домашний адресс: {self.__address}"

    @staticmethod
    def __validate_date(date: str):
        if len(date) == 0:
            raise ValueError("Дата рождения не может быть пустым")
        return date

    @staticmethod
    def __validate_phone(phone: str):
        if len(phone) == 0:
            raise ValueError("Контактный телефон не может быть пустым")

        return phone
