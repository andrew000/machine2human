from m2h import Sec2Hum


def test_sec2hum():
    assert Sec2Hum(0).string == '0 секунд'
    assert Sec2Hum(1).string == '1 секунда'
    assert Sec2Hum(-1).string == '1 секунда'
    assert Sec2Hum(2).string == '2 секунды'
    assert Sec2Hum(5).string == '5 секунд'
    assert Sec2Hum(60).string == '1 минута'
    assert Sec2Hum(120).string == '2 минуты'
    assert Sec2Hum(300).string == '5 минут'
    assert Sec2Hum(3600).string == '1 час'
    assert Sec2Hum(7200).string == '2 часа'
    assert Sec2Hum(18000).string == '5 часов'
    assert Sec2Hum(86400).string == '1 день'
    assert Sec2Hum(172800).string == '2 дня'
    assert Sec2Hum(432000).string == '5 дней'
    assert Sec2Hum(604800).string == '1 неделя'
    assert Sec2Hum(1209600).string == '2 недели'
    assert Sec2Hum(2592000).string == '1 Месяц'
    assert Sec2Hum(5184000).string == '2 Месяца'
    assert Sec2Hum(12960000).string == '5 Месяцев'
    assert Sec2Hum(31536000).string == '1 год'
    assert Sec2Hum(63072000).string == '2 года'
    assert Sec2Hum(157680000).string == '5 лет'

    assert Sec2Hum(34822861).string == '1 год 1 Месяц 1 неделя 1 день 1 час 1 минута 1 секунда'
    assert Sec2Hum(69645722).string == '2 года 2 Месяца 2 недели 2 дня 2 часа 2 минуты 2 секунды'
    assert Sec2Hum(174546305).string == '5 лет 6 Месяцев 2 недели 1 день 5 часов 5 минут 5 секунд'
