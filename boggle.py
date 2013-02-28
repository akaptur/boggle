#! /usr/bin/env python
""""
Implementation of a Boggle cheater

Takes in a string of letters from the command line and 
returns the different different words that can be created
using those letters
"""

import itertools
import argparse
import boggle_graph
import sys

"""
Parses the arguments from the command line and calls the function boggle
"""

letters = sys.argv[1]
n = int(sys.argv[2])
if len(sys.argv) == 4:
    dictionary_path = sys.argv[3]
else:
    dictionary_path = '/usr/share/dict/words'

visited = {}

def create_dictionary(dictionary=dictionary_path):
    """
    Imports words from a local dictionary into a python set
    """
    try:
        with open(dictionary, 'r') as f:
            return {line.strip().lower() for line in f.readlines()}
    except IOError:
        print "No dictionary at", dictionary_path, ". Please enter path to dictionary at command line."
        sys.exit()

def boggle(letters):
    """
    Prints all permutations that are available in the dictionary
    """
    result = []
    words = create_dictionary()
    letters = letters.lower()
    
    # Iterates through all possible lengths (words of length 3 - length of board)
    word_possibilities = []
    for i in xrange(3, len(letters)+1):
        permutations = itertools.permutations(letters, i)
        for p in permutations:  
            word_possibilities.append(''.join(elem[0] for elem in p)) # Joins letters into one string
        # pdb.set_trace()
    word_set = set(word_possibilities) & words # intersection of sets!
    return word_set

def dfs(graph, word, node=' '):
    """
    Performs depth-first-search on the graph, returns True if the word is present
    """
    global visited
    # base case
    if word[0] in node and len(word) <= 1:
        return True
    if word[0] not in node:
        return False
    # recursive step
    visited[(node)] = True 
    for neighbor in graph[node]:
        if not visited.get((neighbor), False):
            if dfs(graph, word[1:], neighbor):
                return True
    visited[(node)] = False
    return False

if __name__ == "__main__":
    permutations = boggle(letters)
    board, position = boggle_graph.make_board(letters, n)
    graph = boggle_graph.make_graph(board, position)
    count = 0
    for word in permutations:
        visited = {}
        if dfs(graph, ' '+word):
            print word
            count += 1
    print count







