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

board = sys.argv[1]
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
            return {line.strip() for line in f.readlines()}
    except IOError:
        print "No dictionary at", dictionary_path, ". Please enter path to dictionary at command line."
        sys.exit()

def power_set(permutations, n):
    """
    Returns the set of permutations of length n from the power set of the elements
    """
    results = []

    for perm in permutations:
        results.append(perm[:n])
    return set(results)

def permutation(elements, length):
    """
    Returns all permutations of the given elements
    """

    # return set(itertools.permutations(board, length))

    result = []

    #base case
    if len(elements) <= 1:
        return elements

    #recursive case
    for i, element in enumerate(elements):
        for perm in permutation(elements[:i]+elements[i+1:], length):
            result.append(element + perm)
    return power_set(result, length)

def boggle(board):
    """
    Prints all permutations that are available in the dictionary
    """
    result = []
    words = create_dictionary()
    
    # Iterates through all possible lengths (words of length 3 - length of board)
    for i in xrange(3, len(board)+1):
        permutations = permutation(board, i)
        perm = []
        for p in permutations:  
            perm.append(''.join(elem[0] for elem in p)) # Joins letters into one string
        for item in (perm):
            if item.lower() in words:
                result.append(item.lower())
    return result

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
    permutations = boggle(board)
    board, position = boggle_graph.make_board(board, n)
    graph = boggle_graph.make_graph(board, position)
    for word in permutations:
        visited = {}
        if dfs(graph, ' '+word):
            print word







