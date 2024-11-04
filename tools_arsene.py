from data import *


def ask_for_the_target_base() :
    target_base = input (ask_for_the_target_base_text)
    while not (is_a_valid_base (target_base)) :
        target_base = input(ask_again_for_the_target_base_text)
    return target_base

def is_a_valid_base(base) :
    if base in bases_accepted : 
        return True
    return False

def dec_to_hex(dec_number):

    result = ""
    dec_number = int(dec_number)
    
    if dec_number == 0:
        return "0"

    while dec_number > 0:
        remainder = dec_number % 16
        result = dec_to_hex_map[remainder] + result  
        dec_number = dec_number // 16
    return result

def hex_to_dec(hex_number):
    hex_number = capitalize(hex_number)
    decimal_value = 0
    length = get_length(hex_number)

    for i in range(length):
        char = hex_number[length - 1 - i]
        if char in hex_to_dec_map:
            decimal_value += int(hex_to_dec_map[char]) * (16 ** i)

    return str(decimal_value)



def capitalize (chain) :
    upper_chain = ""
    for char in chain :
        if char in lowercase_alphabet :
            upper_chain += (uppercase_alphabet[lowercase_alphabet.index(char)])
        else :
            upper_chain += char
    return upper_chain

def get_length(chaine):
    cpt = 0
    for char in chaine:
        cpt += 1
    return cpt
