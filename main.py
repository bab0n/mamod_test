import re


def to_camel_case(text: str) -> str:
    return ''.join(word.title() for word in re.split('_|-', text))


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def count_bits(n: int) -> int:
    return n.bit_count()  # Python 3.10+
    # count_bits = lambda n: bin(n).count('1') # Python 3.9-


def digital_root(n: int) -> int:
    return n if n < 10 else digital_root(sum(map(int, str(n))))


def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"
    # even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
