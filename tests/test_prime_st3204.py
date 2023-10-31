from prime_st3204 import is_prime

def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(15)
    assert is_prime(17)
