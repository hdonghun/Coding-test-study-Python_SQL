# 출처: https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]  #[2:] 을 통해서 2번쨰 인덱스부터 나오게 하여, 0b를 제외시키기.


# 다른 사람이 한것.
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        return format(int(a,2) + int(b,2), 'b')   # 여기서'b'는 이진수를 표현하는것. 접두어 0b를 뺴고 나타낼수있다.





