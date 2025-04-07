"""Comp 110 testing the ex03 dictionary file"""

__author__: str = "730573256"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert() -> None:
    """test the invert function in the dictionary file use case 1"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_2() -> None:
    """test the invert function in the dictionary file use case 2"""
    assert invert({"apple": "fruit", "broccoli": "vegetable"}) == {
        "fruit": "apple",
        "vegetable": "broccoli",
    }


def test_invert_3() -> None:
    """test the invert function in the definition file edge case"""
    assert invert({}) == {}


def test_count_part2() -> None:
    """Test the count function in the dictionary file use case 1."""
    assert count(["Wake", "Orange", "Orange", "Durham"]) == {
        "Wake": 1,
        "Orange": 2,
        "Durham": 1,
    }


def test_count_part2_2() -> None:
    """Test the count function in the dictionary file use case 2"""
    assert count(["Madison", "Madison", "Izzy", "David", "Jesse"]) == {
        "Madison": 2,
        "Izzy": 1,
        "David": 1,
        "Jesse": 1,
    }


def test_count_part2_3() -> None:
    """Test the count function in the dictionary file edge case"""
    assert count([]) == {}


def test_favorite_color() -> None:
    """Test the favorite_color function in the dictionary file use case"""
    assert (
        favorite_color({"Madison": "Pink", "Nathaniel": "Blue", "Emily": "Pink"})
        == "Pink"
    )


def test_favorite_color_2() -> None:
    """Test the favorite_color function in the dictionary file use case"""
    assert favorite_color({"Maddie": "Pink"}) == "Pink"


def test_favorite_color_3() -> None:
    """Test the favorite_color function in the dictionary file edge case"""
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    """Test the bin_len function in the dictionary file use case"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    """Test the bin_len function in the dictionary file use case"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len3() -> None:
    """Test the bin_len function in the dictionary file edge case"""
    assert bin_len([""])
