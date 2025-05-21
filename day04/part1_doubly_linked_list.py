# part1_doubly_linked_list.py
# 양방향 연결 리스트는 이전의 단방향 연결 리스트의 단점인
# 이전 노드로의 이동이 자유롭지 못하다는 것을 해결하기 위해
# 만들어진 자료구조다.
# 때문에 노드에 다음 노드를 가리킬 주소를 담는 변수(next)뿐만 아니라\
# 이전 노드를 가리킬 주소를 담는 변수(prev)까지 클래스 내부에
# 선언되어 사용된다.
# 이전 노드로의 이동은 자유로워졌지만 추가적인 변수, 메모리 공간을
# 필요로 하게 되는 단점을 가진다.

# 양방향 연결 리스트 구현하기
# 앞뒤 노드를 가리킬 변수를 보유한 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 연결리스트 클래스 정의
class DoublyLinkedList:
    def __init__(self):
        # 연결 리스트의 머리, 즉 시작점을 가리킬 변수 선언
        self.head: Node = None
        # 연결 리스트의 끝, 꼬리를 나타낼 변수 선언
        self.tail: Node = None
    
    # 연결 리스트 가장 끝에 요소 추가
    # self.tail의 next를 newNode로 변경하고
    # newNode의 prev를 self.tail 노드로 설정한다.
    # 서로 연결되고 나면 self.tail 저장공간에 newNode의 주소를
    # 저장한다.
    def append(self, data):
        # 입력받은 데이터를 새로운 변수 newNode에 담는다.
        newNode = Node(data)
        # 만약에 헤드가 없다면
        # self.head의 노드를 새로 만든 newNode로 설정해야 한다.
        if not self.head:
            self.head = newNode # 머리로 새로운 노드 임명
            self.tail = newNode # 꼬리로 새로운 노드 임명
        else: # 헤드가 있다면
            # 새로운 노드의 이전 노드를 self.tail로 설정한다.
            newNode.prev = self.tail
            # 새로운 노드를 tail로 설정하기 위해서
            # self.tail의 다음 노드를 새로운 노드로 설정한다.
            self.tail.next = newNode
            # 이로써 self.tail과 새로운 노드 사이에 연결이 생긴다.
            # self.tail의 값으로 새로 추가된 마지막 노드의 주소를
            # 저장한다.
            self.tail = newNode
    def prepend(self, data):
        # 전달된 값을 노드 형태로 바꾸어서 연결 리스트의 앞쪽에
        # 추가하는 방법이다.
        # 새로운 노드를 생성
        newNode = Node(data)
        if not self.head:
            self.head = newNode # 머리로 새로운 노드 임명
            self.tail = newNode # 꼬리로 새로운 노드 임명
        else: 
            # 새로운 노드의 다음 노드를 기존의 head로 변경
            newNode.next = self.head
            self.head.prev = newNode # 순환에 필요
            # 기존 tail을 새로운 노드의 이전 노드로 변경
            newNode.prev = self.tail
            self.tail.next = newNode # 순환에 필요
            # 새로운 노드를 새로운 head로 변경
            self.head = newNode
    
    # 특정 data를 가진 노드를 연결 리스트 상에서 제거 및 기존 값 반환
    # 발견되지 않았다면 None 반환
    def delete(self, data):
        # 현재 노드를 가리킬 변수를 선언하고 기존 head를 담는다.
        current = self.head
        # 만약 current가 None이 아니라면
        while current is not None:
            # 제거하려는 노드의 이전 노드의 주소를 prevNode에 임시로 담고
            prevNode = current.prev
            # 임시로 담고
            nextNode = current.next
            # 현재 노드의 data를 전달받은 data와 비교
            if current.data == data: # 같다면
                # current의 prev의 next에 current의 next를 담고
                prevNode.next = nextNode
                # current의 next를 currnet의 prev로 담는다.
                nextNode.prev = prevNode
                # 위와 같이 양쪽의 노드가 서로를 가리키게 되면
                # current 노드를 가리킬 변수가 사라지게 된다.
                # -> 자연스럽게 삭제
                # 원하는 노드를 찾아서 지웠으므로 여기서 메서드 종료
                return current # 삭제한 노드를 반환
            else: # 입력한 데이터와 현재 노드의 데이터가 일치하지 않는다면
                current = current.next # 다음 노드 확인하기
        
        # 해당 데이터를 가진 노드를 찾지 못하면 도달하는 곳
        # 데이터를 찾지 못한 경우 None 반환
        return None
    
    def display(self):
        # 연결 리스트의 노드마다 데이터를 추출하여 리스트로 만들어 반환하는 메서드
        # 반환할 빈 리스트를 생성
        result = list() # []

        # 현재 확인하고 있는 노드를 담을 변수 current 선언
        current = self.head # head를 시작점으로 한다.

        # 모든 노드를 방문하기 위한 로직 작성
        # while current is not None:
        while current.next != self.head:
            result.append(current.data)
            current = current.next
        # current.next가 self.head이면
        # current는 tail이다.
        result.append(current.data) # 마지막 노드 추가
        # current가 None이면 지금까지 저장한 data들을 담은
        # 리스트, result를 반환한다.
        return result

if __name__ == "__main__":
    obj = DoublyLinkedList()
    obj.append(1)
    obj.append(2)
    obj.append(3)
    obj.append(4)
    obj.prepend(10)
    obj.delete(3)

    # while문의 조건을 이용하여 모든 노드 순회하며 출력
    # 주의: tail의 next가 head이면 순환 양방향 연결 리스트가 되므로
    # 만약 .next가 .head와 같다면 반복을 멈춰야 한다.
    current = obj.head
    
    # while current is not None: # 순환 연결 리스트가 아닐 때 사용하는 조건
    #     # or current.next != obj.head: # 순환 연결 리스트일 때
    #     # tail의 next가 head이면 반복문 종료하는 조건
    #     # current != obj.tail:
    #     print(current.data) # 데이터 출력
    #     current = current.next # 다음 노드를 current 임시변수에 담기
    print("Done.")

    # display 메서드 사용
    print(obj.display())