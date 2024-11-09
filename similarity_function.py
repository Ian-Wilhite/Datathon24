from gensim.models import KeyedVectors

print("loading model")
# Load the Google News Word2Vec model
model_path = 'googlenews_model/archive/GoogleNews-vectors-negative300.bin'
#model = Word2Vec.load(path/to/your/model)
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("model loaded")

similarity = word2vec_model.similarity(word1, word2)
