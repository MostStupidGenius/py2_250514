# part7_linked_list.py
# 연결 리스트
# 데이터를 담고 있는 노드(Node)라는 것을 만들어
# 해당 노드가 데이터와 다음 노드를 가리키는 변수를 보유한다.
# 이로써 이전의 노드가 다음 노드를 가리키는 방식으로
# 모든 노드를 순차적으로 접근할 수 있다.
# 노드 클래스와 해당 노드를 묶어서 관리하는 Linked_list 클래스
# 두 개로 이루어진다.

class Node():
    def __init__(self, data: int):
        self.data = data
        self.next: Node = None # 다음 노드를 가리킬 포인터를 저장하는 변수
        # 기본적으로 가리킬 노드가 없으므로 None으로 설정한다.

class LinkedList():
    def __init__(self):
        # 여러 노드 중 가장 첫번째 노드를 head라고 부른다.
        self.head: Node = None
    
    def insert(self, data: int):
        # 연결 리스트에 값 추가하기
        new_node = Node(data)
        # self.head가 비어있으면(None) self.head에 new_node 저장
        if self.head is None:
            self.head = new_node
            return True # 작업이 끝났으므로 함수 종료
        
        # 다음 노드가 있는지 검사할 노드를 저장할 변수
        current_node = self.head
        try:
            # 현재 노드의 next가 None인지 검사하여
            while current_node.next is not None:
                # None이 아니라면 next를 current_node에 저장하여 반복
                current_node = current_node.next
            # 반복문이 끝났다는 것은 current_node의 next가 None이라는 의미이므로
            # current_node의 next에 new_node를 저장
            current_node.next = new_node
            # 저장이 완료되면 return True
            return True
        except Exception as e:
            print(e)
            # 에러 발생 시 return False
            return False
    
    # 연결 리스트에 있는 모든 데이터를 문자열로 출력
    def __str__(self):
        result = "Link ["
        # 현재 보고 있는 노드
        current = self.head
        # 현재 보고 있는 노드의 순서값
        i = 0
        while current.next is not None:
            if i != 0: result += ", "
            result += str(current.data)
            current = current.next
            i += 1
        # 다음 노드는 없지만 현재 노드의 데이터를 마지막에 추가해주어야 한다.
        result += ", " + str(current.data) + "]"
        # result += f", {current.data}]"
        return result

if __name__ == "__main__":
    link = LinkedList()
    link.insert(1)
    link.insert(2)
    link.insert(3)
    link.insert(4)
    link.insert(67)
    link.insert(14)
    link.insert(24)
    # print(has_insert)
    print(link)



