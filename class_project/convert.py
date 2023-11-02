
class ConvertTemperature:
    # Константы для формулы преобразования градусов Цельсия(С) в Фаренгейта(F) и наоборот
    __A = 32
    __B = 1.8
    # Константа для формулы преобразования градусов Цельсия(С) в Кальвина(К) и наоборот
    __K = 273.15
    # Константа для формулы преобразования градусов Фаренгейта(F) в Кальвина(К) и наоборот
    __F = 459.67

    @staticmethod
    # Преобразования градусов Цельсия в Фаренгейты
    def cel_to_far(degrees: float):
        return f"{degrees * ConvertTemperature.__B + ConvertTemperature.__A} F"

    @staticmethod
    # Преобразование градусов Фаренгейта в градусы Цельсия
    def far_to_cel(degrees: float):
        return f"{(degrees - ConvertTemperature.__A) / ConvertTemperature.__B} C"
