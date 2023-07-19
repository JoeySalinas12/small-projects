LETTERS = 'abcdefghijklmnopqrstuvwxyz'
DISPLACEMENT = 13
CODED_STRING = "TUBFG"


def find_letter_position(string:str) -> str:
    '''Accepts a string as input and decodes the string using a displacement defined earlier in the script. E.g. if the
    displacement is 13 then the function will take each letter in the string provided and count 13 places backwards in
    the alphabet to find the new corresponding letter.

    Args:
        string (str): A string of characters that needs to be decoded

    Returns:
        str: The decoded string of characters
    '''
    new_word_list = []
    for letter in string.lower():

        if letter in LETTERS:
            position = LETTERS.rfind(letter)
            placement = position - DISPLACEMENT
            new_word_list.append(LETTERS[placement])
        else:
            new_word_list.append(letter)

    new_word = "".join(new_word_list)
    return new_word


def main():
    decoded_string = find_letter_position(CODED_STRING)
    print(decoded_string)


if __name__ == "__main__":
    main()