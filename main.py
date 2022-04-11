# Brandon Wong
# CPSC 3400
# HW1 Python Assignment: Finding Word Ladders

from collections import deque
from copy import copy

words_file = 'words.txt'
pairs_file = 'pairs.txt'
max_word_length = 7


def main():
    wordsFile = open(words_file, 'r')
    pairsFile = open(pairs_file, 'r')

    wordList = set()
    adjWords = dict()

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
        if len(startWord) != len(endWord):
            print(startWord + ' and ' + endWord + ' are not the same length\n')
        else:
            q = deque()
            q.append([startWord])
            ans = []
            visited = set()
            while q:
                curr = q.popleft()
                for i in range(len(curr)):
                    word = curr[-1]
                    visited.add(word)
                    if word == endWord:
                        if len(ans) == 0 or len(curr) < len(ans):
                            ans = curr
                            break
                    elif word not in adjWords:
                        adjList = list()
                        for j in range(len(word)):
                            for c in range(ord('a'), ord('z') + 1):
                                new_word = word[:j] + chr(c) + word[j + 1:]
                                if new_word in wordList:
                                    adjList.append(new_word)
                        adjWords[word] = adjList
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