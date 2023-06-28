from cryptography import Caesar, Vigenere, KeywordCipher,Morse,Binary,Atbash

def mainMenu():
    print("Welcome to the main menu \n"
          "Actions you can perform: \n"
          "1- Message Encryption \n"
          "2- Message Decryption \n"
          "3- Email Sending \n"
          "4- Email Reading \n"
          "5- Exit")

def encodeMenu():
    print("Encryption Types: \n"
          "1- Caesar Cipher \n"
          "2- keyword Cipher \n"
          "3- Vigenere Substitution \n"
          "4- Morse Code \n"
          "5- Binary Code \n"
          "6- Atbash Cipher \n"
          "9- Main Menu")

def decodeMenu():
    print("Decryption Types: \n"
          "1- Caesar Cipher \n"
          "2- keyword Cipher \n"
          "3- Vigenere Substitution \n"
          "4- Morse Code \n"
          "5- Binary Code \n"
          "6- Atbash Cipher \n"
          "9- Main Menu")


# Main function
def main():
    while True:
        mainMenu()
        option = input("Choose an option: ")

        if option == "1":
            while True:
                message = input("Enter the message you want to encrypt: ")
                encodeMenu()
                encodeOption = input("Choose an option: ")
                if encodeOption == "1":
                    Caesar.encrypt(message)
                elif encodeOption == "2":
                    key = str(input('Enter the key (a word) you want to use to encode your message: \n'))
                    KeywordCipher.encrypt(message, key)
                elif encodeOption == "3":
                    shift = int(input('Enter the shift value you want to use to encode your message: \n'))
                    Vigenere.encrypt(message, shift)
                elif encodeOption == "4":
                    Morse.encrypt(message)
                elif encodeOption == "5":
                    Binary.encrypt(message)
                elif encodeOption == "6":
                    Atbash.encrypt(message)
                elif encodeOption == "7":
                    break
                else:
                    print("Invalid option. Please choose a valid option.")

        elif option == "2":
            while True:
                message = input("Enter the message to decrypt: ")
                decodeMenu()
                decodeOption = input("Choose an option: ")
                if decodeOption == "1":
                    Caesar.decrypt(message)
                elif decodeOption == "2":
                    key = str(input('Enter the key you want to use to encode your message: \n'
                                    '(It must be the same key used to encrypt the message) \n'))
                    KeywordCipher.decrypt(message, key)
                elif decodeOption == "3":
                    shift = int(input('Enter the shift value you want to use to encode your message: \n'\
                                      '(It must be the same shift used to encrypt the message) \n'))
                    Vigenere.decrypt(message, shift)
                elif decodeOption == "4":
                    Morse.decrypt(message)
                elif decodeOption == "5":
                    Binary.decrypt(message)
                elif decodeOption == "6":
                    Atbash.decrypt(message)
                elif decodeOption == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose a valid option.")
        elif option == "3":
            print("You have chosen option 3.")
            # Here you can add the logic for option 3
        elif option == "4":
            print("You have chosen option 4.")
            # Here you can add the logic for option 4
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the program
main()