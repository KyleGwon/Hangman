import time
import random
def emptyLine():
	print("")
def guess(word, guess):
	listWord = list(word)
	for i in range(len(listWord)):
		if listWord[i] == guess:
			return True
		else:
			tempVar = False
	if tempVar == False:
		return False
def printWord(word, lettersGotten):
	orderedList = []
	for num in range(len(word)):
		i = word[num]
		orderedList.append("-")
		for l in lettersGotten:
			if i == l:
				del orderedList[num]
				orderedList.append(i)
	orderedListStr = "".join(orderedList)
	print(orderedListStr)
def numOfCorrectGuessesList(word, lettersGotten):
	correctGuessesList = []
	for num in range(len(word)):
		i = word[num]
		for l in lettersGotten:
			if i == l:
				correctGuessesList.append(i)
	return correctGuessesList
def removeLetter(letter, validGuesses):
	itemsToDelete = []
	for i in range(len(validGuesses)):
		if letter == validGuesses[i]:
			itemsToDelete.append(i)
	for i in itemsToDelete:
		del validGuesses[i]
	return validGuesses
def main():
	wordInt = random.randint(0, 9)
	if wordInt == 0:
		word = "prankster"
	if wordInt == 1:
		word = "speaker"
	if wordInt == 2:
		word = "mining"
	if wordInt == 3:
		word = "toaster"
	if wordInt == 4:
		word = "lamp"
	if wordInt == 5:
		word = "hallway"
	if wordInt == 6:
		word = "function"
	if wordInt == 7:
		word = "class"
	if wordInt == 8:
		word = "turtle"
	if wordInt == 9:
		word = "easy"
	lettersGuessed = []
	correctGuesses = []
	wrongGuessesLeft = 6
	validGuesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	numOfCorrectGuesses = numOfCorrectGuessesList(word, correctGuesses)
	wentThrough = False
	firstWentThrough = False
	print("Welcome to hangman!")
	while wrongGuessesLeft > 0 and len(numOfCorrectGuesses) < len(word):
		emptyLine()
		print("You have " + str(wrongGuessesLeft) + " wrong answers left.")
		emptyLine()
		print("There are " + str(len(word)) + " letters in the word.")
		emptyLine()
		print("word so far:")
		printWord(word, correctGuesses)
		emptyLine()
		tempVar = True
		print("What is your guess?")
		emptyLine()
		playerGuess = input("> ")
		emptyLine()
		while tempVar:
			firstWentThrough = False
			wentThrough = False
			if firstWentThrough == False:
				for i in validGuesses:
					temp = i
					if i == playerGuess:
						validGuesses = removeLetter(i, validGuesses)
						var = guess(word, playerGuess)
						if var:
							correctGuesses.append(i)
							print("Correct!")
							numOfCorrectGuesses = numOfCorrectGuessesList(word, correctGuesses)
							if len(numOfCorrectGuesses) == len(word):
								print("word so far:")
								printWord(word, correctGuesses)
								if wrongGuessesLeft == 1:
									print("Congrats! You got the word, which was " + word + ", with " + str(wrongGuessesLeft) + " wrong guess to spare!")
									wentThrough = True
									tempVar = False
								else:
									print("Congrats! You got the word, which was " + word + ", with " + str(wrongGuessesLeft) + " wrong guesses to spare! Nice job!")
									wentThrough = True
									tempVar = False
							else:
								wentThrough = True
								tempVar = False
						if not var:
							if wrongGuessesLeft == 1:
								print("Incorrect! The word was " + word + ".")
								wrongGuessesLeft -= 1
								wentThrough = True
								tempVar = False
							else:
								print("Incorrect!")
								wrongGuessesLeft -= 1
								wentThrough = True
								tempVar = False
			if wentThrough == False:
				if temp != playerGuess:
					print("Invalid choice! Please try again!")
					emptyLine()
					playerGuess = input("> ")
			emptyLine()
main()
