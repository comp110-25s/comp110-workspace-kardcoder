"""EX03 - Dictionary Functions."""

__author__ = "730822339"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary. If duplicate values exist, raises a KeyError."""
    result: dict[str, str] = {}
    for key in input_dict:
        val = input_dict[key]
        if val in result:
            raise KeyError(f"Duplicate value found: {val}")
        result[val] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a unique value in the input list,
    and each value is the count of how many times it appeared."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dictionary values.
    If there is a tie, returns the first one encountered."""
    color_counts: dict[str, int] = count(list(color_dict.values()))

    max_count = 0
    most_frequent = ""

    for name in color_dict:
        color = color_dict[name]
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_frequent = color
        # No need to check for equality; we want the first color encountered in a tie

    return most_frequent


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins strings into a dictionary where each key is the length of strings,
    and the value is a set of all strings of that length."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
