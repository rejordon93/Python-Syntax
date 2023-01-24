def print_upper_words(words, must_start_with=set()):
    """
    Prints out each word in the list 'words' on a separate line, in all uppercase.
    Only words that start with one of the letters in the set 'must_start_with' are printed.
    If 'must_start_with' is not provided or is an empty set, all words will be printed.
    """
    for word in words:
        if not must_start_with or word[0].lower() in must_start_with:
            print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
