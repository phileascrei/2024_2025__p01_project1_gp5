from tools import *
from data import *

def bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base) :
    target_number = None     
    return target_number  

# assert bin_dec_hex_to_bin_dec_hex ("101",2,10) == "5" 

def do_the_job (): 
    while True :

        init_number = ask_for_the_init_number ()
        init_base = ask_for_the_init_base (init_number)
        target_base = ask_for_the_target_base ()
        target_number = bin_dec_hex_to_bin_dec_hex (init_number, \
                                init_base,\
                                 target_base)
    
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
    
        while True:
                answer = input(retry)
                if answer == "oui" :
                    break  
                elif answer == "non" :
                    print(thanks)
                    return
                else:
                    print(retry_error)
        




do_the_job()

# print(bin_to_dec("101"))      # Sortie attendue : 5
# print(bin_to_dec("1101"))     # Sortie attendue : 13
# print(bin_to_dec("0"))        # Sortie attendue : 0
# print(bin_to_dec("11111111"))  # Sortie attendue : 255
# print(bin_to_dec("10000000"))  # Sortie attendue : 128
# print(bin_to_dec("101")) # Sortie attendue : 5