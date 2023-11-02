
class ConvertTemperature:
    # Константы для формулы преобразования градусов Цельсия(С) в Фаренгейта(F) и наоборот
    __A = 32
    __B = 1.8
    # Константа для формулы преобразования градусов Цельсия(С) в Кальвина(К) и наоборот
    __K = 273.15
    # Константа для формулы преобразования градусов Фаренгейта(F) в Кальвина(К) и наоборот
    __F = 459.67

    @staticmethod
    def cel_to_far(degrees: float):
        return f"{degrees * ConvertTemperature.__B + ConvertTemperature.__A} F"