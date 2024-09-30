from data import *


def ask_for_the_target_base() :
    target_base = input (ask_for_the_target_base_text)
    while not (is_a_valid_base (target_base)) :
        target_base = input(ask_again_for_the_target_base_text)
    return init_number
    
    
    
    