from datetime import timedelta

import pytest

from m2h import Sec2Hum


def test_en_sec2hum() -> None:
    assert Sec2Hum(seconds=0, lang="en").string == "0 second"
    assert Sec2Hum(seconds=1, lang="en").string == "1 second"
    assert Sec2Hum(seconds=-1, lang="en").string == "1 second"
    assert Sec2Hum(seconds=2, lang="en").string == "2 seconds"
    assert Sec2Hum(seconds=5, lang="en").string == "5 seconds"
    assert Sec2Hum(seconds=11, lang="en").string == "11 seconds"
    assert Sec2Hum(seconds=60, lang="en").string == "1 minute"
    assert Sec2Hum(seconds=120, lang="en").string == "2 minutes"
    assert Sec2Hum(seconds=300, lang="en").string == "5 minutes"
    assert Sec2Hum(seconds=660, lang="en").string == "11 minutes"
    assert Sec2Hum(seconds=3600, lang="en").string == "1 hour"
    assert Sec2Hum(seconds=7200, lang="en").string == "2 hours"
    assert Sec2Hum(seconds=18000, lang="en").string == "5 hours"
    assert Sec2Hum(seconds=39600, lang="en").string == "11 hours"
    assert Sec2Hum(seconds=86400, lang="en").string == "1 day"
    assert Sec2Hum(seconds=172800, lang="en").string == "2 days"
    assert Sec2Hum(seconds=432000, lang="en").string == "5 days"
    assert Sec2Hum(seconds=604800, lang="en").string == "1 week"
    assert Sec2Hum(seconds=1209600, lang="en").string == "2 weeks"
    assert Sec2Hum(seconds=3024000, lang="en").string == "5 weeks"
    assert Sec2Hum(seconds=6652800, lang="en").string == "11 weeks"
    assert Sec2Hum(seconds=31536000, lang="en").string == "1 year"
    assert Sec2Hum(seconds=63072000, lang="en").string == "2 years"
    assert Sec2Hum(seconds=157680000, lang="en").string == "5 years"
    assert Sec2Hum(seconds=346896000, lang="en").string == "11 years"
    assert (
        Sec2Hum(seconds=32230861, lang="en").string
        == "1 year 1 week 1 day 1 hour 1 minute 1 second"
    )
    assert (
        Sec2Hum(seconds=64461722, lang="en").string
        == "2 years 2 weeks 2 days 2 hours 2 minutes 2 seconds"
    )
    assert (
        Sec2Hum(seconds=161154305, lang="en").string
        == "5 years 5 weeks 5 days 5 hours 5 minutes 5 seconds"
    )


def test_uk_sec2hum() -> None:
    assert Sec2Hum(seconds=0, lang="uk").string == "0 секунд"
    assert Sec2Hum(seconds=1, lang="uk").string == "1 секунда"
    assert Sec2Hum(seconds=-1, lang="uk").string == "1 секунда"
    assert Sec2Hum(seconds=2, lang="uk").string == "2 секунди"
    assert Sec2Hum(seconds=5, lang="uk").string == "5 секунд"
    assert Sec2Hum(seconds=11, lang="uk").string == "11 секунд"
    assert Sec2Hum(seconds=60, lang="uk").string == "1 хвилина"
    assert Sec2Hum(seconds=120, lang="uk").string == "2 хвилини"
    assert Sec2Hum(seconds=300, lang="uk").string == "5 хвилин"
    assert Sec2Hum(seconds=660, lang="uk").string == "11 хвилин"
    assert Sec2Hum(seconds=3600, lang="uk").string == "1 година"
    assert Sec2Hum(seconds=7200, lang="uk").string == "2 години"
    assert Sec2Hum(seconds=18000, lang="uk").string == "5 годин"
    assert Sec2Hum(seconds=39600, lang="uk").string == "11 годин"
    assert Sec2Hum(seconds=86400, lang="uk").string == "1 день"
    assert Sec2Hum(seconds=172800, lang="uk").string == "2 дні"
    assert Sec2Hum(seconds=432000, lang="uk").string == "5 днів"
    assert Sec2Hum(seconds=604800, lang="uk").string == "1 тиждень"
    assert Sec2Hum(seconds=1209600, lang="uk").string == "2 тижні"
    assert Sec2Hum(seconds=3024000, lang="uk").string == "5 тижнів"
    assert Sec2Hum(seconds=6652800, lang="uk").string == "11 тижнів"
    assert Sec2Hum(seconds=31536000, lang="uk").string == "1 рік"
    assert Sec2Hum(seconds=63072000, lang="uk").string == "2 роки"
    assert Sec2Hum(seconds=157680000, lang="uk").string == "5 років"
    assert Sec2Hum(seconds=346896000, lang="uk").string == "11 років"
    assert (
        Sec2Hum(seconds=32230861, lang="uk").string
        == "1 рік 1 тиждень 1 день 1 година 1 хвилина 1 секунда"
    )
    assert (
        Sec2Hum(seconds=64461722, lang="uk").string
        == "2 роки 2 тижні 2 дні 2 години 2 хвилини 2 секунди"
    )
    assert (
        Sec2Hum(seconds=161154305, lang="uk").string
        == "5 років 5 тижнів 5 днів 5 годин 5 хвилин 5 секунд"
    )


def test_ru_sec2hum() -> None:
    assert Sec2Hum(seconds=0, lang="ru").string == "0 секунд"
    assert Sec2Hum(seconds=1, lang="ru").string == "1 секунда"
    assert Sec2Hum(seconds=-1, lang="ru").string == "1 секунда"
    assert Sec2Hum(seconds=2, lang="ru").string == "2 секунды"
    assert Sec2Hum(seconds=5, lang="ru").string == "5 секунд"
    assert Sec2Hum(seconds=11, lang="ru").string == "11 секунд"
    assert Sec2Hum(seconds=60, lang="ru").string == "1 минута"
    assert Sec2Hum(seconds=120, lang="ru").string == "2 минуты"
    assert Sec2Hum(seconds=300, lang="ru").string == "5 минут"
    assert Sec2Hum(seconds=660, lang="ru").string == "11 минут"
    assert Sec2Hum(seconds=3600, lang="ru").string == "1 час"
    assert Sec2Hum(seconds=7200, lang="ru").string == "2 часа"
    assert Sec2Hum(seconds=18000, lang="ru").string == "5 часов"
    assert Sec2Hum(seconds=39600, lang="ru").string == "11 часов"
    assert Sec2Hum(seconds=86400, lang="ru").string == "1 день"
    assert Sec2Hum(seconds=172800, lang="ru").string == "2 дня"
    assert Sec2Hum(seconds=432000, lang="ru").string == "5 дней"
    assert Sec2Hum(seconds=604800, lang="ru").string == "1 неделя"
    assert Sec2Hum(seconds=1209600, lang="ru").string == "2 недели"
    assert Sec2Hum(seconds=3024000, lang="ru").string == "5 недель"
    assert Sec2Hum(seconds=6652800, lang="ru").string == "11 недель"
    assert Sec2Hum(seconds=31536000, lang="ru").string == "1 год"
    assert Sec2Hum(seconds=63072000, lang="ru").string == "2 года"
    assert Sec2Hum(seconds=157680000, lang="ru").string == "5 лет"
    assert Sec2Hum(seconds=346896000, lang="ru").string == "11 лет"
    assert (
        Sec2Hum(seconds=32230861, lang="ru").string
        == "1 год 1 неделя 1 день 1 час 1 минута 1 секунда"
    )
    assert (
        Sec2Hum(seconds=64461722, lang="ru").string
        == "2 года 2 недели 2 дня 2 часа 2 минуты 2 секунды"
    )
    assert (
        Sec2Hum(seconds=161154305, lang="ru").string
        == "5 лет 5 недель 5 дней 5 часов 5 минут 5 секунд"
    )


def test_timedelta_sec2hum() -> None:
    assert Sec2Hum(seconds=timedelta(seconds=0), lang="en").string == "0 second"
    assert Sec2Hum(seconds=timedelta(seconds=1), lang="en").string == "1 second"
    assert Sec2Hum(seconds=timedelta(seconds=-1), lang="en").string == "1 second"
    assert Sec2Hum(seconds=timedelta(seconds=2), lang="en").string == "2 seconds"
    assert Sec2Hum(seconds=timedelta(seconds=5), lang="en").string == "5 seconds"
    assert Sec2Hum(seconds=timedelta(seconds=60), lang="en").string == "1 minute"
    assert Sec2Hum(seconds=timedelta(seconds=120), lang="en").string == "2 minutes"
    assert Sec2Hum(seconds=timedelta(seconds=300), lang="en").string == "5 minutes"
    assert Sec2Hum(seconds=timedelta(seconds=3600), lang="en").string == "1 hour"
    assert Sec2Hum(seconds=timedelta(seconds=7200), lang="en").string == "2 hours"
    assert Sec2Hum(seconds=timedelta(seconds=18000), lang="en").string == "5 hours"
    assert Sec2Hum(seconds=timedelta(seconds=86400), lang="en").string == "1 day"
    assert Sec2Hum(seconds=timedelta(seconds=172800), lang="en").string == "2 days"
    assert Sec2Hum(seconds=timedelta(seconds=432000), lang="en").string == "5 days"
    assert Sec2Hum(seconds=timedelta(seconds=604800), lang="en").string == "1 week"
    assert Sec2Hum(seconds=timedelta(seconds=1209600), lang="en").string == "2 weeks"
    assert Sec2Hum(seconds=timedelta(seconds=3024000), lang="en").string == "5 weeks"
    assert Sec2Hum(seconds=timedelta(seconds=31536000), lang="en").string == "1 year"
    assert Sec2Hum(seconds=timedelta(seconds=63072000), lang="en").string == "2 years"
    assert Sec2Hum(seconds=timedelta(seconds=157680000), lang="en").string == "5 years"
    assert (
        Sec2Hum(seconds=timedelta(seconds=32230861), lang="en").string
        == "1 year 1 week 1 day 1 hour 1 minute 1 second"
    )
    assert (
        Sec2Hum(seconds=timedelta(seconds=64461722), lang="en").string
        == "2 years 2 weeks 2 days 2 hours 2 minutes 2 seconds"
    )
    assert (
        Sec2Hum(seconds=timedelta(seconds=161154305), lang="en").string
        == "5 years 5 weeks 5 days 5 hours 5 minutes 5 seconds"
    )


def test_incompatible_type_sec2hum() -> None:
    with pytest.raises(TypeError):
        Sec2Hum(seconds="100", lang="en")  # type: ignore[arg-type]
