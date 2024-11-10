from gensim.models import KeyedVectors
from array_generator import make_array
import numpy as np
from subfunctions import *

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

    if error == "You have already guessed this combination.":
        print(f'ERROR: DUPLICATE SUBMISSION')
        return [], True

    # print(f'Inputs:')
    # print(f'words: {words}, type: {type(words)}')
    # print(f'strikes: {strikes}, type: {type(strikes)}')
    # print(f'isOneAway: {isOneAway}, type: {type(isOneAway)}')
    # print(f'correctGroups: {correctGroups}, type: {type(correctGroups)}')
    # print(f'previousGuesses: {previousGuesses}, type: {type(previousGuesses)}')
    # print(f'error: {error}')
    
    if type(words) == str:
        
        # print(f'words: {words}, type: {type(words)}')
        # print(f'words[0]: {words[0]}, type: {type(words[0])}')
        words = words.replace("\n", "")
        words = words[1: -1].split(", ")
        words = [word.strip()[1: -1] for word in words]
        
        # print(f'words: {words}, type: {type(words)}')
        # print(f'words[0]: {words[0]}, type: {type(words[0])}')

    
    wordsleft = words
    
    #print(f'correctGroups: {correctGroups}')
    
    for words in correctGroups:
        for word in words:
            wordsleft.remove(word)
    print(f'wordsleft: {wordsleft}')
        
    
    # print(f'previousguesses: {previousGuesses}')
    # print(f'wordsleft {type(wordsleft)}, wordlist {type(previousGuesses)}')
    # print(f'wordsleft[0] {type(wordsleft[0])}, wordlist[0] {type(previousGuesses[0])}')
    
    # print(f'previousguesses type: {type(previousGuesses)}')
    for wordlist in correctGroups:
        # print(f'wordlist type: {type(wordlist)}')
        # print(f'wordsleft type: {type(wordsleft)}')
        if wordsleft == wordlist[0]:
            index = wordsleft.indexof(wordlist[0])
            wordsleft[0], wordsleft[index] = wordsleft[index], wordsleft[0]
    
    arr = make_array(wordsleft)
    #print(arr)
    
    indecies_to_group = []
    
    # if previous guesses contains something and not isOneAway, you need to change where you start: red herring clause
    if previousGuesses and not isOneAway:
        arr_cpy = arr.copy()
        arr_cpy[np.unravel_index(np.argmax(arr), arr.shape)] = 0
        
        index1, index2 = np.unravel_index(np.argmax(arr_cpy), arr_cpy.shape)
    else:
        index1, index2 = np.unravel_index(np.argmax(arr), arr.shape)
    
    indecies_to_group += [index1]
    indecies_to_group += [index2]
    print(f'indexes: {indecies_to_group}')
    
    row_of_index2 = piecewise_max(arr[indecies_to_group[-1], :], arr[:, indecies_to_group[-1]])
    #print(f'row of inxes2: {row_of_index2}')
    #remove all previously added solutions
    for i in indecies_to_group:
        row_of_index2[i] = 0.0
    #print(f'row of inxes2: {row_of_index2}')
    
    index3_arr = arr_sum_keep_zeroes(row_of_index2, arr[0])
    #print(index3_arr)
    index3 = np.argmax(index3_arr)
    
    indecies_to_group += [index3]
    #print(indecies_to_group)
    
    row_of_index3 = piecewise_max(arr[index3, :], arr[:, index3])
    for i in indecies_to_group:
        row_of_index2[i] = 0
    
    #print("rows")
    #print(f'arr:{arr[0]}')
    #print(f'row_of_index2:{row_of_index2}')
    #print(f'row_of_index3:{row_of_index3}')
    
    
    index4arr = arr_sum_keep_zeroes(row_of_index3, row_of_index2, arr[0])
    
    if isOneAway: #remove max to grab next best result
        index4arr = np.array(index4arr)
        index4arr[index4arr == index4arr.max()] = 0 
    
    index4 = np.argmax(index4arr)
    indecies_to_group += [index4]
    #print(f'indecies_to_group:{indecies_to_group}')
    
    
    end_turn = False
    group = [wordsleft[i] for i in indecies_to_group]
    
    if group in previousGuesses:
        end_turn = True
    
    print(F'group: {group}')
    return group, end_turn


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

# test_words3 = ['THRONE', 'EXPONENT', 'BATH', 'POWER', 'WARPED', 'BENT', 'TWISTED',
#  'RADICAL', 'POWDER', 'TRACE', 'REST', 'OUNCE', 'GNARLY', 'LICK', 'ROOT',
#  'SHRED']

# batch_1, _ = model(test_words3, 0, 0, [], [], 0)
# print(batch_1)
# batch_2, _ = model(test_words2, 0, 0, [batch_1], [], 0)
# print(batch_2)
# batch_3, _ = model(test_words2, 0, 0, [batch_1, batch_2], [], 0)
# print(batch_3)
# batch_4, _ = model(test_words2, 0, 0, [batch_1, batch_2, batch_3], [], 0)
# print(batch_4)

# print(f'SOLUTION:')
# print(batch_1)
# print(batch_2)
# print(batch_3)
# print(batch_4)

