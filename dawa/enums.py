from enum import Enum


class DawaEnum(Enum):
    vejstykke = 'vejstykke'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)