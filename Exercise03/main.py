def check_brackets(expression):
    stack = []
    brackets_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in brackets_pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in brackets_pairs.keys():  # If it's a closing bracket
            if not stack or stack[-1] != brackets_pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

def test_check_brackets():
    test_cases = [
        ("(a + b) * {c - [d / e]}", True),
        ("(a + b] * {c - d}", False),
        ("[({})]", True),
        ("[(])", False),
        ("{[()()]}", True),
        ("{[(])}", False),
        ("", True),
        ("no brackets here", True),
    ]
    
    for expression, expected in test_cases:
        result = check_brackets(expression)
        print(f"'{expression}' -> {result} (очікувано: {expected})")

test_check_brackets()