def capitalize_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    capitalized_words = []

    for word in words:
        first_letter = word[0].upper()  # Convert the first letter to uppercase
        rest_of_word = word[1:].lower()  # Convert the rest of the letters to lowercase
        capitalized_word = first_letter + rest_of_word
        capitalized_words.append(capitalized_word)

    return capitalized_words
    

# Example usage
sentence = input("Enter a sentence: ")
capitalized_sentence = capitalize_words(sentence)
print(capitalized_sentence)


