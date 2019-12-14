import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
import m2h


def test_strtime2seconds():
    cases = {
        '0w': 0,
        '0d': 0,
        '0h': 0,
        '0m': 0,
        '0s': 0,
        '1w': 604800,
        '1d': 86400,
        '1h': 3600,
        '1m': 60,
        '1s': 1,
        '2w3d4m5s': 1469045,
        '2w  3d  4m  5s': 1469045,
        '50d': 4320000,
        '50d -ae-=orfeads': 4320000,
        '-ae-=orfeads 50d': 4320000,
    }

    for k, v in cases.items():
        assert m2h.Strtime2seconds(k).seconds == v


def test_seconds2human():
    cases = {
        0: '',
        604800: '7 дней',
        86400: '1 день',
        3600: '1 час',
        60: '1 минута',
        1: '1 секунда',
        1469045: '17 дней 4 минуты 5 секунд',
    }

    for k, v in cases.items():
        assert str(m2h.Seconds2human(k)) == v
