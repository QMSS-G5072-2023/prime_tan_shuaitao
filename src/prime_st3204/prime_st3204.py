import math

def is_prime(n):
    """
    Determine if a given number is a prime number.
    
    Parameters:
    - n (int): The number to check for primality.
    
    Returns:
    - bool: True if the number is prime, otherwise False.
    
    Example:
    >>> is_prime(5)
    True
    
    >>> is_prime(4)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

