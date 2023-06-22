class Cesar:
    @staticmethod
    def encode(message):
        message = message.upper()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encryptedAlphabet = list("DEFGHIJKLMNOPQRSTUVWXYZABC")
        encodedMessage = ""
        for letter in message:
            if letter == " ":
                encodedMessage += " "
            elif letter in alphabet:
                index = alphabet.index(letter)
                encodedMessage += encryptedAlphabet[index]
        return encodedMessage

    @staticmethod
    def decode(message):
        message = message.upper()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encryptedAlphabet = list("DEFGHIJKLMNOPQRSTUVWXYZABC")
        decodedMessage = ""

        for letter in message:
            if letter == " ":
                decodedMessage += " "
            elif letter in encryptedAlphabet:
                index = encryptedAlphabet.index(letter)
                decodedMessage += alphabet[index]
        return decodedMessage
    
class Vigenere:
    @staticmethod
    def cifrar(texto, clave):
        # Implementa la lógica de cifrado Vigenère
        # ...
        return texto_cifrado

    @staticmethod
    def descifrar(texto_cifrado, clave):
        # Implementa la lógica de descifrado Vigenère
        # ...
        return texto_descifrado
    
class KeywordCipher: 
    @staticmethod
    def cifrar(texto, clave):
        # Implementa la lógica de cifrado KeywordCipher
        # ...
        return texto_cifrado

    @staticmethod
    def descifrar(texto_cifrado, clave):
        # Implementa la lógica de descifrado KeywordCipher
        # ...
        return texto_descifrado
    
class Morse:
    @staticmethod
    def cifrar(texto):
        # Implementa la lógica de cifrado Morse
        # ...
        return texto_cifrado

    @staticmethod
    def descifrar(texto_cifrado):
        # Implementa la lógica de descifrado Morse
        # ...
        return texto_descifrado
    
class Binary: 
    @staticmethod
    def cifrar(texto):
        # Implementa la lógica de cifrado Binary
        # ...
        return texto_cifrado

    @staticmethod
    def descifrar(texto_cifrado):
        # Implementa la lógica de descifrado Binary
        # ...
        return texto_descifrado
    
class Atbash: 
    @staticmethod
    def cifrar(texto):
        # Implementa la lógica de cifrado Atbash
        # ...
        return texto_cifrado

    @staticmethod
    def descifrar(texto_cifrado):
        # Implementa la lógica de descifrado Atbash
        # ...
        return texto_descifrado