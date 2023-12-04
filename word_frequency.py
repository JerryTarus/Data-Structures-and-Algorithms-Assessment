import string

def word_frequency(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        cleaned_word = word.strip(string.punctuation).lower()
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return word_count

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
