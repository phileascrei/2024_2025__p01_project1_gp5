ask_for_the_init_number = "Le nombre ? : "
ask_again_for_the_init_number_text = "Le nombre put*** ! :"


def is_a_valid_number(number) :
    i = 0
    is_a_valid_char = True
    while is_a_valid_char() :
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char


def check_char_number_validity () :
    pass


def ask_for_the_init_number () :
    init_number = intput(ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_number
