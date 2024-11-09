from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

print("loading model")
# Load the Google News Word2Vec model
model_path = 'googlenews_model/archive/GoogleNews-vectors-negative300.bin'
#model = Word2Vec.load(path/to/your/model)
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("model loaded")

# Check similarity between words
word1 = 'king'
word2 = 'queen'
similarity = word2vec_model.similarity(word1, word2)
print(f"Similarity between '{word1}' and '{word2}': {similarity}")


# Find most similar words
word = 'king'
most_similar = word2vec_model.most_similar(word, topn=15)
print(f"Words most similar to '{word}':")
for similar_word, score in most_similar:
    print(f"{similar_word}: {score}")

# Word vector arithmetic
result = word2vec_model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print("Result for 'king' - 'man' + 'woman':", result)



