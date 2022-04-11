# word-ladder
Assignment for CPSC-3400 Languages and Computation at Seattle University.  
Practicing usage of Python data structures and dynamic programming.

Word Ladder is a Python program that finds the shortest word ladder between pairs of words.
> "A word ladder puzzle begins with two words, and to solve the puzzle one must find a chain of other words to link the two, in which two adjacent words differ by one letter." from https://en.wikipedia.org/wiki/Word_ladder

**main.py** uses input files: **words.txt** and **pairs.txt**
* **words.txt** is a collection of words that **main.py** will work with to construct word ladders
* **pairs.txt** is the collection of pairs of words that **main.py** will try to find word ladders between

Input file format:
* **words.txt**: each word should be on its own line
* **pairs.txt**: each word pair should be on its own line seperated by a space

Example output when a word ladder is found:
```
** Looking for ladder from cat to hot
The ladder is: cat -> bat -> bot -> hot
```
Example output when a word ladder is not found:
```
** Looking for ladder from abed to expo
No ladder found from abed and expo
```
Example output when a pair is of different lengths:
```
** Looking for ladder from aces to clown
aces and clown are not the same length
```
