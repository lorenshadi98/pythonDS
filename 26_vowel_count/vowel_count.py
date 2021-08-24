def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ["a", "i", "o", "e", "u"]
    new_dict = dict()
    new_phrase = phrase.lower()
    for letter in new_phrase:
        if letter in vowels:
            new_dict[letter] = new_phrase.count(letter)
    return new_dict
