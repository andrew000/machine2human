import re
from datetime import timedelta
from typing import Union

RE_SIMPLE_STRING = re.compile(r"(\d+)+\s*([yMwdhmsглМндчмс])")
CHAR_TO_RU_STR = {'y': ('лет', 'год', 'года'),
                  'M': ('Месяцев', 'Месяц', 'Месяца'),
                  'w': ('недель', 'неделя', 'недели'),
                  'd': ('дней', 'день', 'дня'),
                  'h': ('часов', 'час', 'часа'),
                  'm': ('минут', 'минута', 'минуты'),
                  's': ('секунд', 'секунда', 'секунды')}
CHAR_TO_SEC = {'y': 31536000, 'M': 2592000, 'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1,
               'г': 31536000, 'л': 31536000, 'М': 2592000, 'н': 604800, 'д': 86400, 'ч': 3600, 'м': 60, 'с': 1}
STR_TO_SEC = {'years': 31536000, 'months': 2592000, 'weeks': 604800,
              'days': 86400, 'hours': 3600, 'minutes': 60, 'seconds': 1}


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


class Sec2Hum:
    __slots__ = ['years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds', 'string']

    def __init__(self, seconds: Union[int, float, timedelta]):
        if isinstance(seconds, int) or isinstance(seconds, float):
            seconds = abs(seconds)

        elif isinstance(seconds, timedelta):
            seconds = seconds.total_seconds()

        else:
            raise TypeError

        if seconds == 0:
            self.seconds = 0
            self.string = '0 секунд'

        else:
            for k, v in STR_TO_SEC.items():
                self.__setattr__(k, seconds // v)
                seconds %= v

            self.string = " ".join(filter(None, (_get_times(self.years, 'y'),
                                                 _get_times(self.months, 'M'),
                                                 _get_times(self.weeks, 'w'),
                                                 _get_times(self.days, 'd'),
                                                 _get_times(self.hours, 'h'),
                                                 _get_times(self.minutes, 'm'),
                                                 _get_times(self.seconds, 's'))))

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return f"{self.__class__} {self.string}"


class Hum2Sec:
    """
    :var self.seconds:
    :type self.seconds: int
    """
    __seconds: int
    __delta: timedelta

    def __init__(self, string: str):
        """
        :param string: time-string to parse.
        :type string: str.
        """
        self.string = string
        self.calculate()

    def calculate(self):
        if self.string.isdigit():
            self.__seconds = int(self.string)

            try:
                self.__delta = timedelta(seconds=self.__seconds)

            except OverflowError:
                self.__delta = timedelta(seconds=999999999)

        else:
            self.__seconds = sum([int(x[0]) * CHAR_TO_SEC[x[1]] for x in re.findall(RE_SIMPLE_STRING, self.string)])

            try:
                self.__delta = timedelta(seconds=self.__seconds)

            except OverflowError:
                self.__delta = timedelta(seconds=999999999)

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        raise ValueError

    @property
    def delta(self):
        return self.__delta

    @delta.setter
    def delta(self, value):
        raise ValueError

    def __str__(self) -> str:
        return str(self.__seconds)

    def __repr__(self) -> str:
        return f"{self.__class__} {self.__seconds}"
