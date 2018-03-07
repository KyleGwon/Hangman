import time
def emptyLine():
    return("  ")
def guess(i, guess):
        if i == guess:
            return True
        else:
            return False
def printWord(word, lettersGotten):
    orderedList = []
    for num in range(len(word)):
        i = word[num]
        orderedList.append("_")
        for l in lettersGotten:
            if i == l:
                del orderedList[num]
                orderedList.append(i)

    print(orderedList)
def removeLetter(letter, validGuesses):
    itemsToDelete = []
    for i in range(len(validGuesses)):
        if letter == validGuesses[i]:
            itemsToDelete.append(i)
    for i in itemsToDelete:
        # i should be 15
        del validGuesses[i]
    #should print a list of a - z without t in it
    return validGuesses
def main():
    word = "turtle"
    lettersGuessed = []
    correctGuesses = []
    wrongGuessesLeft = 5
    wrongGuesses = 0
    validGuesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # print("Welcome to hangman!")
    # 
    while wrongGuessesLeft > 0:
        # emptyLine()
        # print("You have " + str(wrongGuessesLeft) + " wrong answers left.")
        # 
        # emptyLine()
        # print("There are " + str(len(word)) + " letters in the word.")
        # 
        printWord(word, correctGuesses)
        # print("What is your guess?")
        # emptyLine()
        playerGuess = input("> ")
        for i in validGuesses:
            if i == playerGuess:
                validGuesses = removeLetter(i, validGuesses)
                for i in list(word):
                    var = guess(i, playerGuess)
                    if var == True:
                        correctGuesses.append(i)
                    #Need help on "if var == false:""


main()
