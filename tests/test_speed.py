from m2h import Sec2Hum, Hum2Sec
from random import randint, choice


def _gen_string(_range) -> str:
    return "".join(["{}{}".format(randint(1, 100), choice("yMwdhmsгМндчмс")) for _ in range(_range)])


test_string = _gen_string(1000000)
test_seconds = randint(100000, 999999999)


def test_m2h_hum2sec():
    return Hum2Sec(test_string).seconds


def test_m2h_sec2hum():
    return Sec2Hum(test_seconds).string
