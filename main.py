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


print(hex_to_dec("Ad5fT"))