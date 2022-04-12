# Brandon Wong
# CPSC 3400
# HW1 Python Assignment: Finding Word Ladders
# This program finds the shortest word ladder between pairs of words

from collections import deque
from copy import copy

words_file = 'words.txt'
pairs_file = 'pairs.txt'
max_word_length = 7


def main():
    # Input files
    wordsFile = open(words_file, 'r')
    pairsFile = open(pairs_file, 'r')

    wordList = set()
    adjWords = dict()

    # Add words under max word length to the set of words
    for line in wordsFile:
        line = line.rstrip()
        if len(line) <= max_word_length:
            wordList.add(line)
    wordsFile.close()

    for line in pairsFile:
        line = line.rstrip().split()
        startWord = line[0]
        endWord = line[1]
        print('** Looking for ladder from ' + startWord + ' to ' + endWord)
        # Stop if start word and end word are diff lengths
        if len(startWord) != len(endWord):
            print(startWord + ' and ' + endWord + ' are not the same length\n')
        else:
            q = deque()
            q.append([startWord])
            ans = []
            visited = set()
            # Continue the DFS until word ladder is found or queue becomes empty (no word ladder found)
            while q:
                # Get first ladder in the queue
                curr = q.popleft()
                for i in range(len(curr)):
                    # Add the last word in the ladder to set of visited words
                    word = curr[-1]
                    visited.add(word)
                    if word == endWord:
                        ans = curr
                        break
                    # If current word is not already in the adjacency list, find all the adjacent words for that word
                    elif word not in adjWords:
                        adjList = list()
                        for j in range(len(word)):
                            for c in range(ord('a'), ord('z') + 1):
                                new_word = word[:j] + chr(c) + word[j + 1:]
                                if new_word in wordList:
                                    adjList.append(new_word)
                        # Add the list of adjacent words to the dictionary
                        adjWords[word] = adjList
                    # From the dictionary, make new ladders using unvisited adjacent words
                    # and append to the end of the queue
                    for possibleWord in adjWords[word]:
                        if possibleWord not in visited:
                            new_ladder = copy(curr)
                            new_ladder.append(possibleWord)
                            visited.add(possibleWord)
                            if possibleWord == endWord:
                                ans = new_ladder
                                break
                            q.append(new_ladder)
            if ans:
                res = " -> ".join(ans)
                print('The ladder is: ' + res + '\n')
            else:
                print('No ladder found from ' + startWord + ' and ' + endWord + '\n')
    pairsFile.close()


if __name__ == "__main__":
    main()