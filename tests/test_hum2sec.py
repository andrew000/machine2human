from m2h import Hum2Sec


def test_hum2sec():
    assert Hum2Sec('').seconds == 0
    assert Hum2Sec('0').seconds == 0
    assert Hum2Sec('100').seconds == 100
    assert Hum2Sec('0 секунд').seconds == 0
    assert Hum2Sec('1 секунда').seconds == 1
    assert Hum2Sec('1 sec').seconds == 1
    assert Hum2Sec('1с').seconds == 1
    assert Hum2Sec('1s').seconds == 1
    assert Hum2Sec('1 минута').seconds == 60
    assert Hum2Sec('1 min').seconds == 60
    assert Hum2Sec('1м').seconds == 60
    assert Hum2Sec('1m').seconds == 60
    assert Hum2Sec('1 час').seconds == 3600
    assert Hum2Sec('1 hour').seconds == 3600
    assert Hum2Sec('1ч').seconds == 3600
    assert Hum2Sec('1h').seconds == 3600
    assert Hum2Sec('1 день').seconds == 86400
    assert Hum2Sec('1 day').seconds == 86400
    assert Hum2Sec('1д').seconds == 86400
    assert Hum2Sec('1d').seconds == 86400
    assert Hum2Sec('1 неделя').seconds == 604800
    assert Hum2Sec('1 week').seconds == 604800
    assert Hum2Sec('1н').seconds == 604800
    assert Hum2Sec('1w').seconds == 604800
    assert Hum2Sec('1 неделя 1 день 1 час 1 минута 1 секунда').seconds == 694861
    assert Hum2Sec('2 недели 2 дня 2 часа 2 минуты 2 секунды').seconds == 1389722
    assert Hum2Sec('5 недель 5 дней 5 часов 5 минут 5 секунд').seconds == 3474305

