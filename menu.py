from cryptography import Caesar, Vigenere, KeywordCipher,Morse,Binary,Atbash

def mainMenu():
    print("Welcome to the main menu \n"
          "Actions you can perform: \n"
          "1- Message Encryption \n"
          "2- Message Decryption \n"
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
                    print(Caesar.encode(message))
                elif encodeOption == "2":
                    while True:
                        key = str(input('Enter the key (a word) you want to use to encode your message: \n'))
                        if not key.isalpha():
                            print("Invalid key. Please enter a word.")
                            continue
                        break
                    print(KeywordCipher.encode(message, key))
                elif encodeOption == "3":
                    while True:
                        shift = input('Enter the shift value you want to use to encode your message: \n')
                        if not shift.isdigit():
                            print("Invalid shift value. Please enter an integer.")
                            continue
                        shift = int(shift)
                        break
                    print(Vigenere.encode(message, shift))
                elif encodeOption == "4":
                    print(Morse.encode(message))
                elif encodeOption == "5":
                    print(Binary.encode(message))
                elif encodeOption == "6":
                    print(Atbash.encodeAndDecode(message))
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
                    print(Caesar.decode(message))
                elif decodeOption == "2":
                    while True:
                        key = str(input('Enter the key you want to use to encode your message: \n'
                                    '(It must be the same key used to encrypt the message) \n'))
                        if not key.isalpha():
                            print("Invalid key. Please enter a word.")
                            continue
                        break
                    print(KeywordCipher.decode(message, key))
                elif decodeOption == "3":
                    while True:
                        shift = int(input('Enter the shift value you want to use to encode your message: \n'\
                                      '(It must be the same shift used to encrypt the message) \n'))
                        if not shift.isdigit():
                            print("Invalid shift value. Please enter an integer.")
                            continue
                        shift = int(shift)
                        break
                    print(Vigenere.decode(message, shift))
                elif decodeOption == "4":
                    print(Morse.decode(message))
                elif decodeOption == "5":
                    print(Binary.decode(message))
                elif decodeOption == "6":
                    print(Atbash.encodeAndDecode(message))
                elif decodeOption == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose a valid option.")
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the program
main()