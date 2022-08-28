import re

SPECIAL_SYMBOL = {'\n', '\t', '\r', ';', ',', ' ', '，'}
STRING_SPLIT_REGEX = re.compile(rf'[{"".join(SPECIAL_SYMBOL)}]')


def string_symbol_split(string: str) -> list[str]:
    if not isinstance(string, str):
        raise ValueError(f"Expected type str, but got {type(string)}")
    # has_special_symbol = set(string) & SPECIAL_SYMBOL
    # if has_special_symbol:
    #     raise ValueError(f"String contains wrong symbol: {has_special_symbol}."
    #                      f"Symbols should not appear in a string: {SPECIAL_SYMBOL}")
    return list(filter(lambda x: x != '', map(lambda x: x.strip(), STRING_SPLIT_REGEX.split(string))))
