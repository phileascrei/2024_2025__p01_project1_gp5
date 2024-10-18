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


def dec_to_hex(dec_number_str):
    # Convertir la chaîne en entier
    try:
        dec_number = int(dec_number_str)
    except ValueError:
        raise ValueError("L'entrée doit être une chaîne représentant un nombre entier.")

    if dec_number < 0:
        return "-" + dec_to_hex(str(-dec_number))
    
    hex_digits = "0123456789ABCDEF"
    if dec_number == 0:
        return "0"
    
    hex_value = ""
    while dec_number > 0:
        remainder = dec_number % 16
        hex_value = hex_digits[remainder] + hex_value
        dec_number //= 16
    
    return hex_value

def hex_to_dec(hex_number):
    hex_digits = "0123456789ABCDEF"
    hex_number = capitalize(hex_number)
    decimal_value = 0
    length = len(hex_number)

    for i in range(length):
        digit = hex_number[length - 1 - i] 
        is_valid = False
        for j in range(len(hex_digits)):
            if digit == hex_digits[j]:
                decimal_value += j * (16 ** i)
                is_valid = True
                break
        if not is_valid:
            print("n'est pas un chiffre hexadécimal valide.")
    return decimal_value



def capitalize (chain) :
    upper_chain = ""
    for char in chain :
        if char in lowercase_alphabet :
            upper_chain += (uppercase_alphabet[lowercase_alphabet.index(char)])
        else :
            upper_chain += char
    return upper_chain