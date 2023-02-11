# 문제 설명
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
# 입출력 예
# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
# 입출력 예 설명
# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.



# solution
n = 10
lost = [1,5,3,7,8] 
reserve = [2,6,5,7,9]
lost.sort()
reserve.sort()
answer = (n - len(lost))
print("초기 answer의 값: ", answer)


for k in range(len(lost)):  
    for j in range(len(reserve)):
        if(reserve[j] == lost[k]):   # 옷을 원래 빌려줄수 있는 학생이, 옷을 도난 당했을때의 경우
            answer += 1
            reserve[j] = reserve[j] * 0
            break
        elif((lost[k]>reserve[j]) and ((lost[k]-1) == reserve[j])):
            answer += 1
            reserve[j] = reserve[j] * 0
            break
        elif((lost[k] < reserve[j]) and ((lost[k]+1) == reserve[j])):
            answer += 1
            reserve[j] = reserve[j] * 0
            break

print("answer의 최종 값: ", answer)
# example 1,2,3 에 맞게 해봤는데, 통과해서 기분 좋아서 채점 했는데.....
# 채점 결과
# 정확성: 50.0
# 효율성: 0.0
# 합계: 50.0 / 100.0
# 결론은 50점짜리 답안이였던것.....ㅠㅠ

# 문제 다시 읽고, 정렬 코드 추가 해주고 다시 채점 결과
# lost.sort()
# reserve.sort()
# 채점 결과
# 정확성: 83.3
# 효율성: 0.0
# 합계: 83.3 / 100.0
# 83.3점까지 올라오긴 했는데....100점은 아니다... ㅠㅠ




#강의 듣고 풀었을 떄
def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1, n+1):
        if u[i-1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i + 2] = [1,1]
    return len([x for x in u[1:-1] if x> 0])
# 강사님은 엄청 쉬운 알고리즘이라고하는데, 나는 바보인가


# 또 다른 풀이
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
# 학생의 수가 엄청 많아 질 때는,
# 시간복잡도에 효용에 따라 #또 다른 풀이가 더 적합하다.