from calculate_native_python import calculate_pi as calculate_python
from calculate_with_cffi import calculate_pi as calculate_cffi


def test_native_python():
    assert calculate_python(1) == 4
    assert 2.66 < calculate_python(2) < 2.67
    assert 3.46 < calculate_python(3) < 3.47
    assert 2.895 < calculate_python(4) < 2.896
    assert 3.3396 < calculate_python(5) < 3.3397
    assert 3.14 < calculate_python(1000) < 3.15
    assert 3.1415 < calculate_python(100_000) < 3.1416


def test_cffi():
    assert calculate_cffi(1) == 4
    assert 2.66 < calculate_cffi(2) < 2.67
    assert 3.46 < calculate_cffi(3) < 3.47
    assert 2.895 < calculate_cffi(4) < 2.896
    assert 3.3396 < calculate_cffi(5) < 3.3397
    assert 3.14 < calculate_cffi(1000) < 3.15
    assert 3.1415 < calculate_cffi(100_000) < 3.1416
