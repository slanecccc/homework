from copy import deepcopy


class Manufacturer:
    def __init__(self, title: str, country: str) -> None:
        self.title = title
        self.country = country

    def __str__(self) -> str:
        return f"- Название производителя: {self.title} \n" \
               f" - Страна производитель: {self.country}"


class Automobile:
    def __init__(self, car_brand: str, year_release: int, manufacturer: Manufacturer,
                 engine_capacity: float | int, colour: str, price: int) -> None:
        self.car_brand = car_brand
        if year_release <= 1980:
            raise ValueError("Машина не может быть старше 1980 года выпуска")
        self.year_release = year_release
        self.manufacturer = deepcopy(manufacturer)
        self.engine_capacity = engine_capacity
        self.colour = colour
        self.price = price

    def __str__(self) -> str:
        return f"Название модели: {self.car_brand} \n" \
               f"Год выпуска: {self.year_release} \n" \
               f"Производитель: \n {self.manufacturer} \n" \
               f"Объем двигателя: {self.engine_capacity} л. \n" \
               f"Цвет машины: {self.colour} \n" \
               f"Цена машины: {self.price} руб."


class Stadium:
    def __init__(self, title: str, opening_date: int, country: str, city: str, capacity: int) -> None:
        self.title = title
        if opening_date <= 1940:
            raise ValueError("Стадион не должен быть построен раньше 1940 года ")
        self.opening_date = opening_date
        self.country = country
        self.city = city
        if capacity <= 3000:
            raise ValueError("Вместимость стадиона не может быть менее 3000 человек")
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Название стадиона: {self.title} \n" \
               f"Дата открытия: {self.opening_date} г. \n" \
               f"Страна: {self.country} \n" \
               f"Город: {self.city} \n" \
               f"Вместимость: {self.capacity} человек"
