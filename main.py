from tools import *
from data import *

def bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base) :
    target_number = None     
    return target_number  

# assert bin_dec_hex_to_bin_dec_hex ("101",2,10) == "5" 

def do_the_job (): 
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base (init_number)
    target_base = ask_for_the_target_base ()
    target_number = bin_dec_hex_to_bin_dec_hex (init_number, \
                                init_base,\
                                 target_base)

# do_the_job()
# print(dec_to_hex("10"))

print(bin_to_dec("101"))      # Sortie attendue : 5
print(bin_to_dec("1101"))     # Sortie attendue : 13
print(bin_to_dec("0"))        # Sortie attendue : 0
print(bin_to_dec("11111111"))  # Sortie attendue : 255
print(bin_to_dec("10000000"))  # Sortie attendue : 128
print(bin_to_dec("101")) 