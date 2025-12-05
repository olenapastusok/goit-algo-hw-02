from collections import deque

def is_palindrome(data: str):

    cleaned_data = ''.join(ch.lower() for ch in data if ch.isalnum())

    d = deque(cleaned_data)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    
    return True


def test_is_palindrome():
    test_cases = [
        ("А роза упала на лапу Азора", True),
        ("Hello", False),
        ("Мадам", True),
        ("12321", True),
        ("12345", False),
        ("Never odd or even", True),
        ("Was it a car or a cat I saw", True),
        ("Python", False),
    ]
    
    for data, expected in test_cases:
        result = is_palindrome(data)
        print(f"'{data}' -> {result} (очікувано: {expected})")

test_is_palindrome()