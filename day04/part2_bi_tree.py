# part2_bi_tree.py
# 이진 트리(Binary Tree)
# 노드가 단방향으로 두 개의 또다른 노드를 가리키는 
# 피라미드 구조로 만들어진 것을 이진 트리라고 부른다.
# 1. 완전 이진 트리
# : 마지막 레벨을 제외한 나머지 레벨이 모두 채워진 이진트리를 가리키는 말
# 2. 포화 이진 트리
# : 완전 이진 트리에서 마지막 레벨까지 모두 채워진 이진트리를 가리킨다.
# 3. 균형 이진 트리
# : 좌우의 가지, 서브트리의 깊이가 1보다 크지 않은 이진트리를 가리킨다.
# 마지막 레벨의 깊이와 가장 깊지 않은 리프 노드(자식이 없는 노드)의 깊이가
# 1보다 크지 않은 것을 가리킨다.

# 파이썬으로 이진트리 구현하기
# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진트리 클래스 정의
class BinaryTree:
    def __init__(self):
        # 루트 노드, 시작 노드를 담을 변수
        self.root = None
    
    # 데이터를 전달받아서 새로운 노드를 이진 트리에 편입시킨다.
    def insert(self, data):
        # self.root가 없으면 새로운 데이터를 Node로 바꾸어
        # self.root에 담은 뒤 메서드 종료
        if self.root is None:
            self.root = Node(data)
            return # 함수 종료
        
        # queue 자료구조를 이용하여 노드를 순회해주어야 한다.
        # 대기열을 저장할 빈 리스트를 생성
        queue = []

        # 루트 노드를 가장 먼저 넣어놓고 이진트리를 탐색해야 하므로
        # 대기열에 루트노드를 추가한다.
        queue.append(self.root)

        # 새로운 노드를 생성한다.
        newNode = Node(data)

        while queue: # 대기열에 노드가 하나라도 남아있으면 반복
            # 대기열의 0번째 노드(첫번째 노드)를 임시변수로 추출한다.
            node = queue.pop(0)
            if not node.left: # 추출한 노드의 왼쪽 자식 노드가 없다면
                node.left = newNode
                # 새로 만든 노드를, 임시변수로 뽑아낸 노드의 left로 저장
                return # 삽입 완료 되었으므로 반복의 필요성이 사라졌다.
            if not node.right:
                node.right = newNode
                return
            # 여기까지 내려왔다면 node 변수에 담긴 노드는
            # 왼쪽, 오른쪽 자식 노드가 모두 존재하는 것이다.
            # 그렇기 때문에 새로운 노드가 들어갈 자리가 없다.
            # -> 자식 노드들을 압축해제하여 그 자식 노드들을
            # 대기열에 넣어야 한다. -> 전부 탐색
            queue.append(node.left)
            queue.append(node.right)

    def display(self):
        # 이진 트리의 모든 데이터를 순회하며 리스트로 만들어낸다.
        # 이때 레벨 순서대로 진행되며, 왼쪽부터 오른쪽으로 진행된다.
        result = [] # 데이터들을 담아서 반환할 변수 선언
        queue = [] # 빈 리스트 생성
        
        # 검색할 노드가 하나도 없다면(루트가 없다면)
        # 함수 종료
        if not self.root: return None
        
        # self.root가 존재하면 queue에 루트 노드 추가
        queue.append(self.root)

        # 루트 노드를 대기열에 추가시키고 반복적으로 하위 노드(자식 노드)에 접근하여
        # 순서대로 data를 추출, result에 추가한다.
        while queue: # queue에 노드가 하나라도 있다면
            # 현재 확인하고 있는 노드를 담을 임시 변수
            node = queue.pop(0) # 대기열의 첫번째 노드를 추출
            if node is None: break # 추출한 노드가 None이라면 while문 탈출

            # 해당 노드가 None이 아니므로 data가 존재할 것이다.-> 추출
            data = node.data
            result.append(data)
            # 현재 노드에 자식 노드가 있다면 대기열에 추가
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        # 여기까지 왔다는 것은 대기열의 모든 노드를 살펴본 것이다.
        # 그리고 result 리스트에 모든 data가 순서대로 담긴 상태일 것이다.
        # 이 result를 반환하면 끝
        return result
    
# 전위 순회(preoder traversal)
# 루트, 왼쪽 서브트리, 오른쪽 서브트리 순으로 방문하는 순회방법
# 전위, 중위, 후위의 기준은 루트를 좌우를 포함하여 어느 위치에서
# 루트의 데이터를 조회하는지를 가리킨다.
# 모든 순회 함수는 재귀함수로 구현된다.
def preorder(node:Node):
    if not node: return # 기본 케이스
    # 서브트리들보다 루트 노드의 데이터를 먼저 조회
    print(node.data, end=' ') # 루트 
    preorder(node.left) # 왼쪽 -> 재귀 케이스
    preorder(node.right)# 오른쪽 -> 재귀 케이스

# 중위 순회
# 왼쪽 서브트리, 루트(data), 오른쪽 서브트리
def inorder(node: Node):
    if not node: return # 기본 케이스
    inorder(node.left) # 왼쪽 -> 재귀 케이스
    print(node.data, end=' ') # 루트 
    inorder(node.right)# 오른쪽 -> 재귀 케이스

# 후위 순회
# 왼쪽, 오른쪽, 루트
def postorder(node: Node):
    if not node: return # 기본 케이스
    postorder(node.left) # 왼쪽 -> 재귀 케이스
    postorder(node.right)# 오른쪽 -> 재귀 케이스
    print(node.data, end=' ') # 루트

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    print(bt.display())
    print("=" * 10)

    # 전위순회의 특징
    # 좌우의 서브트리를 순회하기 전에 데이터를 출력한다
    # 루트노드부터 왼쪽 서브트리를 먼저 출력하는 형태를 가지게 된다.
    print("\n전위순회:")
    preorder(bt.root)

    # 중위순회의 특징
    # 왼쪽 서브트리를 모두 순회한 뒤, 리프노드를 만나면
    # 오른쪽 서브트리를 순회하기 전에 데이터를 출력한다.
    # 왼쪽에 위치한 노드부터 순회하여 리프노드의 데이터를 출력하는
    # 성질을 가지게 된다.
    print("\n중위 순회")
    inorder(bt.root)

    # 후위순회
    # 좌우 서브트리를 모두 순회한 뒤 리프노드부터
    # 데이터를 출력한다.
    # 왼쪽 서브트리의 가장 아래 레벨부터 출력을 시작하여
    # 루트노드까지 출력하며 올라간다
    # 하지만 루트노드는 출력하지 않고 오른쪽 서브트리로 진입하여
    # 마찬가지로 가장 아래 레벨부터 출력하여 올라가
    # 가장 마지막에 루트노드를 출력한다.
    print("\n후위 순회")
    postorder(bt.root)
