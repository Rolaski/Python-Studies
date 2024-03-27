def histogram(file_path):
    # Initialize an empty dictionary to store character frequencies
    char_freq = {}

    # Open the file and read its content
    with open(file_path, 'r') as file:
        text = file.read()

    # Count the frequency of each character in the text
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq


# Test the function
file_path = "document.txt"
result = histogram(file_path)
print("Document contains text:", result)
