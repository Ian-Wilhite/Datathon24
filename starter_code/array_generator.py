from gensim.models import KeyedVectors
import numpy as np
import pandas as pd

def make_array(words):
    
    print("loading model")
    
    # Load the Google News Word2Vec model
    model_path = 'archive/GoogleNews-vectors-negative300.bin'
    #model = Word2Vec.load(path/to/your/model)
    word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    
    print("model loaded")

    words = [word.lower() for word in words]  # Convert words to lowercase
    arr = np.zeros([16, 16])
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            try:
                
                arr[i][j] = word2vec_model.similarity(words[i], words[j])
            except:
                try:
                    arr[i][j] = 0  # Handle missing word gracefully
                except:
                    pass
                    
    df = pd.DataFrame(arr)
    df.to_csv('diagonal.csv', index=False, header=False)
    return arr
    
# test_words = [
#     "apple", "banana", "grape", "orange",         # Fruits
#     "dog", "cat", "rabbit", "hamster",            # Pets
#     "car", "truck", "bicycle", "motorcycle",      # Vehicles
#     "guitar", "piano", "drum", "violin"           # Musical Instruments
# ]

# test_words2 = [
#     "BENT",
#     "GNARLY",
#     "TWISTED",
#     "WARPED",
#     "LICK",
#     "OUNCE",
#     "SHRED",
#     "TRACE",
#     "EXPONENT",
#     "POWER",
#     "RADICAL",
#     "ROOT",
#     "BATH",
#     "POWDER",
#     "REST",
#     "THRONE"
# ]       
                
                
# arr = make_array(test_words)
# #print(arr)
# #print(arr[0])
