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
    hex_number = hex_number.upper()  # Pour gérer les lettres en minuscules
    decimal_value = 0
    
    for index, digit in enumerate(reversed(hex_number)):
        if digit in hex_digits:
            decimal_value += hex_digits.index(digit) * (16 ** index)
        else:
            raise ValueError(f"'{digit}' n'est pas un chiffre hexadécimal valide.")
    
    return decimal_value

