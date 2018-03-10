"""Name: Solution
   Lab Section: Kenny's Labs
   Title: Hangman
   Due Date: Sunday, March 4"""

def getLetter():
	#This function prompts the user for a single, lower case letter
	validInput = False
	guessedLetters = []
	while not validInput:
	#This while loop runs until letter is returned since validInput
	#is never false
		print("*" * 50)
		letter = input("\nplease enter a lower case letter: ")

		if letter.isalpha():
		#checks to see if the string is consists of only letters
			if len(letter) == 1:
			#checks to see if input consists of only one character
				if letter.islower():
				#checks to see if the string is a lower case letter
					return letter
		print("That's not a valid letter \n")

def containsLetter(secretWord, character):
	#This function checks to see if the word contains the character that is guessed
	for letter in secretWord:
		if letter == character:
			return True
			#if we reach a return statement we automatically exit the function

	#so we can only reach the false statement if we run through each
	#letter in the secret word and none of the letters match the character
	return False

def replaceVisibleWord(word, visibleWord, letter):
	#This goes through each charcter in the word
	#if the character is the same as the charcater that is guessed,
	#we change the spot of that character in visbileWord list to the character
	for i in range(len(word)):
		if word[i] == letter:
			visibleWord[i] = letter
	return visibleWord

def printStatus(visibleWord, whammiesLeft):
	#This function prints current word and whammies left
	print("Current guess:")
	print("".join(visibleWord))
	print()
	print("You have %d guesses remaining" % (whammiesLeft))
	print()

def repeatGuess(guessedAlready, letter):
	for guess in guessedAlready:
		if letter == guess:
			return True
	return False

def main():
	secretWord = "saucy"
	visibleWord = []
	whammiesLeft = 6
	guessedAlready = []
	win = False

	#This for loop creates visible word
	#Visible word to start wtih is all -'s
	for letter in secretWord:
		visibleWord.append("-")
	
	while whammiesLeft > 0:
		repeated = True
		while repeated:
			letter = getLetter()
			repeated = repeatGuess(guessedAlready, letter)
		guessedAlready.append(letter)
		if containsLetter(secretWord, letter):
			#replaceVisibleWord takes in a visibleWord and returns a new visibleWord
			#that's why we set visibleWord equal to replaceVisibleWord(...)
			print("Yippee that's right")
			visibleWord = replaceVisibleWord(secretWord, visibleWord, letter)
		else:
			print("That is incorrect")
			whammiesLeft = whammiesLeft - 1
		if secretWord == "".join(visibleWord):
			win = True
			break
		printStatus(visibleWord, whammiesLeft)
	if not win:
		print("Sorry you lose")
		print("The correct word was %s" % (secretWord))
	else:
		print("Congratulations")
		print("You were able to solve the word with %d whammies left" % (whammiesLeft))
		print("The word was %s" % (secretWord))





	
main()

