def generate_substrings(text):
    for i in range(1, len(text) + 1):
        yield text[:i]


# Test the generator function
text = "spam"
substrings = list(generate_substrings(text))
print(substrings)
