from __future__ import annotations

import array
from datetime import timedelta
from string import digits
from sys import version_info
from typing import Any, ClassVar, NoReturn
from warnings import warn

from m2h.lang import (
    CHAR_TO_SEC,
    HAS_THREE_FORMS,
    KEY_TO_PLURAL,
    Key,
    Lang,
    Plural2_4Index,
    Plural5Index,
    Seconds,
    SingularIndex,
)

if version_info >= (3, 13):
    ARRAY_C_TYPE = "w"  # pragma: no cover
else:
    ARRAY_C_TYPE = "u"  # pragma: no cover

DIGITS: frozenset[str] = frozenset(digits)


def apply_plural(*, digit: float, key: Key, lang: Lang) -> str | None:
    digit = round(digit)

    if digit == 0:
        return None

    if lang in HAS_THREE_FORMS:
        tmp = digit % 100
        if 11 <= tmp <= 19:
            return f"{digit} {KEY_TO_PLURAL[lang][key][Plural5Index]}"
        tmp = digit % 10
        if tmp == 1:
            return f"{digit} {KEY_TO_PLURAL[lang][key][SingularIndex]}"
        if 2 <= tmp <= 4:
            return f"{digit} {KEY_TO_PLURAL[lang][key][Plural2_4Index]}"
        if tmp == 0 or 5 <= tmp <= 9:
            return f"{digit} {KEY_TO_PLURAL[lang][key][Plural5Index]}"

        msg = "unreachable"  # pragma: no cover
        raise AssertionError(msg)  # pragma: no cover

    if digit == 1:
        return f"{digit} {KEY_TO_PLURAL[lang][key][SingularIndex]}"

    return f"{digit} {KEY_TO_PLURAL[lang][key][Plural2_4Index]}"


def human_parser(*, string: str, lang: Lang) -> Seconds:
    tmp_digit: array.array[str] = array.array(ARRAY_C_TYPE)
    seconds: Seconds = 0
    char_to_sec = CHAR_TO_SEC[lang]
    char_to_sec_keys = frozenset(CHAR_TO_SEC[lang].keys())

    for char in string:
        if char in DIGITS:
            tmp_digit.append(char)

        elif tmp_digit and char in char_to_sec_keys:
            seconds += int(tmp_digit.tounicode()) * char_to_sec[char]
            tmp_digit = array.array(ARRAY_C_TYPE)

    return seconds


class Sec2Hum:
    __slots__ = (
        "days",
        "hours",
        "lang",
        "minutes",
        "seconds",
        "string",
        "weeks",
        "years",
    )

    __seconds_to_attr__: ClassVar[dict[Seconds, str]] = {
        31536000: "years",
        604800: "weeks",
        86400: "days",
        3600: "hours",
        60: "minutes",
        1: "seconds",
    }

    def __init__(self, seconds: float | timedelta, lang: Lang) -> None:
        if isinstance(seconds, (int, float)):
            seconds = abs(seconds)

        elif isinstance(seconds, timedelta):
            seconds = abs(seconds.total_seconds())

        else:
            raise TypeError

        self.years: float = 0
        self.weeks: float = 0
        self.days: float = 0
        self.hours: float = 0
        self.minutes: float = 0
        self.seconds: float = 0
        self.lang = lang

        if seconds == 0:
            if lang in HAS_THREE_FORMS:
                self.string = f"0 {KEY_TO_PLURAL[self.lang]['s'][Plural5Index]}"
            else:
                self.string = f"0 {KEY_TO_PLURAL[self.lang]['s'][SingularIndex]}"

        else:
            for sec, attr in self.__seconds_to_attr__.items():
                self.__setattr__(attr, seconds // sec)
                seconds %= sec

            self.string = " ".join(
                filter(
                    None,
                    (
                        apply_plural(digit=self.years, key="y", lang=self.lang),
                        apply_plural(digit=self.weeks, key="w", lang=self.lang),
                        apply_plural(digit=self.days, key="d", lang=self.lang),
                        apply_plural(digit=self.hours, key="h", lang=self.lang),
                        apply_plural(digit=self.minutes, key="m", lang=self.lang),
                        apply_plural(digit=self.seconds, key="s", lang=self.lang),
                    ),
                )
            )

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return f"{self.__class__} {self.string}"


class Hum2Sec:
    def __init__(self, string: str, lang: Lang) -> None:
        self.__seconds: int = 0
        self.__timedelta: timedelta = timedelta()
        self.__string = string
        self.__lang = lang
        self.calculate()

    def calculate(self) -> None:
        if self.__string.isdigit():
            self.__seconds = int(self.__string)

            if self.__seconds > 86399999999999:
                warn("Value is too large, setting to max value.", stacklevel=2)
                self.__timedelta = timedelta.max

            else:
                self.__timedelta = timedelta(seconds=self.__seconds)

        else:
            self.__seconds = human_parser(string=self.__string, lang=self.__lang)

            if self.__seconds > 86399999999999:
                warn("Value is too large, setting to max value.", stacklevel=2)
                self.__timedelta = timedelta.max
            else:
                self.__timedelta = timedelta(seconds=self.__seconds)

    @property
    def seconds(self) -> int:
        return self.__seconds

    @seconds.setter
    def seconds(self, _: Any) -> NoReturn:
        raise ValueError

    @property
    def timedelta(self) -> timedelta:
        return self.__timedelta

    @timedelta.setter
    def timedelta(self, _: Any) -> NoReturn:
        raise ValueError

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, value: str) -> None:
        self.__string = value
        self.calculate()

    @property
    def lang(self) -> Lang:
        return self.__lang

    @lang.setter
    def lang(self, value: Lang) -> None:
        self.__lang = value
        self.calculate()

    def __str__(self) -> str:
        return str(self.__seconds)

    def __repr__(self) -> str:
        return f"{self.__class__} {self.__seconds}"
