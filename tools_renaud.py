from data import *


def is_a_valid_base (base) :
    return base in bases_accepted

def ask_for_the_init_base (init_number) : 
    init_base = input(ask_for_the_init_base_text) 
    while not (is_a_valid_base(init_base)) :
        init_base = input(ask_again_for_the_init_number_text)
    if check_validity_of_init_number_for_init_base(init_number, init_base) == [True, True, True] : 
        pass
    elif check_validity_of_init_number_for_init_base(init_number, init_base) == [False, True, True] : 
        if init_base == "2" :
            init_base = input(non_accepted_base)
    elif check_validity_of_init_number_for_init_base(init_number, init_base) == [False, False, True] : 
        # WIP


    return init_base 


def check_validity_of_init_number_for_init_base (init_number,init_base) :
    bin_validity = False
    dec_validity = False
    hex_validity = False

    for i in init_number :
        if i in bin_number_accepted : 
            bin_validity = True 
            dec_validity = True 
            hex_validity = True 
        elif i in dec_number_accepted : 
            bin_validity = False
            dec_validity = True 
            hex_validity = True 
        elif i in hex_number_accepted : 
            bin_validity = False
            dec_validity = False
            hex_validity = True
    return bin_validity, dec_validity, hex_validity







