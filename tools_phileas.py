from data import *

def is_a_valid_number(number) : # vérifie si le nombre entrer est accepter.
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def is_a_bin_number(bin_str): # vérifie si le nombre entrer est binaire 
    return isinstance(bin_str, str) and all(char in bin_number_accepted for char in bin_str)

def is_a_dec_number(dec_str): # vérifie si le nombre entrer est décimale
    return isinstance(dec_str, str) and all(char in dec_number_accepted for char in dec_str)

def is_a_hex_number(hex_str): # vérifie si le nombre entrer est hexadécimale
    return isinstance(hex_str, str) and all(char in hex_number_accepted for char in hex_str)


def check_char_number_validity (char) : # vérifie si le nombre est valide 
    return char in hex_number_accepted

def ask_for_the_init_number () : 
    init_number = input(ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_number


def bin_to_dec (bin_number) :
    return int(bin_number, 2)
#A modifier, ne pas utiliser la fonction de python

def dec_to_bin(dec_number) :
    binary_number = ""
    if is_a_dec_number(dec_number) :
        dec_number = int(dec_number)
    while dec_number > 0:
        remainder = dec_number % 2  # Obtenir le reste
        binary_number = str(remainder) + binary_number  # Ajouter le bit à la chaîne
        dec_number //= 2  # Diviser par 2

    return binary_number                                                                                                
