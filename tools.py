from data import *


"""FONCTIONS PRINCIPALES"""

def ask_for_the_init_number () : # demande d'entrer un nombre en base binaire, decimal ou hexadacimal
    init_number = input(ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) :
        init_number = input(ask_again_for_the_init_number_text)
    return init_number


def ask_for_the_init_base(init_number) : # demande d'entrer la base du nombre donner lors de la fonction ask_for_the_init_number()
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


def ask_for_the_target_base() : # demande d'entrer la base dans laquelle le nombre de la fonction ask_for_the_init_number() a la base entrer dans ask_for_the_init_base() doit etre converti
    target_base = input (ask_for_the_target_base_text)

    while not (is_a_valid_base (target_base)) :
        target_base = input(ask_again_for_the_target_base_text)
    return target_base


def bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base) : # converti en fonction des entre de l'utilisateur le nombre en la base voulue

    if init_base == "2" :
        if target_base == "2" :
            print(init_number)
        if target_base == "10" :
            print(bin_to_dec(init_number))
        if target_base == "16" :
            print(bin_to_hex(init_number))
    if init_base == "10" :
        if target_base == "2" :
           print(dec_to_bin(init_number))
        if target_base == "10" :
            print(init_number)
        if target_base == "16" :
            print(dec_to_hex(init_number))
    if init_base == "16" :
        if target_base == "2" :
            print(hex_to_bin(init_number))
        if target_base == "10" :
            print(hex_to_dec(init_number))
        if target_base == "16" :
            print(init_number)


def asking_for_retry () : # boucle permettant de demander si l'utilisateur veux refaire une convertion

    while True:
        answer = input(retry)
        if answer == "oui" :
            return True
        elif answer == "non" :
            print(thanks)
            return False
        else:
            print(retry_error)
 







"""CONVERTIONS"""

def dec_to_bin(dec_number) : # converti un nombre decimal en un nombre binaire
    binary_number = ""
    if is_a_dec_number(dec_number) :
        dec_number = int(dec_number)

    while dec_number > 0:
        remainder = dec_number % 2
        binary_number = str(remainder) + binary_number 
        dec_number //= 2

    return binary_number                                                                                                

def bin_to_dec(bin_number) : # converti un nombre binaire en nmbre decimal
    result = 0
    length = len(bin_number)

    for i in range(length):
        bit = int(bin_number[length - 1 - i])  
        result += bit * (2 ** i) 
    return result

def dec_to_hex(dec_number) : # converti un nombre decimal en nombre hexadecimal

    result = ""
    dec_number = int(dec_number)
    
    if dec_number == 0:
        return "0"

    while dec_number > 0:
        remainder = dec_number % 16
        result = dec_to_hex_map[remainder] + result  
        dec_number = dec_number // 16
    return result

def hex_to_dec(hex_number) : # converti un nombre hexadecimal en nombre decimal
    hex_number = capitalize(hex_number)
    decimal_value = 0
    length = get_length(hex_number)

    for i in range(length):
        char = hex_number[length - 1 - i]
        if char in hex_to_dec_map:
            decimal_value += int(hex_to_dec_map[char]) * (16 ** i)

    return str(decimal_value)


def hex_to_bin(hex_number) : # converti un nombre hexadecimal en nombre binaire

    if hex_number == "0" :
        return "0"
    else :
        dec_number = hex_to_dec(hex_number)
        bin_number = dec_to_bin(dec_number)
        return bin_number

def bin_to_hex(bin_number) : # converti un nombre binaire en un nombre hexadecimal
    
    if bin_number == "0" :
        return "0"
    else :
        dec_number = bin_to_dec(bin_number)
        hex_number = dec_to_hex(dec_number)
        return hex_number







"""VERIFICATIONS"""

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

def is_a_valid_base (base) : # verifie si la base entrer fait bien partit des bases gerer par le programme
    return base in bases_accepted



def check_char_number_validity (char) : # vérifie si le nombre est valide 
    return char in hex_number_accepted

def check_validity_of_init_number_for_init_base (init_number) : #  vérifie si un nombre est valide pour une base donnée
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



"""UTILITAIRES"""

def capitalize (chain) : # mette en capital la chaine de caractere entre
    upper_chain = ""
    for char in chain :
        if char in lowercase_alphabet :
            upper_chain += (uppercase_alphabet[lowercase_alphabet.index(char)])
        else :
            upper_chain += char
    return upper_chain

def get_length(chaine) : # donne le nombre de caractere d'une chaine de caractere
    cpt = 0
    for char in chaine:
        cpt += 1
    return cpt