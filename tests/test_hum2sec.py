from datetime import timedelta

import pytest

from m2h import Hum2Sec


def test_en_hum2sec() -> None:
    assert Hum2Sec("", lang="en").seconds == 0
    assert Hum2Sec("0", lang="en").seconds == 0
    assert Hum2Sec("100", lang="en").seconds == 100
    assert Hum2Sec("0 seconds", lang="en").seconds == 0
    assert Hum2Sec("1 second", lang="en").seconds == 1
    assert Hum2Sec("2 seconds", lang="en").seconds == 2
    assert Hum2Sec("5 seconds", lang="en").seconds == 5
    assert Hum2Sec("1s", lang="en").seconds == 1
    assert Hum2Sec("1 minute", lang="en").seconds == 60
    assert Hum2Sec("2 minutes", lang="en").seconds == 120
    assert Hum2Sec("5 minutes", lang="en").seconds == 300
    assert Hum2Sec("1m", lang="en").seconds == 60
    assert Hum2Sec("1 hour", lang="en").seconds == 3600
    assert Hum2Sec("2 hours", lang="en").seconds == 7200
    assert Hum2Sec("5 hours", lang="en").seconds == 18000
    assert Hum2Sec("1h", lang="en").seconds == 3600
    assert Hum2Sec("1 day", lang="en").seconds == 86400
    assert Hum2Sec("2 days", lang="en").seconds == 172800
    assert Hum2Sec("5 days", lang="en").seconds == 432000
    assert Hum2Sec("1d", lang="en").seconds == 86400
    assert Hum2Sec("1 week", lang="en").seconds == 604800
    assert Hum2Sec("2 weeks", lang="en").seconds == 1209600
    assert Hum2Sec("5 weeks", lang="en").seconds == 3024000
    assert Hum2Sec("1w", lang="en").seconds == 604800
    assert Hum2Sec("1 year 1 week 1 day 1 hour 1 minute 1 second", lang="en").seconds == 32230861
    assert (
        Hum2Sec("2 years 2 weeks 2 days 2 hours 2 minutes 2 seconds", lang="en").seconds == 64461722
    )
    assert (
        Hum2Sec("5 years 5 weeks 5 days 5 hours 5 minutes 5 seconds", lang="en").seconds
        == 161154305
    )

    assert (
        Hum2Sec("5 years 5 weeks 5 days 5 hours 5 minutes 5 seconds", lang="en").string
        == "5 years 5 weeks 5 days 5 hours 5 minutes 5 seconds"
    )


def test_uk_hum2sec() -> None:
    assert Hum2Sec("", lang="uk").seconds == 0
    assert Hum2Sec("0", lang="uk").seconds == 0
    assert Hum2Sec("100", lang="uk").seconds == 100
    assert Hum2Sec("0 секунд", lang="uk").seconds == 0
    assert Hum2Sec("1 секунда", lang="uk").seconds == 1
    assert Hum2Sec("2 секунди", lang="uk").seconds == 2
    assert Hum2Sec("5 секунд", lang="uk").seconds == 5
    assert Hum2Sec("1с", lang="uk").seconds == 1
    assert Hum2Sec("1 хвилина", lang="uk").seconds == 60
    assert Hum2Sec("2 хвилини", lang="uk").seconds == 120
    assert Hum2Sec("5 хвилин", lang="uk").seconds == 300
    assert Hum2Sec("1хв", lang="uk").seconds == 60
    assert Hum2Sec("1 година", lang="uk").seconds == 3600
    assert Hum2Sec("2 години", lang="uk").seconds == 7200
    assert Hum2Sec("5 годин", lang="uk").seconds == 18000
    assert Hum2Sec("1г", lang="uk").seconds == 3600
    assert Hum2Sec("1 день", lang="uk").seconds == 86400
    assert Hum2Sec("2 дні", lang="uk").seconds == 172800
    assert Hum2Sec("5 днів", lang="uk").seconds == 432000
    assert Hum2Sec("1д", lang="uk").seconds == 86400
    assert Hum2Sec("1 тиждень", lang="uk").seconds == 604800
    assert Hum2Sec("2 тижні", lang="uk").seconds == 1209600
    assert Hum2Sec("5 тижнів", lang="uk").seconds == 3024000
    assert Hum2Sec("1т", lang="uk").seconds == 604800
    assert (
        Hum2Sec("1 рік 1 тиждень 1 день 1 година 1 хвилина 1 секунда", lang="uk").seconds
        == 32230861
    )
    assert (
        Hum2Sec("2 роки 2 тижні 2 дні 2 години 2 хвилини 2 секунди", lang="uk").seconds == 64461722
    )
    assert (
        Hum2Sec("5 років 5 тижнів 5 днів 5 годин 5 хвилин 5 секунд", lang="uk").seconds == 161154305
    )

    assert (
        Hum2Sec("5 років 5 тижнів 5 днів 5 годин 5 хвилин 5 секунд", lang="uk").string
        == "5 років 5 тижнів 5 днів 5 годин 5 хвилин 5 секунд"
    )


def test_ru_hum2sec() -> None:
    assert Hum2Sec("", lang="ru").seconds == 0
    assert Hum2Sec("0", lang="ru").seconds == 0
    assert Hum2Sec("100", lang="ru").seconds == 100
    assert Hum2Sec("0 секунд", lang="ru").seconds == 0
    assert Hum2Sec("1 секунда", lang="ru").seconds == 1
    assert Hum2Sec("2 секунды", lang="ru").seconds == 2
    assert Hum2Sec("5 секунд", lang="ru").seconds == 5
    assert Hum2Sec("1с", lang="ru").seconds == 1
    assert Hum2Sec("1 минута", lang="ru").seconds == 60
    assert Hum2Sec("2 минуты", lang="ru").seconds == 120
    assert Hum2Sec("5 минут", lang="ru").seconds == 300
    assert Hum2Sec("1м", lang="ru").seconds == 60
    assert Hum2Sec("1 час", lang="ru").seconds == 3600
    assert Hum2Sec("2 часа", lang="ru").seconds == 7200
    assert Hum2Sec("5 часов", lang="ru").seconds == 18000
    assert Hum2Sec("1ч", lang="ru").seconds == 3600
    assert Hum2Sec("1 день", lang="ru").seconds == 86400
    assert Hum2Sec("2 дня", lang="ru").seconds == 172800
    assert Hum2Sec("5 дней", lang="ru").seconds == 432000
    assert Hum2Sec("1д", lang="ru").seconds == 86400
    assert Hum2Sec("1 неделя", lang="ru").seconds == 604800
    assert Hum2Sec("2 недели", lang="ru").seconds == 1209600
    assert Hum2Sec("5 недель", lang="ru").seconds == 3024000
    assert Hum2Sec("1н", lang="ru").seconds == 604800
    assert Hum2Sec("1 год 1 неделя 1 день 1 час 1 минута 1 секунда", lang="ru").seconds == 32230861
    assert Hum2Sec("2 года 2 недели 2 дня 2 часа 2 минуты 2 секунды", lang="ru").seconds == 64461722
    assert Hum2Sec("5 лет 5 недель 5 дней 5 часов 5 минут 5 секунд", lang="ru").seconds == 161154305

    assert (
        Hum2Sec("5 лет 5 недель 5 дней 5 часов 5 минут 5 секунд", lang="ru").string
        == "5 лет 5 недель 5 дней 5 часов 5 минут 5 секунд"
    )


def test_seconds_overflow() -> None:
    with pytest.warns(UserWarning, match="Value is too large, setting to max value."):
        obj = Hum2Sec(f"{int(timedelta.max.total_seconds())}", lang="en")

    assert obj.timedelta == timedelta.max


def test_timedelta_overflow() -> None:
    with pytest.warns(UserWarning, match="Value is too large, setting to max value."):
        obj = Hum2Sec("1000000000000 years", lang="en")

    assert obj.timedelta == timedelta.max


def test_hum2sec_seconds_setter() -> None:
    obj = Hum2Sec("1 hour", lang="en")

    with pytest.raises(ValueError):  # noqa: PT011
        obj.seconds = 0


def test_hum2sec_timedelta_setter() -> None:
    obj = Hum2Sec("1 hour", lang="en")

    with pytest.raises(ValueError):  # noqa: PT011
        obj.timedelta = timedelta(seconds=0)


def test_hum2sec_string_setter() -> None:
    obj = Hum2Sec("1 hour", lang="en")
    assert obj.seconds == 3600

    obj.string = "2 hours"
    assert obj.seconds == 7200


def test_hum2sec_lang_setter() -> None:
    obj = Hum2Sec("1 hour", lang="en")
    assert obj.lang == "en"
    assert obj.seconds == 3600

    obj.lang = "uk"
    assert obj.lang == "uk"
    assert obj.seconds == 0  # because "1 hour" is not valid in Ukrainian
