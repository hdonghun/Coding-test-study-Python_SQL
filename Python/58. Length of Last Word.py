# 출처: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = ''
        k = s.split()
        return len(k[-1])


# 다른 사람이 푼 방법 확인
# https://www.youtube.com/watch?v=KT9rltZTybQ

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i>= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
