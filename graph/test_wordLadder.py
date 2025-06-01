from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = [[beginWord, 1]]

        while queue:
            item = queue.pop(0)
            word = item[0]
            length = item[1]

            # check if reach the end
            if word == endWord:
                return length
            
            # mutate a char
            for i in range(len(word)):
                # try every alphabet
                for j in range(26):
                    newWord = word[:i] + chr(j + ord('a')) + word[i + 1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append([newWord, length + 1]) 

        return 0
    
def test1():
    solution = Solution()
    assert solution.ladderLength(
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
    ) == 5

def test2():
    solution = Solution()
    assert solution.ladderLength(
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log"]
    ) == 0
