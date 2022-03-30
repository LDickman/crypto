# crypto.py
# CS 220 Lab 2- Encrypting and Decrypting Text Files
# Lauren Dickman
# Monday, November 18, 2019

# See: https://pythonspot.com/tk-file-dialogs/
from tkinter import *
from tkinter.filedialog import *

# Global Constants: Define the working alphabet
# The "working alphabet" is a section of the ASCII alphabet,
# starting from FIRST_CHAR and ending with LAST_CHAR (inclusive).
FIRST_CHAR = ' '
LAST_CHAR = '~'
ALPHA_SIZE = ord(LAST_CHAR) - ord(FIRST_CHAR) + 1

# Provided Helper Functions -- Use them!

###
# function:  is_in_alphabet
# parameter: my_char, a string of length 1
# return:    True if my_char is in our working alphabet
###
def is_in_alphabet(my_char):
    return FIRST_CHAR <= my_char <= LAST_CHAR

###
# function:  print_infile_prompt
# parameter: mode, a string
# note:      Call this function with mode = "encoding!" or mode = "decoding!".
###
def print_infile_prompt(mode):
    print("\nReady for Caesar cipher " + mode)
    print("I'm going to ask you to find your INPUT text file for me.")
    print("The input file should hold the message to be encoded/decoded,", end=" ")
    print("composed of upper-case letters and (optional) other stuff.\n")

###
# function:  get_infile
# parameter: mode, a string
# return:    filepath for reading the message to be encoded/decoded
# note:      Call this function with mode = "encoding!" or mode = "decoding!".
###
def get_infile(mode):
    print_infile_prompt(mode)
    root = Tk()  # open Tkinter window
    infile_location = askopenfilename(title = "Select Input Text File")
    root.destroy()  # close Tkinter window
    infile = open(infile_location, "r")  # open file for reading
    return infile

###
# function:  get_outfile
# return:    filepath for writing the message to be encoded/decoded
###
def get_outfile():
    print("\nNext I'll to ask you to find your OUTPUT text file for me.")
    root = Tk()  # open Tkinter window
    outfile_location = asksaveasfilename(title = "Select Output Text File")
    root.destroy()  # close Tkinter window
    outfile = open(outfile_location, "w")  # open file for writing
    return outfile

########## Helper functions for students to implement ##########

###
# function: get_user_action
# return:   an integer, either 1, 2, or 3, indicating user's intended action
# note:     Repeatedly prints a menu of options until the user makes a valid
#              selection. Invalid inputs should NOT cause the program to crash.
###
def get_user_action():
    print("\nEnter a digit to choose action.")
    print("   1: ENCODE")
    print("   2: DECODE")
    print("   3: QUIT")
    while True:
        num = input()
        if (num == '1' or num == '2' or num == '3'):
            return int(num)
        print("Try again! Enter a digit: 1, 2, or 3.")
    
###
# function:  get_shift_from_user
# return:    an integer for calculating the Caesar cipher
# note:      Asks the user for an input string until the user enters
#               a string that can be converted to an integer. Invalid
#               inputs should NOT cause the program to crash.
###
def get_shift_from_user():
    while True:
        print("Give me the ENCODING shift for your cipher, any integer: ")
        encoding = input()
        if can_convert_to_integer(encoding) == True:
            return int(encoding)
        else:
            print("Try again! Please enter an integer.")

###
# function:  can_convert_to_integer
# parameter: in_string, a string
# return:    True if in_string is the string version of an integer:
#               a. begins with a digit or hyphen (i.e., negative sign)
#               b. has at least one digit
#               c. except for the optional hyphen at the front, has ONLY digits
# note:      Invalid inputs should NOT cause the program to crash.
###
def can_convert_to_integer(in_string):
    checking_for_numbers(in_string)
    num = 0
    while len(in_string) > num:
        if "0" <= in_string[num] <= "9":
            num = num + 1
        elif num == 0 and in_string[num] == '-' and len(in_string) > 1:
            num = num + 1
        else:
            return False
    return True
    
def checking_for_numbers(in_string):
    if (in_string[0] == '-') and len(in_string) == 1:
        return False

###
# function:  get_shifted_offset
# parameter: my_char, a single character from our working alphabet
# parameter: shift, an integer for encoding Caesar cipher
# return:    an integer, the offset (relative to the first character in our
#               working alphabet) for the ENCODED version of my_char
###
def get_shifted_offset(my_char, shift):
    offset = ord(my_char) - ord(FIRST_CHAR)
    shifted_offset = (offset + shift) % ALPHA_SIZE
    return shifted_offset

###
# function:  encode_char
# parameter: my_char, a string of length 1
# parameter: shift, an integer for encoding Caesar cipher
# return:    ENCODED version of my_char
# note:      If my_char is not in our working alphabet, returns my_char
#               (unchanged).
###
def encode_char(my_char, shift):
    if not is_in_alphabet(my_char):
        return my_char
    num = get_shifted_offset(my_char, shift)
    new_offset = ord(FIRST_CHAR) + num
    return chr(new_offset)

###
# function:  encode_str
# parameter: my_str, a string to be encoded
# parameter: shift, an integer for encoding Caesar cipher
# return:    ENCODED version of my_str
# note:      Uses encode_chr to encode each character of my_str.
###
def encode_str(my_str, shift):
    new_str = ""
    for l in my_str:
        new_l = encode_char(l, shift)
        new_str = new_str + new_l
    return new_str

###
# function:  write_to_outfile
# parameter: content, a string
# note:      Uses get_outfile to obtain a filepath from the user, and prints a
#               message after content has been written to that file. No return.
###
def write_to_outfile(content):
    newfile = get_outfile()
    newfile.write(content)
    print("\nOutput written successfully to this location:") 
    print("   " + newfile.name)

###
# function:  encode_from_file
# note:      Uses get_infile to obtain a filepath from the user, reads the
#               provided text file, encodes that text using Caesar cipher,
#               and writes the encoded message to another file.
###
def encode_from_file():
    mode = "encoding!"
    myfile = get_infile(mode)
    file_contents = myfile.read()
    shift = get_shift_from_user()
    print("ENCODING NOW...")
    new_words = encode_str(file_contents, shift)
    write_to_outfile(new_words)

###
# function:  decode_from_file
# note:      Uses get_infile to obtain a filepath from the user, reads the
#               provided text file, decodes that text using Caesar cipher,
#               and writes the decoded message to another file.
###
def decode_from_file():
    mode = "decoding!"
    myfile = get_infile(mode)
    file_contents = myfile.read()
    shift = -1 * get_shift_from_user()
    print("DECODING NOW...")
    new_words = encode_str(file_contents, shift)
    write_to_outfile(new_words)

###
# function: main
#
# Repeatedly asks the user whether they want to encode a message, decode a
#    message, or quit. Calls appropriate helper functions to carry out action
#    for user. CODE PROVIDED.
#
###
def main():
    while True:
        action = get_user_action()
        if action == 1:  # ENCODE
            encode_from_file()
        elif action == 2:  # DECODE
            decode_from_file()
        elif action == 3:  # QUIT
            print("\nBye!")
            return  # stops the execution

main()
