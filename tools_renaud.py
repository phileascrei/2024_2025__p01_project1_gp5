from data import *


def is_a_valid_base (base) :
    return base in bases_accepted

def ask_for_the_init_base () : 
    init_base = input(ask_for_the_init_base_text) 
    while not (is_a_valid_base(init_base)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_base 