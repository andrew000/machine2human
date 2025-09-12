from __future__ import annotations

from typing import Literal, TypeAlias

Lang: TypeAlias = str
Key: TypeAlias = Literal["y", "w", "d", "h", "m", "s"]
Char: TypeAlias = str
Singular: TypeAlias = str
SingularIndex: int = 0
Plural2_4: TypeAlias = str
Plural2_4Index: int = 1
Plural5: TypeAlias = str
Plural5Index: int = 2
PluralForms: TypeAlias = tuple[Singular, Plural2_4, Plural5]
Seconds: TypeAlias = int
PluralForm: TypeAlias = str

HAS_THREE_FORMS: frozenset[Lang] = frozenset({"ru", "uk"})

KEY_TO_PLURAL: dict[Lang, dict[Key, PluralForms]] = {
    "en": {
        "y": ("year", "years", "years"),
        "w": ("week", "weeks", "weeks"),
        "d": ("day", "days", "days"),
        "h": ("hour", "hours", "hours"),
        "m": ("minute", "minutes", "minutes"),
        "s": ("second", "seconds", "seconds"),
    },
    "uk": {
        "y": ("рік", "роки", "років"),
        "w": ("тиждень", "тижні", "тижнів"),
        "d": ("день", "дні", "днів"),
        "h": ("година", "години", "годин"),
        "m": ("хвилина", "хвилини", "хвилин"),
        "s": ("секунда", "секунди", "секунд"),
    },
    "ru": {
        "y": ("год", "года", "лет"),
        "w": ("неделя", "недели", "недель"),
        "d": ("день", "дня", "дней"),
        "h": ("час", "часа", "часов"),
        "m": ("минута", "минуты", "минут"),
        "s": ("секунда", "секунды", "секунд"),
    },
}

CHAR_TO_SEC: dict[Lang, dict[Char, Seconds]] = {
    "en": {"y": 31536000, "w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1},
    "uk": {"р": 31536000, "т": 604800, "д": 86400, "г": 3600, "х": 60, "с": 1},
    "ru": {"г": 31536000, "л": 31536000, "н": 604800, "д": 86400, "ч": 3600, "м": 60, "с": 1},
}

LANG_CHARS: dict[Lang, frozenset[Char]] = {
    "en": frozenset(CHAR_TO_SEC["en"].keys()),
    "uk": frozenset(CHAR_TO_SEC["uk"].keys()),
    "ru": frozenset(CHAR_TO_SEC["ru"].keys()),
}

STR_TO_SEC: dict[Lang, dict[PluralForm, Seconds]] = {
    "en": {
        "year": 31536000,
        "years": 31536000,
        "week": 604800,
        "weeks": 604800,
        "day": 86400,
        "days": 86400,
        "hour": 3600,
        "hours": 3600,
        "minute": 60,
        "minutes": 60,
        "second": 1,
        "seconds": 1,
    },
    "uk": {
        "рік": 31536000,
        "роки": 31536000,
        "років": 31536000,
        "тиждень": 604800,
        "тижні": 604800,
        "тижнів": 604800,
        "день": 86400,
        "дні": 86400,
        "днів": 86400,
        "година": 3600,
        "години": 3600,
        "годин": 3600,
        "хвилина": 60,
        "хвилини": 60,
        "хвилин": 60,
        "секунда": 1,
        "секунди": 1,
        "секунд": 1,
    },
    "ru": {
        "год": 31536000,
        "года": 31536000,
        "лет": 31536000,
        "неделя": 604800,
        "недели": 604800,
        "недель": 604800,
        "день": 86400,
        "дня": 86400,
        "дней": 86400,
        "час": 3600,
        "часа": 3600,
        "часов": 3600,
        "минута": 60,
        "минуты": 60,
        "минут": 60,
        "секунда": 1,
        "секунды": 1,
        "секунд": 1,
    },
}
