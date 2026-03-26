import pytest

class Solution:
    def queueQuestion(self, moves: [str], target: int) -> int:
        queue = []
        target_index = -1

        for i, move in enumerate(moves):
            temp = move.split(" ")
            if temp[0] == "ENQUEUE":
                queue.append(int(temp[1]))

                if int(temp[1]) == target:
                    target_index = i

            elif temp[0] == "DEQUEUE":
                queue.pop(0)
                target_index = target_index - 1

        count = 0
        for item in range(target_index):
            count = count + 1

        return count

    def decipher(self, ciphered: str, knownWord: str) -> str:
        possibleWords = []

        for s in ciphered.split(" "):
            if len(s) == len(knownWord):
                possibleWords.append(s)

        if len(possibleWords) == 0:
            return "Invalid"

        for word in possibleWords:
            tempChars = []
            swift = (ord(word[0]) - ord(knownWord[0])) % 26
            for c in word:
                tempChars.append(chr(ord(c) - swift))

            tempWord = "".join(tempChars)
            if tempWord == knownWord:
                break

        result = []
        for c in ciphered:
            if (c < 'z' and c > 'a') or (c < 'Z' and c > 'A'):
                result.append(chr(ord(c) - swift))
            else:
                result.append(c)

        return "".join(result)


def test1():
    solution = Solution()
    assert solution.decipher("jgnnq yqtnf! ccccc", "hello") == "hello world! aaaaa"

def test2():
    solution = Solution()
    assert solution.decipher("", "hello") == "Invalid"

def test3():
    solution = Solution()
    assert solution.queueQuestion(["ENQUEUE 19", "ENQUEUE 20", "ENQUEUE 21", "DEQUEUE", "ENQUEUE 22"], 20) == 0

def test4():
    solution = Solution()
    assert solution.queueQuestion(["ENQUEUE 19", "ENQUEUE 21", "ENQUEUE 20", "ENQUEUE 22"], 20) == 2
    