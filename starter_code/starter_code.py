from gensim.models import KeyedVectors

print("loading model")
# Load the Google News Word2Vec model
model_path = 'archive/GoogleNews-vectors-negative300.bin'
#model = Word2Vec.load(path/to/your/model)
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("model loaded")


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
					score = (word2vec_model.similarity(words[i], words[j]) + word2vec_model.similarity(words[i], words[k]) + 
							word2vec_model.similarity(words[i], words[l]) + word2vec_model.similarity(words[j], words[k]) + 
							word2vec_model.similarity(words[j], words[l]) + word2vec_model.similarity(words[k], words[l])) / 6
					if score > highestScore:
						nextGuess = group
						highestScore = score
	
	# guess = ["apples", "bananas", "oranges", "grapes"] # 1D Array with 4 elements containing guess
	endTurn = False # True if you want to end puzzle and skip to the next one
	return nextGuess, endTurn
