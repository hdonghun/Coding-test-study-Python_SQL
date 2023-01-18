# 출처 : https://leetcode.com/problems/longest-common-prefix/
# 14. Longest Common Prefix

str = ["flower","flow","flight"]
char = ""
# 길이가 : 3
# [0][i] == [j][i] 
# [0][0] == [1][0]  > f
# [0][0] == [2][0]  > f
# [0][0] == [3][0]
# [0][1] == [1][1]  > l
# [0][1] == [2][1]  > l
# [0][1] == [3][1]
# [0][2] == [1][2]  > o
# [0][2] == [2][2]  
# [0][2] == [3][2]
# [0][3] == [1][3]
# [0][3] == [2][3]
# [0][3] == [3][3]


for i in range(len(str)):
    for j in range(0,len(str)-1):
        if(str[0][i]==str[j+1][i]):  
                char+=str[0][i]  
for k in range(len(char)):
    if(char[k:]!=char[k+1:]):
        char.replace(char[k],"")
    else:
        continue;

print(char)
result = ''.join(dict.fromkeys(char))  #중복제거, 순서상관(o)
print(result)
# 완성 못함..ㅠㅠ 처음 생각을 완전히 잘못하였다. 



# 다른 사람이 한 것!
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs, key=len) # 길이를 기준으로 최소 길이를 갖는 문자열을 찾는다.
        
        for i, ch in enumerate(shortest): # 최소 길이 문자열의 문자를 하나씩 iteration
            for other in strs: # 리스트의 다른 문자열과 비교
                if other[i] != ch: # 동일한 위치에 있는 문자와 비교해서 다르다면
                    return shortest[:i] # 다르기 전까지의 문자만 return
        return shortest

# enumerate 사용하는법을 배웠다.

