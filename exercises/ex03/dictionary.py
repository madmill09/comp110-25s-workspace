"""Comp 110 exercise to practice dictionaries"""

__author__: str = "730573256"

key: str
value: str
flipped_dict: dict[str, str]


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the original dictionary in this function."""
    flipped_dict = {}
    for key, value in input_dict.items():
        flipped_dict[value] = key
    return flipped_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in the list."""
    counting_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] in counting_dict:
            counting_dict[input_list[idx]] += 1
        else:
            counting_dict[input_list[idx]] = 1
        idx += 1
    return counting_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Determine the favorite color based on popular vote."""
    colors_list: list[str] = list(color_dict.values())
    colors_count: dict[str, int] = {}
    color: str = ""
    for color in colors_list:
        for color in colors_list:
            colors_count[color] = 0
        if color in colors_list:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
    for color in colors_list:
        max_count = 0
        if colors_count[color] > max_count:
            max_count = colors_count[color]
            colors_count["fav"] = max_count
    for color in colors_list:
        if colors_count[color] == colors_count["fav"]:
            return color
    return color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    result: dict[int, set] = {}
    for string in strings:
        length = len(string)
        if length not in result:
            result[length] = set()
        result[length].add(string)
    return result
