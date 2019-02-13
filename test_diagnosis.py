import pytest


@pytest.mark.parametrize('s,expected', [
    ([1, 2, 3], "normal thyroid function"),
    ([.5, 2, 3], "hyperthyroidism"),
    ([5, 4, 3], "hypothyroidism"),
    ([4, 3, 2, 1], "normal thyroid function")
])
def test_exact(s, expected):
    from tsh import diagnose
    answer = diagnose(s)
    assert answer == expected
