import random
import string
alphabet = list(string.ascii_letters)
number = list(string.digits)
punctuation = list(string.punctuation)
all_cha = alphabet+number+punctuation
blank_list = ""
length_of_password = input("how long you need your password to be(insert digit)= ")
unlowered_response=input("repeat(y or n)? ")
response=unlowered_response.lower()


while response=="y":
    for password in range(int(length_of_password)):
        blank_list += random.choice(all_cha)
    print(blank_list)
    blank_list = ""
    unlowered_response = input("repeat(y or n)? ")
    response = unlowered_response.lower()
if response != "y":
    print("password generator ended")
