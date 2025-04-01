"""EX03 - Unit Tests for Dictionary Functions."""

__author__ = "730822339"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_empty_dict():
    """Edge case: inverting an empty dictionary should return an empty dictionary."""
    assert invert({}) == {}


def test_invert_single_pair():
    """Use case: a one-pair dictionary should return the key and value flipped."""
    assert invert({"apple": "red"}) == {"red": "apple"}


def test_invert_multiple_pairs():
    """Use case: a dictionary with multiple unique values should invert successfully."""
    input_dict = {"a": "1", "b": "2", "c": "3"}
    expected = {"1": "a", "2": "b", "3": "c"}
    assert invert(input_dict) == expected


import pytest


def test_invert_duplicate_values():
    """Edge case: if values are not unique, a KeyError should be raised."""
    with pytest.raises(KeyError):
        invert({"a": "x", "b": "x"})


def test_count_empty_list():
    """Edge case: counting an empty list should return an empty dictionary."""
    assert count([]) == {}


def test_count_unique_values():
    """Use case: a list where all items are unique."""
    assert count(["apple", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 1,
        "cherry": 1,
    }


def test_count_with_duplicates():
    """Use case: a list with some repeated values."""
    assert count(["cat", "dog", "cat", "cat", "dog"]) == {"cat": 3, "dog": 2}


def test_favorite_color_clear_winner():
    """Use case: one color clearly appears the most."""
    input_dict = {"Alice": "blue", "Bob": "blue", "Cara": "red"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_tie():
    """Edge case: two colors appear the same number of times; first one in order wins."""
    input_dict = {"Alice": "blue", "Bob": "red", "Cara": "blue", "Dan": "red"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_single_entry():
    """Use case: only one person with one favorite color."""
    input_dict = {"Eve": "green"}
    assert favorite_color(input_dict) == "green"


def test_bin_len_empty():
    """Edge case: an empty list should return an empty dictionary."""
    assert bin_len([]) == {}


def test_bin_len_unique_lengths():
    """Use case: each word has a different length."""
    assert bin_len(["hi", "yes", "hello"]) == {2: {"hi"}, 3: {"yes"}, 5: {"hello"}}


def test_bin_len_duplicates():
    """Use case: multiple words with same length and repeats."""
    assert bin_len(["the", "quick", "the", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
