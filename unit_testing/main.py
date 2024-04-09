def add(a, b):
    """Add two numbers."""
    return a + b

def concatenate(str1, str2):
    """Concatenate two strings."""
    return str1 + str2

def find_maximum(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def convert_to_dictionary(list_of_tuples):
    """Convert a list of tuples into a dictionary."""
    return dict(list_of_tuples)
