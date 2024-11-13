from tools import *
from data import *

def do_the_job (): 
    while True :

        init_number = ask_for_the_init_number ()
        init_base = ask_for_the_init_base (init_number)
        target_base = ask_for_the_target_base ()

        bin_dec_hex_to_bin_dec_hex(init_number, init_base, target_base)

        if asking_for_retry() != True :
            break
        

do_the_job()