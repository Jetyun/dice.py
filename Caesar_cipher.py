# ceasar cipher (encryption and decryption)

# cons
# only 25 tries needed to decrypt the message
# frequency of alphabets (if the message is long enough, and the shift of alphabet remain the same for whole msg)

# the encryption

def caesar_cipher(not_encrypted_txt, shift_number):
    import string
    unmodded_lowercase = string.ascii_lowercase
    unmodded_uppercase = string.ascii_uppercase
    listed_lowercase = list(unmodded_lowercase)
    listed_uppercase = list(unmodded_uppercase)
    listed_modded_lowercase = listed_lowercase[shift_number:]+listed_lowercase[:shift_number]
    listed_modded_uppercase = listed_uppercase[shift_number:]+listed_uppercase[:shift_number]
    modded_lowercase = ''.join(listed_modded_lowercase)
    modded_uppercase = ''.join(listed_modded_uppercase)
    lower_trans = not_encrypted_txt.maketrans(unmodded_lowercase, modded_lowercase)
    upper_trans = not_encrypted_txt.maketrans(unmodded_uppercase, modded_uppercase)
    lower_encrypted_txt = not_encrypted_txt.translate(lower_trans)
    fully_encrypted_txt = lower_encrypted_txt.translate(upper_trans)
    print(fully_encrypted_txt)


caesar_cipher("fuck you", 4)

# the decryption of caesar_cipher


def caesar_cipher_brute_force(fully_encrypted_txt):
    import string
    unmodded_lowercase = string.ascii_lowercase
    unmodded_uppercase = string.ascii_uppercase
    listed_lowercase = list(unmodded_lowercase)
    listed_uppercase = list(unmodded_uppercase)
    print("Here is the list of 25 possibilities ")
    decryption_tries_count = 0
    experimental_shift_order = 0
    while decryption_tries_count <= 25:
        experimental_shift_order += 1
        decryption_tries_count += 1
        listed_exp_lowercase = listed_lowercase[experimental_shift_order:] + listed_lowercase[:experimental_shift_order]
        listed_exp_uppercase = listed_uppercase[experimental_shift_order:] + listed_uppercase[:experimental_shift_order]
        exp_modded_lowercase = ''.join(listed_exp_lowercase)
        exp_modded_uppercase = ''.join(listed_exp_uppercase)
        exp_lower_trans = fully_encrypted_txt.maketrans(unmodded_lowercase, exp_modded_lowercase)
        exp_upper_trans = fully_encrypted_txt.maketrans(unmodded_uppercase, exp_modded_uppercase)
        lower_encrypted_txt = fully_encrypted_txt.translate(exp_lower_trans)
        exp_decrypted_txt = lower_encrypted_txt.translate(exp_upper_trans)
        print(exp_decrypted_txt)


caesar_cipher_brute_force("hygo csy csy wxytmh tmigi sj wlmx")

# monoalphabetic cipher


def monoalphabetic_cipher(decrypted_txt, secret_phrase):
    question = input("advance or simple (A or S)=")
    if question.upper() == "S":
        import string
        import random
        unmodded_lowercase = string.ascii_lowercase
        unmodded_uppercase = string.ascii_uppercase
        lowercase = list(unmodded_lowercase)
        listed_lowercase = list(unmodded_lowercase)
        listed_uppercase = list(unmodded_uppercase)
        random.shuffle(listed_uppercase)
        random.shuffle(listed_lowercase)
        delist_lowercase = ''.join(listed_lowercase)
        delist_uppercase = ''.join(listed_uppercase)
        print(lowercase)
        print(listed_lowercase)
        print(listed_uppercase)
        lower_trans = decrypted_txt.maketrans(unmodded_uppercase, delist_uppercase)
        upper_trans = decrypted_txt.maketrans(unmodded_lowercase, delist_lowercase)
        lower_encrypted_txt = decrypted_txt.translate(lower_trans)
        encrypted_txt = lower_encrypted_txt.translate(upper_trans)
    elif question.upper() == "A":
        listed_phrase = list(dict.fromkeys(list(secret_phrase)))  # remove duplicate from list
        listed_txt = list(dict.fromkeys(list(decrypted_txt)))
        listed_phrase.remove(' ')
        listed_txt.remove(' ')
        print(listed_txt)
        print(listed_phrase)
        if len(listed_phrase) > len(listed_txt):
            joined_txt = ''.join(listed_txt)
            modded_phrase = listed_phrase[:len(listed_txt)]
            secret_phrase = ''.join(modded_phrase)
        elif len(listed_txt) > len(listed_phrase):
            modded_txt = listed_txt[:len(listed_phrase)]
            joined_txt = ''.join(modded_txt)
            secret_phrase = ''.join(listed_phrase)
        elif len(listed_txt) == len(listed_phrase):
            joined_txt = ''.join(listed_txt)
            secret_phrase = ''.join(listed_phrase)
        trans = decrypted_txt.maketrans(joined_txt, secret_phrase)
        encrypted_txt = decrypted_txt.translate(trans)
    print(encrypted_txt)


monoalphabetic_cipher("mother and father is a stupid piece of shit", "my house pc is at taman miharja")


def string_freq_checker(fully_encrypted_txt):
    encrypted_alphabet_freq = {}
    for alphabet in fully_encrypted_txt:
        if alphabet in encrypted_alphabet_freq:
            encrypted_alphabet_freq[alphabet] += 1
        else:
            encrypted_alphabet_freq[alphabet] = 1
    print(encrypted_alphabet_freq)

string_freq_checker("DJ DK C QLXDWI WF SDGDU PCX. XLRLU KQCSLKBDQK, KJXDHDET FXWZ C BDIILE RCKL, BCGL PWE JBLDX FDXKJ GDSJWXO CTCDEKJ JBL LGDU TCUCSJDS LZQDXL. IYXDET JBL RCJJUL, XLRLU KQDLK ZCECTLI JW KJLCU KLSXLJ QUCEK JW JBL LZQDXL’K YUJDZCJL PLCQWE, JBL ILCJB KJCX, CE CXZWXLI KQCSL KJCJDWE PDJB LEWYTB QWPLX JW ILKJXWO CE LEJDXL QUCELJ. QYXKYLI RO JBL LZQDXL’K KDEDKJLX CTLEJK, QXDESLKK ULDC XCSLK BWZL CRWCXI BLX KJCXKBDQ, SYKJWIDCE WF JBL KJWULE QUCEK JBCJ SCE KCGL BLX QLWQUL CEI XLKJWXL FXLLIWZ JW JBL TCUCVO")


