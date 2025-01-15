def to_alternating_caps(text):
    return ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text))
print(to_alternating_caps("Hello world"))