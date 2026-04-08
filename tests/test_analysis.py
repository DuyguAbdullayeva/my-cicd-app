from analysis import compute_statistics

def test_mean():
    assert compute_statistics([10, 20, 30])["mean"] == 20.0

def test_min_max():
    result = compute_statistics([5, 15, 25])
    assert result["min"] == 5
    assert result["max"] == 25
