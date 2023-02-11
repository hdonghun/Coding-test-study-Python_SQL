# #문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# #제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.

# #입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

# #입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.



#participant = ["leo", "kiki", "eden"]
participant =  ["mislav", "stanko", "mislav", "ana"]
#completion = ["eden", "kiki"]
completion =  ["stanko", "ana", "mislav"]
temp_list = []
temp_list2 = []
answer = ''

for i in participant:
    if(i not in completion):
        answer += i                                              # 중복되지 않는 값만 넣기
    if(x for x in participant if participant.count(x) > 1):
        temp_list = [x for x in participant if participant.count(x) > 1]  # 중복되는 값 찾아서 넣기
        for i in range(len(temp_list)):
            for j in range(len(completion)):   
                if(temp_list[i] == completion[j]):
                    temp_list2 += temp_list
        if(len(temp_list2) <= 4):
            temp_list2 = set(temp_list2)
            temp_list2 = str(temp_list2)
            answer += temp_list2
            answer = answer[2:-2]

print(answer)
# 완료 못함.....ㅠㅠ



#강의 듣고 풀었을 떄
## 해쉬hash를 이용!

def solution(participant, completion):
    answer = ''
    d = {}
    for x in participant:
        d[x] = d.get(x,0) + 1   #해쉬 형태! , 각각의 값당 하나씩 더하기
    for x in completion:
        d[x] -= 1               #completion에 있으면, 하나 하나 빼주기! 참가인원과 완주한 사람의 인원이 같으면 0, 완주못한 사람이 한명씩 존재 할 수록 1
    dnf = [k for k,v in d.items() if v > 0 ]
    answer = dnf[0]

return answer
#시간복잡도 O(N)



# 또 다른 풀이
# 정렬을 이용!
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant-1)]
#시간 복잡도 O(NlogN)