from util import Queue
import string

# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# 2: Build The Graph
f = open('words.txt', 'r')
word_set = frozenset(f.read().lower().split("\n"))
f.close()


def get_neighbors(word):
    """
    Get all words that are one letter
    away from the given word
    """
    # Get same length words first
    # Swap each letter with a letter in the alphabet
    # If resulting word is in the word_set, add to the results
    results = []

    list_word = list(word)
    for i in range(len(list_word)):
        for letter in list(string.ascii_lowercase):
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    return results


# def words_are_neighbors(w1, w2):
#     """
#     return True if words are one letter apart
#     False otherwise
#     """
#     list_word = list(w1)
#     for i in range(len(list_word)):
#         for letter in list(string.ascii_lowercase):
#             temp_word = list_word.copy()
#             temp_word[i] = letter
#             if "".join(temp_word) == w2:
#                 return True
#     return False


# neighbors = {}
#
# for word in word_set:
#     neighbors[word] = set()
#     for potential_neighbor in word_set:
#         if words_are_neighbors(word, potential_neighbor):
#             neighbors[word].add(potential_neighbor)


# def get_neighbors(word):
#     return neighbors[word]

# def words_are_neighbors(w1, w2):
#     if len(w1) != len(w2):
#         return False
#     for i in range(len(w1)):
#         if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
#             return True
#     return False


# 3: Traverse teh graph (BFS)
def word_ladder(begin_word, end_word):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    q = Queue()
    q.enqueue([begin_word])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            visited.add(w)
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(word_ladder('tag', 'dap'))
