from game import add_points

def test_add_points():
    assert add_points(0, 1) == 1
    assert add_points(5, 3) == 8
