from gensim.models import KeyedVectors
import openai
openai.api_key = 'your-api-key'

print("loading model")
# Load the Google News Word2Vec model
model_path = 'archive/GoogleNews-vectors-negative300.bin'
#model = Word2Vec.load(path/to/your/model)
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("model loaded")


def get_similarity(word1, word2):
    response = openai.Embedding.create(
        input=[word1, word2],
        model="text-embedding-ada-002"
    )
    embedding1 = response['data'][0]['embedding']
    embedding2 = response['data'][1]['embedding']
    
    similarity = sum(a*b for a, b in zip(embedding1, embedding2)) / (sum(a**2 for a in embedding1)**0.5 * sum(b**2 for b in embedding2)**0.5)
    return similarity

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
	groups = []
	bestGroup = []
	highestScore = 0
	
	for i in range(len(words)):
		for j in range(i + 1, len(words)):
			for k in range(j + 1, len(words)):
				for l in range(k + 1, len(words)):
					if(words[i] in correctGroups or words[j] in correctGroups or words[k] in correctGroups or words[l] in correctGroups):
						continue
					group = [words[i], words[j], words[k], words[l]]
					score = 0
					for m in range(4):
						for n in range(m + 1, 4):
							score += get_similarity(group[m], group[n])
					score /= 6
					if score > highestScore and group not in previousGuesses:
						nextGuess = group
						highestScore = score

	
	# guess = ["apples", "bananas", "oranges", "grapes"] # 1D Array with 4 elements containing guess
	endTurn = False # True if you want to end puzzle and skip to the next one
	return nextGuess, endTurn
