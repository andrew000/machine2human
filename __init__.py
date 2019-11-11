from typing import Union


def _get_times(digit: Union[int, float], tm: str) -> str:
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


class Seconds2human:

    def __init__(self, seconds: Union[int, float]):
        self.days = seconds // 86400
        seconds -= self.days * 86400
        self.hours = seconds // 3600
        seconds -= self.hours * 3600
        self.minutes = seconds // 60
        seconds -= self.minutes * 60
        self.seconds = seconds
        self.string = " ".join(
            f"{_get_times(self.days, 'd')} {_get_times(self.hours, 'h')} {_get_times(self.minutes, 'm')} {_get_times(self.seconds, 's')}".split())


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


__all__ = ['Seconds2human', 'Strtime2seconds']
