import pytest


@pytest.mark.parametrize('s,expected', [
    ([1, 2, 3], "normal thyroid function"),
    ([.5, 2, 3], "hyperthyroidism"),
    ([5, 4, 3], "hypothyroidism"),
    ([4, 3, 2, 1], "normal thyroid function")
])
def test_diagnosis(s, expected):
    """Tests whether the diagnose function is correct

    Args:
        s (list): TSH measurements
        expected (str): correct output

    Returns:

    """
    from tsh import diagnose
    answer = diagnose(s)
    assert answer == expected
