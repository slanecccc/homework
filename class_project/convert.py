
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

    @staticmethod
    # Преобразование градусов Цельсия в Кельвина
    def cel_to_cal(degrees: float):
        return f"{degrees + ConvertTemperature.__K} K"

    @staticmethod
    # Преобразование градусов Кельвина в Цельсия
    def cal_to_cel(degrees: float):
        return f"{degrees - ConvertTemperature.__K} C"

    @staticmethod
    # Преобразование градусов Фаренгейта в Кельвина
    def far_to_cal(degrees: float):
        return f"{(degrees + ConvertTemperature.__F) / ConvertTemperature.__B} K"

    @staticmethod
    # Преобразование градусов Кельвина В Фаренгейта
    def cal_to_far(degrees:  float):
        return f"{degrees * ConvertTemperature.__B - ConvertTemperature.__F} F"
