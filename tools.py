from tools_renaud import *
from tools_phileas import *
from tools_arsene import * 

# ask_for_the_init_number () -> tools_phileas.py

# ask_for_the_init_base () -> tools_renaud.py

# ask_for_the_target_base () -> tools_arsene.py

def bin_dec_hex_to_bin_dec_hex (init_number, init_base, target_base) :
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

def asking_for_retry () :
    while True:
        answer = input(retry)
        if answer == "oui" :
            return True
        elif answer == "non" :
            print(thanks)
            return False
        else:
            print(retry_error)
        
