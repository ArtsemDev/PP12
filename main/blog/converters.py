from ulid import parse, ULID

from re import fullmatch


class ULIDConverter:
    regex = r'[a-z,A-Z,0-9]{24}'

    def to_python(self, value: str):
        if fullmatch(self.regex, value) is None:
            raise ValueError
        return value

    def to_url(self, value: ULID):
        return value.str
