from typing import Union


class Seconds2human:

    def __init__(self, seconds: Union[int, float]):
        self.days = seconds // 86400
        seconds -= self.days * 86400
        self.hours = seconds // 3600
        seconds -= self.hours * 3600
        self.minutes = seconds // 60
        seconds -= self.minutes * 60
        self.seconds = seconds
        self.string = " ".join(filter(None, (self.__get_times(self.days, 'd'),
                                             self.__get_times(self.hours, 'h'),
                                             self.__get_times(self.minutes, 'm'),
                                             self.__get_times(self.seconds, 's'))))

    def __str__(self) -> str:
        return self.string

    @staticmethod
    def __get_times(digit: Union[int, float], tm: str) -> str:
        digit = round(digit)
        times = {'d': ['дней', 'день', 'дня'],
                 'h': ['часов', 'час', 'часа'],
                 'm': ['минут', 'минута', 'минуты'],
                 's': ['секунд', 'секунда', 'секунды']}

        if digit == 0:
            return ''
        tmp = digit % 100
        if 11 <= tmp <= 19:
            return f"{digit} {times[tm][0]}"
        tmp = digit % 10
        if tmp == 1:
            return f"{digit} {times[tm][1]}"
        if 2 <= tmp <= 4:
            return f"{digit} {times[tm][2]}"
        if tmp == 0 or 5 <= tmp <= 9:
            return f"{digit} {times[tm][0]}"
        return f"{digit} {times[tm][2]}"


class Strtime2seconds:

    def __init__(self, string: str):
        chars = {'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1}
        self.seconds = 0

        if string.isdigit():
            self.seconds = int(string)

        tmp = []

        for char in string:
            if not char.isdigit() and not tmp:
                pass

            elif char.isdigit():
                tmp.append(char)

            elif char in chars.keys():
                self.seconds += int(''.join(tmp)) * chars[char]
                tmp.clear()

    def __str__(self) -> str:
        return str(self.seconds)


class StringMatch:

    def __init__(self, original_string: str, second_string: str, decorate: bool = False):
        try:
            from numpy.ma import zeros

        except ImportError:
            raise Exception("Numpy is not installed")

        original_string, second_string = original_string.lower(), second_string.lower()
        self.decorate = decorate

        rows = len(original_string) + 1
        cols = len(second_string) + 1
        distance = zeros((rows, cols), dtype=int)

        for i in range(1, rows):
            for k in range(1, cols):
                distance[i][0] = i
                distance[0][k] = k

        for col in range(1, cols):
            for row in range(1, rows):
                if original_string[row - 1] == second_string[col - 1]:
                    cost = 0
                else:
                    cost = 2
                distance[row][col] = min(distance[row - 1][col] + 1,
                                         distance[row][col - 1] + 1,
                                         distance[row - 1][col - 1] + cost)

        self.percent = round(float((((len(original_string) + len(second_string)) - distance[row][col]) /
                                    (len(original_string) + len(second_string))) * 100), 2)

    def __str__(self) -> str:
        if self.decorate:
            return "{} %".format(self.percent)
        else:
            return str(self.percent)
