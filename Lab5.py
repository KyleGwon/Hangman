import time
def emptyLine():
    return("  ")
def guess(i, guess):
        if i == guess:
            return True
        else:
            return False
# def printWord(word, lettersGotten):
#     return none
def main():
    word = "turtle"
    lettersGuessed = []
    correctGuesses = []
    wrongGuessesLeft = 5
    wrongGuesses = 0
    # print("Welcome to hangman!")
    # time.sleep(0.2)
    while wrongGuessesLeft > 0:
        # emptyLine()
        # print("You have " + str(wrongGuessesLeft) + " wrong answers left.")
        # time.sleep(0.2)
        # emptyLine()
        # print("There are " + str(len(word)) + " letters in the word.")
        # time.sleep(0.2)
        # print("What is your guess?")
        # emptyLine()
        validGuesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        playerGuess = input("> ")
        # printWord(word, lettersGuessed)
        for letter in validGuesses:
            if letter == playerGuess:
                validGuesses.remove(letter)
                for i in list(word):
                    var = guess(i, playerGuess)
                    if var == True:
                        correctGuesses.append(i)
        printVar = "".join(map(str, correctGuesses))
        print(printVar)


main()