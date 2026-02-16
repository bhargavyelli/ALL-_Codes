import numpy as np
import pyautogui as py
import time
from numpy.linalg import inv, det 
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# # reversedd_arr = arr[::-1]
# # np.shape
# arr = arr.reshape(3,3)

# # for i in range(arr):
# #     for j in range(len(i)):
# #         if j%2 == 1:
# #             arr[i][j] = -1

# # print(arr[arr != 0])
# # print(arr)

# print(np.argmax(arr))

# t = time.time()
# # print(t%3600)
# x = 1450
# y = 500
# while(time.time()-t < 60):
#     py.click(x, y, duration=5)
#     y = y+20
#     # //py.moveTo(x, y, duration=2)

    




# arr = np.ones((5,5))
# arr[2:-1,1:-1] = 0

# print(arr)


# arr = np.array([1,2])
# arr2 = np.array([3,4])
# arr = np.vstack((arr,arr2))
# print(arr)
# # print(np.linalg.inv(arr))
# print(np.linalg.det(arr))



from collections import Counter, defaultdict

def get_stats(vocab):
    """Count frequency of symbol pairs in the vocabulary."""
    pairs = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    """Merge all occurrences of the most frequent pair."""
    bigram = ' '.join(pair)
    new_vocab = {}
    for word in vocab:
        # Replace occurrences of the pair with merged token
        new_word = word.replace(bigram, ''.join(pair))
        new_vocab[new_word] = vocab[word]
    return new_vocab

def build_bpe_vocab(corpus, num_merges):
    """
    corpus: list of words (strings)
    num_merges: number of merge operations to perform
    """
    # Initialize vocabulary: each word is split into chars + end-of-word token
    vocab = {}
    for word in corpus:
        # Append end of word symbol '</w>'
        chars = ' '.join(list(word)) + ' </w>'
        vocab[chars] = vocab.get(chars, 0) + 1

    merges = []
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        # Find most frequent pair
        best = max(pairs, key=pairs.get)
        merges.append(best)
        vocab = merge_vocab(best, vocab)

    return vocab, merges

def tokenize(word, merges):
    """Tokenize a new word using learned merges."""
    symbols = list(word) + ['</w>']
    while True:
        pairs = [(symbols[i], symbols[i+1]) for i in range(len(symbols)-1)]
        merge_candidates = [pair for pair in pairs if pair in merges]
        if not merge_candidates:
            break
        # Merge the first candidate pair found (greedy)
        first_pair = merge_candidates[0]
        new_symbols = []
        i = 0
        while i < len(symbols):
            if i < len(symbols) -1 and symbols[i] == first_pair[0] and symbols[i+1] == first_pair[1]:
                new_symbols.append(''.join(first_pair))
                i += 2
            else:
                new_symbols.append(symbols[i])
                i += 1
        symbols = new_symbols
    return symbols

# Example usage:
corpus = ["hi","my","name","name","is","is","bhargav"]
num_merges = 10


vocab, merges = build_bpe_vocab(corpus, num_merges)
print("Learned merges:")
print(merges)

word = "lowest"
tokens = tokenize(word, merges)
print(f"Tokenization of '{word}': {tokens}")







