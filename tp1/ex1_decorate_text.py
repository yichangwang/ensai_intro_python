def display_title(text, input_length):
    """Display text as title style
    text: input text
    input_length: target length of the line
    """
    # find length of the longest line in test
    max_length = 0
    for line in text:
        if len(line) > max_length:
            max_length = len(line)
    # calculate adapted length
    adapted_length = max(max_length, input_length)
    length_for_asterisk = adapted_length + 2
    # print first line
    print("*" * length_for_asterisk)
    # print context
    for line in text:
        # https://docs.python.org/3.5/library/string.html#format-examples
        print('*{:{align}{length}}*'.format(line, align='^',length=adapted_length))
    print("*" * length_for_asterisk)


if __name__ == "__main__":
    my_text = [ "L'ingénieux hidalgo",
                "Don Quichotte de la Manche", "",
                "Composé par Miguel de Cervantes",
                "", "Avec privilège royal",
                "à Madrid", "en l'an de grâce 1605"]

    display_title(my_text, 40)
    display_title(my_text, 10)
