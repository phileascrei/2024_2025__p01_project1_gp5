from data import *


def is_a_valid_base (base) :
    return base in bases_accepted




# def ask_for_the_init_base (init_number) : 
#     init_base = input(ask_for_the_init_base_text)
    
#     while True :
        
#         if check_validity_of_init_number_for_init_base(init_number) == (True, True, True) and is_a_valid_base(init_base) : 
#             break
#         elif check_validity_of_init_number_for_init_base(init_number) == (False, True, True) and is_a_valid_base(init_base): 
#             if init_base == "2" :
#                 init_base = input(non_accepted_base)
#                 break
#         elif check_validity_of_init_number_for_init_base(init_number) == (False, False, True) and is_a_valid_base(init_base) : 
#            if init_base in ["2","10"] :
#                 init_base = input(non_accepted_base)
#                 break
    
#     return init_base 


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
                    continue  # Redemander l'entrée
                else :
                    return init_base
            elif validity == (False, False, True):
                if init_base in ["2", "10"]:
                    init_base = input(non_accepted_base)
                    continue  # Redemander l'entrée
                else :
                    return init_base
        else:
            print("Base initiale erronée, veuillez réessayer.")  # Message d'erreur pour une entrée invalide
# WIP


def check_validity_of_init_number_for_init_base (init_number) :
    bin_validity = False
    dec_validity = False
    hex_validity = False

    for i in init_number :
        if i in bin_number_accepted : 
            bin_validity = True 
            dec_validity = True 
            hex_validity = True 
        elif i in dec_number_accepted : 
            
            dec_validity = True 
            hex_validity = True 
        elif i in hex_number_accepted : 
            
            hex_validity = True
    return bin_validity, dec_validity, hex_validity
# fonction a rtefaire