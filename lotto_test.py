"""Test lotto draw numbers"""
from lotto import draw_numbers

def test_draw_numbers():
    "Testing draw"
    for _ in range(501):
        drawn_numbers = sorted(list(draw_numbers()))

        assert len(drawn_numbers) == 6
        assert drawn_numbers[0] >= 1
        assert drawn_numbers[-1] <= 49
