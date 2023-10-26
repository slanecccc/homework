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


class HomeAddress:
    def __init__(self, country: str, city: str, street: str, house_number: int, flat: int):
        self.__country: str = self.__validate_place(country)
        self.__city: str = self.__validate_place(city)
        self.__street: str = self.__validate_place(street)
        self.__house: int = self.__validate_number(house_number)
        self.__flat: int = self.__validate_number(flat)

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
        return num


class Person:
    def __init__(self, full_name: FullName, date_birth: str, phone: str, home_address: HomeAddress):
        self.__name: FullName = deepcopy(full_name)
        self.__birth: str = self.__validate_date(date_birth)
        self.__phone: str = self.__validate_phone(phone)
        self.__address: HomeAddress = deepcopy(home_address)

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

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        if len(phone) == 0:
            raise "Контактный телефон не может быть пустым"
        self.__phone = phone

    @property
    def home_address(self):
        return self.__address

    @home_address.setter
    def home_address(self, home: HomeAddress):
        if not isinstance(home, HomeAddress):
            raise ValueError("Не верный адрес. Введите в формате: страна, город, улица, дом, квартира.")
        self.__address = home

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: FullName):
        if not isinstance(name, FullName):
            raise ValueError("Не верное ФИО.")
        self.__name = name

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, birth: str):
        self.__birth = birth