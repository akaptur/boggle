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

def create_dictionary(dictionary=dictionary_path):
    """
    Imports words from a local dictionary into a python set
    """
    try:
        with open(dictionary, 'r') as f:
            return [line.strip().lower() for line in f.readlines()]
    except IOError:
        print "No dictionary at", dictionary_path, ". Please enter path to dictionary at command line."
        sys.exit()


def dfs(visited_nodes, graph, node=('',(None,None))):
    """
    Performs depth-first-search on the graph, returns True if the word is present
    """
    global dictionary_set
    visited_nodes = visited_nodes + [node]

    word_fragment = "".join([letter for letter, position in visited_nodes]) 
    # print word_fragment
    # pdb.set_trace()

    if len(word_fragment) >= 3 and word_fragment in dictionary_set:
        yield word_fragment

    good_neighbors = [n for n in graph[node] if n not in visited_nodes]
    # print "good_neighbors", good_neighbors
    for neighbor in good_neighbors:
        for result in dfs(visited_nodes, graph, neighbor):
            yield result

# def is_in(word, dictionary):
#     # print dictionary
#     if not dictionary:
#         return False
#     if len(dictionary) == 1:
#         if dictionary[0].startswith(word):
#             return True
#         else:
#             return False
#     length = len(dictionary)
#     middle_element = dictionary[length/2]
#     if middle_element > word:
#         if middle_element.startswith(word):
#             return True
#         else:
#             return is_in(word, dictionary[:length/2])
#     else:
#         return is_in(word, dictionary[length/2:])

# def test_is_in():
#     sys.setrecursionlimit(10)
#     word = 'ch'
#     dictionary = ['apples', 'chad', 'dog', 'lemur', 'paper', 'pragmatic', 'what']
#     print is_in(word, dictionary)


if __name__ == "__main__":
    dictionary_list = create_dictionary()
    # test_is_in()
    # pdb.set_trace()
    dictionary_set = set(dictionary_list)
    print "dictionary created"
    board, position = boggle_graph.make_board(letters, n)
    graph = boggle_graph.make_graph(board, position)
    words_out = []
    for word in dfs([], graph):
        print word
        words_out.append(word)
    answers = set(words_out)
    print len(answers)
    # time for CATSJAOREKONVUES 4 = 1m22.705s







