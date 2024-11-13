from data import *
from tools_phileas import *
from tools_arsene import * 


def ask_for_the_init_base(init_number) :

    init_base = input(ask_for_the_init_base_text)

    while True:

        validity = check_validity_of_init_number_for_init_base(init_number)

        if is_a_valid_base(init_base):
            if validity == (True, True, True):
                return init_base
            elif validity == (False, True, True):
                if init_base == "2":
                    init_base = input(non_accepted_base)
                else :
                    return init_base
            elif validity == (False, False, True):
                if init_base in ["2", "10"]:
                    init_base = input(non_accepted_base)
                else :
                    return init_base
        else:
            init_base = input(ask_again_for_the_init_base_text)

def is_a_valid_base (base) :
    return base in bases_accepted

def check_validity_of_init_number_for_init_base (init_number) :
    bin_validity = True
    dec_validity = True
    hex_validity = True

    for i in init_number :
        if i in bin_number_accepted : 
            pass
        elif i in dec_number_accepted : 
            bin_validity = False 
        elif i in hex_number_accepted : 
            bin_validity = False
            dec_validity = False
    return bin_validity, dec_validity, hex_validity





def hex_to_bin(hex_number):

    if hex_number == "0" :
        return "0"
    else :
        dec_number = hex_to_dec(hex_number)
        bin_number = dec_to_bin(dec_number)
        return bin_number

def bin_to_hex(bin_number):
    
    if bin_number == "0" :
        return "0"
    else :
        dec_number = bin_to_dec(bin_number)
        hex_number = dec_to_hex(dec_number)
        return hex_number
