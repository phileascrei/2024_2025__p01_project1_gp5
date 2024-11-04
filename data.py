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

hex_to_bin_map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A'or'a':'1010',
        'B'or'b':'1011',
        'C'or'c': '1100',
        'D'or'd': '1101',
        'E'or'e': '1110',
        'F'or'f': '1111'
    }

bin_to_hex_map = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": 'A'or'a',
        "1011": 'B'or'b',
        "1100": 'C'or'c',
        "1101": 'D'or'd',
        "1110": 'E'or'e',
        "1111": 'F'or'f'
    }

hex_to_dec_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    'A'or 'a': 10,
    'B'or'b': 11,
    'C'or'c': 12,
    'D'or'd': 13,
    'E'or'e': 14,
    'F'or'f': 15
}

dec_to_hex_map= {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A'or'a',
    11: 'B'or'b',
    12: 'C'or'c',
    13: 'D'or'd',
    14: 'E'or'e',
    15: 'F'or'f'
}

dec_to_bin_map= {
    0: "0000",
    1: "0001",
    2: "0010",
    3: "0011",
    4: "0100",
    5: "0101",
    6: "0110",
    7: "0111",
    8: "1000",
    9: "1001"
}

bin_to_dec_map= {
    "0000": 0,
    "0001": 1,
    "0010": 2,
    "0011": 3,
    "0100": 4,
    "0101": 5,
    "0110": 6,
    "0111": 7,
    "1000": 8,
    "1001": 9
}