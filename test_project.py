import pytest
from project import win_checker


def main():
    test_win_checker()

def test_win_checker():
    assert win_checker([["1", "X", "", ""], ["2", "X", "", ""], ["3", "X", "", ""]]) == ["X"]
    assert win_checker([["1", "", "O", ""], ["2", "", "O", ""], ["3", "", "O", ""]]) == ["O"]


if __name__ == "__main__":
    main()
