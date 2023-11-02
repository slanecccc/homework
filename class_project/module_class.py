from copy import deepcopy


class Manufacturer:
    def __init__(self, title: str, country: str) -> None:
        self.__title: str = title
        self.__country: str = country

    def __str__(self) -> str:
        return f"- Название производителя: {self.__title} \n" \
               f" - Страна производитель: {self.__country}"


class Automobile:
    def __init__(self, car_brand: str, year_release: int, manufacturer: Manufacturer,
                 engine_capacity: float | int, colour: str, price: int) -> None:
        self.__car_brand: str = car_brand
        self.__year_release: int = self.__validate_year_release(year_release)
        self.__manufacturer: Manufacturer = deepcopy(manufacturer)
        self.__engine_capacity: float | int = engine_capacity
        self.__colour: str = colour
        self.__price: int = price

    def __str__(self) -> str:
        return f"Название модели: {self.__car_brand} \n" \
               f"Год выпуска: {self.__year_release} \n" \
               f"Производитель: \n {self.__manufacturer} \n" \
               f"Объем двигателя: {self.__engine_capacity} л. \n" \
               f"Цвет машины: {self.__colour} \n" \
               f"Цена машины: {self.__price} руб."
    @staticmethod
    def __validate_year_release(year: int):
        if year < 1980:
            raise ValueError("Машина не может быть старше 1980 года выпуска")
        return year

    @property
    def car_brand(self):
        return self.__car_brand

    @car_brand.setter
    def car_brand(self, brand: str):
        self.__car_brand = brand

    @property
    def year_release(self):
        return self.__year_release

    @year_release.setter
    def year_release(self, year: int):
        self.__year_release = year

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: Manufacturer):
        if not isinstance(manufacturer, Manufacturer):
            raise ValueError("Не верно указан производитель")
        self.__manufacturer = deepcopy(manufacturer)

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine: float | int):
        self.__engine_capacity = engine

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.__price = price






class Stadium:
    def __init__(self, title: str, opening_date: int, country: str, city: str, capacity: int) -> None:
        self.__title = title
        self.__opening_date = self.__validate_opening_data(opening_date)
        self.__country = country
        self.__city = city
        self.__capacity = self.__validate_capacity(capacity)

    def __str__(self) -> str:
        return f"Название стадиона: {self.__title} \n" \
               f"Дата открытия: {self.__opening_date} г. \n" \
               f"Страна: {self.__country} \n" \
               f"Город: {self.__city} \n" \
               f"Вместимость: {self.__capacity} человек"

    @staticmethod
    def __validate_opening_data(data: int):
        if data <= 1940:
            raise ValueError("Стадион не должен быть построен раньше 1940 года ")
        return data

    @staticmethod
    def __validate_capacity(num: int):
        if num <= 3000:
            raise ValueError("Вместимость стадиона не может быть менее 3000 человек")
        return num

    @property
    def title_stadium(self):
        return self.__title

    @title_stadium.setter
    def title_stadium(self, title: str):
        self.__title = title

    @property
    def opening_data(self):
        return self.__opening_date

    @opening_data.setter
    def opening_data(self, data: int):
        self.__opening_date = self.__validate_opening_data(data)


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, num: int):
        self.__capacity = self.__validate_capacity(num)
