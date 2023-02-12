
numbers = [30,3,34,5,9]
answer = ""
str_number = list(map(str,numbers))
sorted_number = sorted(str_number,key=lambda x: x*3,reverse=True)
for number in sorted_number:
    answer += number
print( str(int(answer)))


#강의 듣고 풀었을 떄
def solution(numbers):
    numbers = [str(x) for x in number]                         #문자열로 바꾸어서, 리스트화한다.
    numbers.sort((key=lambda x : (x*4)[:4]), reverse = True)
    if numbers[0] == '0' : 
        answer = '0'
    else: 
        answer
    answer = ''.join(numbers) # 이어붙이기
     
    return answer