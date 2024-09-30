
ask_for_the_init_base_text ="Dans quel base se trouve votre nombre ? \n Tapez 2 s'il se trouve dans la base Binaire \n Tapez '10' s'il se trouve dans la base Décimale \n Tapez '16' s'il se trouvez dans la base Hexadécimale"
ask_again_for_the_init_number_text = "Base initiale eronnée, veuillez réessayer"
# exemple du prof mais pas utile :
# bin_base_chains_valid = [2,bin,b]
# dec_base_chains_valid = 
# hex_base_chains_valid = 

def is_a_valid_base (number) : 
    if number == 2 or number == 10 or number == 16 : 
        return True 
    else :
        return False 
    # exemple du prof mais pas utile :
    # return number in bin_base_chains_valid \
    # or number in dec_base_chains_valid \
    # or number in hex_base_chains_valid 

def ask_for_the_init_base () : 
    init_base = input(ask_for_the_init_base_text) 
    while not (is_a_valid_base(init_base)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_base 