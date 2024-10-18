ask_for_the_init_number_text = "Le nombre ? : "
ask_again_for_the_init_number_text = "Le nombre put*** ! : "

ask_for_the_target_base_text = "La base cible ? : "
ask_again_for_the_target_base_text = "La base put*** ! : "

bases_accepted = ["2", "10", "16"]

bin_number_accepted = ["0","1"]
dec_number_accepted = bin_number_accepted + ["2","3","4","5","6","7","8","9"]
hex_number_accepted = dec_number_accepted + ["a","b","c","d","e","f"] + ["A","B","C","D","E","F"]

ask_for_the_init_base_intro_text = "Dans quel base se trouve votre nombre ? \n"

ask_for_the_init_base_exept_bin_and_dec_text = ask_for_the_init_base_intro_text + " Tapez '16' s'il se trouve dans la base Hexadécimale \n"

ask_for_the_init_base_exept_bin_text = ask_for_the_init_base_exept_bin_and_dec_text + " Tapez '10' s'il se trouve dans la base Decimale \n"

ask_for_the_init_base_text = ask_for_the_init_base_exept_bin_text + " Tapez '2' s'il se trouve dans la base Binaire \n"





ask_again_for_the_init_base_text = "Base initiale eronnée, veuillez réessayer "
non_accepted_base = "La base n'est pas acceptée pour le nombre entré, entrer une autre base : "


lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"