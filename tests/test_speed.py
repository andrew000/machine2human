from random import choice, randint

from m2h import Hum2Sec, Sec2Hum


def _gen_string(_range) -> str:
    return "".join(["{}{}".format(randint(1, 100), choice("yMwdhmsгМндчмс")) for _ in range(_range)])


test_string = _gen_string(1_000_000)
test_seconds = randint(100_000, 999_999_999)


def test_m2h_hum2sec():
    return Hum2Sec(test_string).seconds


def test_m2h_sec2hum():
    return Sec2Hum(test_seconds).string
