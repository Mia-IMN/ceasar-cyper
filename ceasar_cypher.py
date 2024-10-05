import string
from ceasar_cypher_art import logo

print(logo)

using = True

while using == True:

    user_choice = input("Do you want to Encode or Decode a message (E or D): ").lower()
    message = input("Type in your message: ")
    shift_num = int(input("Input shift number: "))

    def ED_crypt(choice, shift_num, message):
        shift_num = shift_num
        message = message
        which = choice
        EorD = 0

        if which == "e":
            print("\nHere's your Encoded result: ", end="")
            for let in message:
                EorD = ord(let) + shift_num
                for letter in string.printable:
                    if letter == chr(EorD):
                        print(letter, end="")
        elif which == "d":
            print("\nHere's your Decoded result: ", end="")
            for let in message:
                EorD = ord(let) - shift_num
                for letter in string.printable:
                    if letter == chr(EorD):
                        print(letter, end="")

        else:
            print("Error!! \nChoose valid option!")
    

    ED_crypt(user_choice, shift_num, message)

    want_to_continue = input("\n\nDo you want to continue(Y/N): ").lower()
    print()

    if want_to_continue == "n":
        using = False
        print("******Program Terminated******\n")