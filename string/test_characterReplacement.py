import pytest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = dict()
        max_freq_char = 0
        max_len = 0

        for right in range(len(s)):
            if(freq.get(s[right])):
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1

            max_freq_char = max(max_freq_char, freq[s[right]])
            
            print(freq)
            print(f'max_freq_char: {max_freq_char}')

            while (right - left + 1 - max_freq_char > k):
                print(right)
                print(left)
                # shrink left
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        print(freq)
        print(right)
        print(left)

        return max_len


def test1():
    solution = Solution()
    Input = "ABAB"
    k = 2
    Output = 4
    assert solution.characterReplacement(Input, k) == Output

def test2():
    solution = Solution()
    Input = "AABABBA"
    k = 1
    Output = 4
    assert solution.characterReplacement(Input, k) == Output

def test3():
    solution = Solution()
    Input = "ABAB"
    k = 0
    Output = 1
    assert solution.characterReplacement(Input, k) == Output

def test4():
    solution = Solution()
    Input = "AAB"
    k = 0
    Output = 2
    assert solution.characterReplacement(Input, k) == Output
       