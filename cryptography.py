class Caesar:
    @staticmethod
    def encode(message):
        message = message.upper().strip()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encryptedAlphabet = list("DEFGHIJKLMNOPQRSTUVWXYZABC")
        encodedMessage = ""
        for letter in message:
            if letter == " ":
                encodedMessage += " "
            elif letter in alphabet:
                index = alphabet.index(letter)
                encodedMessage += encryptedAlphabet[index]
        print("encodedMessage: ", encodedMessage)
        return encodedMessage.capitalize()

    @staticmethod
    def decode(message):
        message = message.upper().strip()
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encryptedAlphabet = list("DEFGHIJKLMNOPQRSTUVWXYZABC")
        decodedMessage = ""

        for letter in message:
            if letter == " ":
                decodedMessage += " "
            elif letter in encryptedAlphabet:
                index = encryptedAlphabet.index(letter)
                decodedMessage += alphabet[index]
        return decodedMessage.capitalize()

class Vigenere:
    @staticmethod
    def shiftLetter(letter, shift):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shiftedIndex = (alphabet.index(letter) + shift) % 26
        shiftedLetter = alphabet[shiftedIndex]
        return shiftedLetter

    @staticmethod
    def encodeWordVigenere(word, shift):
        encodedWord = ""
        for i, letter in enumerate(word):
            if i % 2 == 0:
                encodedWord += Vigenere.shiftLetter(letter, shift // 10)
            else:
                encodedWord += Vigenere.shiftLetter(letter, shift % 10)
        return encodedWord

    @staticmethod
    def encode(message, shift):
        encodedMessage = ""
        words = message.upper().split()
        for word in words:
            encodedWord = Vigenere.encodeWordVigenere(word, shift)
            encodedMessage += encodedWord + " "
        return encodedMessage.strip().capitalize()

    @staticmethod
    def shiftLetterDecoded(encodedLetter, shift):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        encodedLetter = encodedLetter.upper()
        shiftedIndex = (alphabet.index(encodedLetter) - shift) % 26
        shiftedLetter = alphabet[shiftedIndex]
        return shiftedLetter

    @staticmethod
    def decodeWordVigenere(encodedWord, shift):
        decodedWord = ""
        for i, letter in enumerate(encodedWord):
            if i % 2 == 0:
                decodedWord += Vigenere.shiftLetterDecoded(letter, shift // 10)
            else:
                decodedWord += Vigenere.shiftLetterDecoded(letter, shift % 10)
        return decodedWord

    @staticmethod
    def decode(encodedMessage, shift):
        decodedMessage = ""
        words = encodedMessage.split()
        for word in words:
            decodedWord = Vigenere.decodeWordVigenere(word, shift)
            decodedMessage += decodedWord + " "
        return decodedMessage.strip().capitalize()

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

    @staticmethod
    def letterToNumericValue(letter):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return alphabet.index(letter) + 1

    @staticmethod
    def valueToLetter(value):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return alphabet[value - 1]

    @staticmethod
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
        message = message.upper().strip()
        key = key.upper().strip()
        messageInWords = message.split(" ")
        keyAdapted = KeywordCipher.adaptKeyInMessage(message, key)
        keyInWords = keyAdapted.split(" ")
        encodedMessage = " ".join(KeywordCipher.encodeWordWithKey(word, key_word) for word, key_word in zip(messageInWords, keyInWords))
        return encodedMessage.capitalize()

    @staticmethod
    def decodeWordWithKey(word, key):
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
        message = message.upper().strip()
        key = key.upper().strip()
        messageWords = message.split(" ")
        adaptedKey = KeywordCipher.adaptKeyToMessage(message, key)
        keyWords = adaptedKey.split(" ")
        decodedMessage = ""

        for word, keyWord in zip(messageWords, keyWords):
            decodedWord = KeywordCipher.decodeWordWithKey(word,keyWord)
            decodedMessage += decodedWord + " "
        return decodedMessage.capitalize().strip()

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
        messageList = message.strip().upper().split(" ")
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
    def encodeWordToBinary(word):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        binaryCode = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
                    "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
                    "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000",
                    "11001"]

        binaryWord = ""
        for char in word:
            if char in alphabet:
                charIndex = alphabet.index(char)
                binaryWord += binaryCode[charIndex] + " "

        return binaryWord.strip()
    
    @staticmethod
    def encode(message):
        messageList = message.strip().upper().split(" ")
        binaryMessage = ""
        for word in messageList:
            binaryWord = Binary.encodeWordToBinary(word)
            binaryMessage += binaryWord + " * "

        return binaryMessage[:-2]
    
    @staticmethod
    def decodeWordFromBinary(binaryWord):
        binaryLetters = binaryWord.split(" ")
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        binaryCode = ["00000","00001","00010","00011","00100","00101","00110","00111",
                    "01000","01001","01010","01011","01100","01101","01110","01111",
                    "10000","10001","10010","10011","10100","10101","10110","10111","11000",
                    "11001"]
        decodedWord = []
        
        for letter in binaryLetters:
            if letter in binaryCode:
                index = binaryCode.index(letter)
                decodedWord.append(alphabet[index])
        
        return decodedWord

    @staticmethod
    def decode(binaryMessage):
        binaryMessageList = binaryMessage.split("*")
        decodedMessage = ""
        
        for binaryWord in binaryMessageList:
            decodedWord = Binary.decodeWordFromBinary(binaryWord)
            decodedMessage += " ".join(decodedWord) + " "
        return decodedMessage.strip().capitalize()

class Atbash:
    @staticmethod
    def encodeAndDecode(message):
        message = message.strip().upper()
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
        return encodedOrDecodedMessage.capitalize()
