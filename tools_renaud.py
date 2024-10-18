from data import *


def is_a_valid_base (base) :
    return base in bases_accepted


def ask_for_the_init_base(init_number) :

    init_base = input(ask_for_the_init_base_text)

    while True:

        # Vérifiez la validité du nombre initial par rapport à la base
        validity = check_validity_of_init_number_for_init_base(init_number)

        if is_a_valid_base(init_base):
            if validity == (True, True, True):
                return init_base  # Toutes les vérifications sont passées
            elif validity == (False, True, True):
                if init_base == "2":
                    init_base = input(non_accepted_base)
                      # Redemander l'entrée
                else :
                    return init_base
            elif validity == (False, False, True):
                if init_base in ["2", "10"]:
                    init_base = input(non_accepted_base)
                      # Redemander l'entrée
                else :
                    return init_base
        else:
            init_base = input(non_accepted_base) # Message d'erreur pour une entrée invalide
# WIP


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
# fonction a rtefaire


# rentrer un nombre en base hex
# qu'on convertit en base bin
# qui ne comprend que de éléments : 0 et 1 
# contrairement au nombre entrée qui comprend 16 éléments : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e ou 

# def hex_to_bin (hex_number):
#     bin_number = 0 

#     return bin_number

# def bin_to_hex (bin_number): 
#     hex_number = 0
#     return hex_number

def hex_to_bin(hex_number):
    bin_number = ''

    for char in hex_number:
        bin_number += hex_to_bin_map[char]
    return bin_number



def bin_to_hex(bin_number):
    hex_number = ''

    for char in bin_number:
        hex_number += bin_to_hex_map[char]
    return hex_number