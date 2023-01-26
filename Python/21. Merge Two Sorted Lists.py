# 출처 : https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

# 감이 안와서 아래 링크 영상강의 참조함.
# https://www.youtube.com/watch?v=XIdigk956u0 

#Node : 데이터와 다음 데이터를 가리키는 주소(포인터)로 이루어져 있다.
#Head : 링크드리스트에서 가장 시작점인 데이터를 의미한다.
#Tail : 링크드리스트에서 가장 마지막 데이터를 의미

#장점: 링크드리스트 수정시 시간복잡도 O(1)을 갖는다. 항상 일정한 속도
#단점: 위 구조에서 보듯이 다음 데이터를 연결하기 위해선 별도의 주소 공간을 가져야 한다. 저장공간 효율이 높지 않음
#      배열은 인덱스를 통해 데이터에 접근하므로 시간복잡도 O(1)을 갖지만 링크드리스트의 경우 O(n)을 갖는다