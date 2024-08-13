def print_upper_words(words):
    for word in words:
        print(word.upper())


def print_upper_words_E(words):
    for word in words:
        if word.startswith("e") or words.startswith("E"):
            print(word.upper())


def print_upper_words_must_start_with(words, start_with):
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})