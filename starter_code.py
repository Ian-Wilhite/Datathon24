def model(words, strikes, isOneAway, correctGroups, previousGuesses, error):
	"""
	_______________________________________________________
	Parameters:
	words - 1D Array with 16 shuffled words
	strikes - Integer with number of strikes
	isOneAway - Boolean if your previous guess is one word away from the correct answer
	correctGroups - 2D Array with groups previously guessed correctly
	previousGuesses - 2D Array with previous guesses
	error - String with error message (0 if no error)

	Returns:
	guess - 1D Array with 4 words
	endTurn - Boolean if you want to end the puzzle
	_______________________________________________________
	"""

	# Your Code here
	# Good Luck!
	playerLives = 4
	groups = []
	bestGroup = []
	highestScore = 0
	
	for i in range(len(words)):
		for j in range(i + 1, len(words)):
					for k in range(j + 1, len(words)):
						for l in range(k + 1, len(words)):
							group = [words[i], words[j], words[k], words[l]]
							score = (similarity(words[i], words[j]) + similarity(words[i], words[k]) + 
									similarity(words[i], words[l]) + similarity(words[j], words[k]) + 
									similarity(words[j], words[l]) + similarity(words[k], words[l])) / 6
							if score > highestScore:
								nextGuess = group
								highestScore = score
	# Example code where guess is hard-coded
	guess = ["apples", "bananas", "oranges", "grapes"] # 1D Array with 4 elements containing guess
	endTurn = False # True if you want to end puzzle and skip to the next one

	return guess, endTurn
