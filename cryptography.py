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
    def adaptKeyInWord(word, key):
        keyByWordSize = key * (len(word) // len(key))
        keyByWordSize += key[: len(word) % len(key)]
        return keyByWordSize

    @staticmethod
    def adaptKeyInMessage(message, key):
        messageInWords = message.split(" ")
        messageInKey = " ".join(
            KeywordCipher.adaptKeyInWord(word, key) for word in messageInWords)
        return messageInKey

    def letterToNumericValue(letter):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return alphabet.index(letter) + 1

    def valueToLetter(value):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return alphabet[value - 1]

    def encodeWordWithKey(word, key):
        encodedWord = ""
        for letter, key_letter in zip(word, key):
            letterSum = KeywordCipher.letterToNumericValue(letter) + KeywordCipher.letterToNumericValue(key_letter)
            if letterSum > 26:
                letterSum -= 26
            encodedWord += KeywordCipher.valueToLetter(letterSum)
        return encodedWord

    @staticmethod
    def encode(message, key):
        message = message.upper()
        key = key.upper()
        messageInWords = message.split(" ")
        keyAdapted = KeywordCipher.adaptKeyInMessage(message, key)
        keyInWords = keyAdapted.split(" ")
        encodedMessage = " ".join(KeywordCipher.encodeWordWithKey(word, key_word) for word, key_word in zip(messageInWords, keyInWords))
        return encodedMessage.capitalize()

    @staticmethod
    def decodeWordWithKey(word, key):
        word = word.upper()
        key = key.upper()
        decodedWord = ""
        for word_letter, key_letter in zip(word, key):
            letter_difference = KeywordCipher.letterValue(word_letter) - KeywordCipher.letterValue(key_letter)
            if 0 < letter_difference <= 26:
                decodedWord += KeywordCipher.letterFromValue(letter_difference)
            else:
                decodedWord += KeywordCipher.letterFromValue(letter_difference + 26)
        return decodedWord
    
    @staticmethod
    #Ver si agregar la funcion de crear cadena
    def decode(message, key):
        message = message.upper()
        key = key.upper()
        messageWords = message.split(" ")
        adaptedKey = KeywordCipher.adaptKeyToMessage(message, key)
        keyWords = adaptedKey.split(" ")
        decodedMessage = ""

        for word, key_word in zip(messageWords, keyWords):
            decodedWord = KeywordCipher.decodeWordWithKey(word,key_word)
            decodedMessage += decodedWord + " "

        return decodedMessage[:-1].capitalize()


class Morse:
    @staticmethod
    def encodeWordInMorse(word):
        alphabet = ["A", "B", "C", "CH", "D", "E", "F", "G", "H", "I", "J",
                    "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
                    "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    ".", ",", "?", '"', "/"]

        morseCode = ["·—", "—···", "—·—·", "————", "—··", "·",
                    "··—·", "——·", "····", "··", "·———", "—·—", "·—··",
                    "——", "—·", "——·——", "———", "·——·", "——·—", "·—·", "···",
                    "—", "··—", "···—", "·——", "—··—", "—·——", "——··", "—————",
                    "·————", "··———", "···——", "····—", "·····", "—····",
                    "——···", "———··", "————·", "·—·—·—", "——··——",
                    "··——··", "·—··—·", "—··—·"]

        encodedWord = ""

        for char in word:
            if char in alphabet:
                charIndex = alphabet.index(char)
                encodedWord += morseCode[charIndex] + "*"

        return encodedWord[:-1]
    
    @staticmethod
    def encode(message):
        messageList = message.upper().split(" ")
        encodedMessage = ""

        for word in messageList:
            encodedMessage += Morse.encodeWordInMorse(word) + " "

        return encodedMessage.strip()

    @staticmethod
    def decodeMorseToWord(morseWord):
        letterMorse = morseWord.split("*")
        alphabet = ["A", "B", "C", "CH", "D", "E", "F", "G", "H", "I", "J",
                    "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
                    "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    ".", ",", "?", '"', "/"]

        morseCode = ["·—", "—···", "—·—·", "————", "—··", "·",
                    "··—·", "——·", "····", "··", "·———", "—·—", "·—··",
                    "——", "—·", "——·——", "———", "·——·", "——·—", "·—·", "···",
                    "—", "··—", "···—", "·——", "—··—", "—·——", "——··", "—————",
                    "·————", "··———", "···——", "····—", "·····", "—····",
                    "——···", "———··", "————·", "·—·—·—", "——··——",
                    "··——··", "·—··—·", "—··—·"]

        decodedWord = []

        for morseChar in letterMorse:
            if morseChar in morseCode:
                charIndex = morseCode.index(morseChar)
                decodedWord.append(alphabet[charIndex])
        return decodedWord
    
    @staticmethod
    # Ver si agregar la funcion de crear cadena
    def decode(message):
        morseWordList = message.split(" ")
        decodedMessage = ""

        for morseWord in morseWordList:
            decodedWord = Morse.decodeMorseToWord(morseWord)
            decodedMessage += decodedWord + " "

        return decodedMessage.strip().capitalize()


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
    def codeAndDecode(message):
        message = message.upper()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        atbashAlphabet = list("ZYXWVUTSRQPONMLKJIHGFEDCBA")
        encodedOrDecodedMessage = ""

        for char in message:
            if char == " ":
                encodedOrDecodedMessage += " "
            elif char in alphabet:
                char_index = alphabet.index(char)
                encoded_or_decoded_char = atbashAlphabet[char_index]
                encodedOrDecodedMessage += encoded_or_decoded_char

        return encodedOrDecodedMessage
