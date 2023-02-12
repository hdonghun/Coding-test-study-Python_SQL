# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.
# 입출력 예
# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"



def solution(number, k):
    collected = []

    for i , num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0: #collected[-1] 마지막 원소를 나타냄.
            collected.pop() # 리스트 끝에 있는 원소를 없엔다.
            k -= 1          # k 조정하기
        if k == 0:          # 뺄건 다 빼고, 남아있는 것들을 이어붙이기 위한 작업 실행!
            collected += list(number[i:]) # 남아있는 number를 전체를 리스트로 만들어서 붙이기 , 여기때문에 enumerate로 i를 사용하여, 인덱스 이용
            break            
        collected.append(num) # if문이 없더라도 이어붙여서 작동함. 

    collected   = collected[:-k] if k > 0 else collected         #만약에 불필요한 값들이 있을때, 빼주기
    answer = ''.join(collected) #리스트에 하나하나씩 담겨있기 떄문에, ''.join으로 다 같이 넣어주기
    return answer