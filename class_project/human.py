class FullName:
    def __init__(self, name: str, surname: str, patronymic: str) -> None:
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.patronymic}"


class HomeAddress:
    def __init__(self, street: str, house_number: int, flat: int):
        self.street = street
        self.house = house_number
        self.flat = flat

    def __str__(self) -> str:
        return f"ул.{self.street} д.{self.house} кв.{self.flat}"


class Person:
    def __init__(self, full_name: FullName, date_birth: str, phone: str, country: str,
                 city: str, home_address: HomeAddress):
        self.name = full_name
        self.birth = date_birth
        self.phone = phone
        self.country = country
        self.city = city
        self.address = home_address

    def __str__(self):
        return f"ФИО: {self.name} \n" \
               f"Дата рождения: {self.birth} \n" \
               f"Контактный телелефон: {self.phone} \n" \
               f"Страна: {self.country} \n" \
               f"Город: {self.city} \n" \
               f"Домашний адресс: {self.address}"