#출처 : https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Example 1:
    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3.

# Example 2:
    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V= 5, III = 3.

# s가 문자열로 MCMXCIV 이렇게 주어진다면,

s = 'MCMXCIV'
s = list(s)
reselt = 0
i = 0

for i in range(len(s)):
    if(s[i] == 'I'):
        reselt += 1
        i += 1
        continue
    if(s[i] == 'V'):
        reselt += 5
        i += 1
        continue
    if(s[i] == 'X'):
        reselt += 10
        i += 1
        continue
    if(s[i] == 'L'):
        reselt += 50
        i += 1
        continue
    if(s[i] == 'C'):
        reselt += 100
        i += 1
        continue
    if(s[i] == 'D'):
        reselt+=500
        i += 1
        continue
    if(s[i] == 'M'):
        reselt+=1000
        i += 1
        continue
        
print(f'결과값은 {reselt} 입니다')
print(f's 값은 {s} 입니다')

# 처음에 continue를 생각 못 하고, 계속 결과값이 잘못 나왔었다.


# 다른 사람이 한거 참조!
class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        answer = 0
        
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                answer -= roman[s[i]]
            else:
                answer += roman[s[i]]

        return answer + roman[s[-1]]