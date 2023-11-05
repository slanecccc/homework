
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
        return f"{round(degrees * ConvertTemperature.__B + ConvertTemperature.__A, 2)} F"

    @staticmethod
    # Преобразование градусов Фаренгейта в градусы Цельсия
    def far_to_cel(degrees: float):
        return f"{round((degrees - ConvertTemperature.__A) / ConvertTemperature.__B, 2)} C"

    @staticmethod
    # Преобразование градусов Цельсия в Кельвина
    def cel_to_cal(degrees: float):
        return f"{round(degrees + ConvertTemperature.__K, 2)} K"

    @staticmethod
    # Преобразование градусов Кельвина в Цельсия
    def cal_to_cel(degrees: float):
        return f"{round(degrees - ConvertTemperature.__K, 2)} C"

    @staticmethod
    # Преобразование градусов Фаренгейта в Кельвина
    def far_to_cal(degrees: float):
        return f"{round((degrees + ConvertTemperature.__F) / ConvertTemperature.__B, 2)} K"

    @staticmethod
    # Преобразование градусов Кельвина В Фаренгейта
    def cal_to_far(degrees:  float):
        return f"{round(degrees * ConvertTemperature.__B - ConvertTemperature.__F, 2)} F"

class ConvertLengthMeasures:
    __FOOT_CEN = 30.48  # 1 фут = 30.38 см
    __FOOT_MET = 0.3  # 1 фут = 0.3 м
    __INCH_CEN = 2.54  # 1 дюйм = 2.54
    __INCH_MET = 0.025  # 1 дюйм = 0.025 м
    __YARD_CEN = 91.44  # 1 ярд = 91.44 см
    __YARD_MET = 0.91  # 1 ярд = 0.91 м