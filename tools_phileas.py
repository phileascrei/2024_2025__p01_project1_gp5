from data import *



def ask_for_the_init_number () : 
    init_number = input(ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_number


def is_a_valid_number(number) : # vérifie si le nombre entrer est accepter.
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def is_a_bin_number (bin_str) : # vérifie si le nombre entrer est binaire 
    for char in bin_str:
        if char not in bin_number_accepted :
            return False
    return True

def is_a_dec_number(dec_str) : # vérifie si le nombre entrer est décimale
    for char in dec_str:
        if char not in dec_number_accepted :
            return False
    return True

def is_a_hex_number(hex_str) :  # vérifie si le nombre entrer est hexadécimale
    for char in hex_str:
        if char not in hex_number_accepted:
            return False
    return True

def check_char_number_validity (char) : # vérifie si le nombre est valide 
    return char in hex_number_accepted

def get_length(chaine):
    cpt = 0
    for char in chaine:
        cpt += 1
    return cpt





def dec_to_bin(dec_number) :
    binary_number = ""
    if is_a_dec_number(dec_number) :
        dec_number = int(dec_number)

    while dec_number > 0:
        remainder = dec_number % 2
        binary_number = str(remainder) + binary_number 
        dec_number //= 2

    return binary_number                                                                                                

def bin_to_dec(bin_number):
    result = 0
    length = len(bin_number)

    for i in range(length):
        bit = int(bin_number[length - 1 - i])  
        result += bit * (2 ** i) 
    return result

