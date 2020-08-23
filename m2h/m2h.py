import re
from typing import Union

RE_SIMPLE_STRING = re.compile(r"(\d+)+\s*([wdhmsндчмс])")
CHAR_TO_RU_STR = {'w': ('недель', 'неделя', 'недели'),
                  'd': ('дней', 'день', 'дня'),
                  'h': ('часов', 'час', 'часа'),
                  'm': ('минут', 'минута', 'минуты'),
                  's': ('секунд', 'секунда', 'секунды')}
CHAR_TO_SEC = {'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1,
               'н': 604800, 'д': 86400, 'ч': 3600, 'м': 60, 'с': 1}


def _get_times(digit: Union[int, float], tm: str) -> Union[str, None]:
    digit = round(digit)

    if digit == 0:
        return None
    tmp = digit % 100
    if 11 <= tmp <= 19:
        return f"{digit} {CHAR_TO_RU_STR[tm][0]}"
    tmp = digit % 10
    if tmp == 1:
        return f"{digit} {CHAR_TO_RU_STR[tm][1]}"
    if 2 <= tmp <= 4:
        return f"{digit} {CHAR_TO_RU_STR[tm][2]}"
    if tmp == 0 or 5 <= tmp <= 9:
        return f"{digit} {CHAR_TO_RU_STR[tm][0]}"
    return f"{digit} {CHAR_TO_RU_STR[tm][2]}"


class Seconds2human:

    def __init__(self, seconds: Union[int, float]):
        self.weeks = seconds // 604800
        seconds -= self.weeks * 604800
        self.days = seconds // 86400
        seconds -= self.days * 86400
        self.hours = seconds // 3600
        seconds -= self.hours * 3600
        self.minutes = seconds // 60
        seconds -= self.minutes * 60
        self.seconds = seconds
        self.string = " ".join(filter(None, [_get_times(self.weeks, 'w'),
                                             _get_times(self.days, 'd'),
                                             _get_times(self.hours, 'h'),
                                             _get_times(self.minutes, 'm'),
                                             _get_times(self.seconds, 's')]))

    def __str__(self) -> str:
        return self.string


class Strtime2seconds:

    def __init__(self, string: str):
        self.seconds = 0
        self.string = string
        self.calculate()

    def calculate(self):
        if self.string.isdigit():
            self.seconds = int(self.string)

        else:
            self.seconds = sum([int(x[0]) * CHAR_TO_SEC[x[1]] for x in re.findall(RE_SIMPLE_STRING, self.string)])

    def __str__(self) -> str:
        return str(self.seconds)

    def __repr__(self) -> str:
        return f"{self.__class__} {self.seconds}"
