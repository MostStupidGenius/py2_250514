# part1_dfs.py
# DFS
# 깊이 우선 탐색 알고리즘은 그래프의 정점(Vertex)과
# 정점과 정점 사이를 잇는 간선(Edge)을 탐색하는 알고리즘을
# 가리킨다.
# 이러한 그래프를 나타내는 방법으로는
# dict 자료구조를 통해 서로의 연결관계를 나타내는 것이다.
graph = {
    'A' : ['B', 'C'], # A 정점이 B, C와 연결되어있다.
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'], # 연결된 정점이 하나이므로
    # 이진트리로 치면 리프노드(단말노드)에 해당한다.
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}
# 깊이 우선 탐색은 한 경로를 끝까지 탐색한 뒤
# 더 이상 진행할 수 없으면(단말정점이면)
# 가장 최근 갈림길로 돌아가 방문하지 않은(visited)
# 정점을 탐색해 나간다.
# stack 자료구조나 재귀함수(recursive)를 통해 
# 구현할 수 있다.

# 1. 재귀함수를 통한 DFS 구현
def dfs_recursive(graph_var, start, visited=None):
    """
    graph_var: DFS를 수행할 그래프 데이터
    start: 그래프에서 시점이 될 정점 이름
    visited: set 자료구조로, 방문한 노드를 검사하기 위한 변수다.
    """
    # visited가 None이면 새로운 set 생성 (최초 호출 시)
    if visited is None: visited = set()

    # 현재 노드(start)를 방문 처리
    visited.add(start)
    print(start, end=" ") # 방문한 노드(정점) 출력

    # 현재 노드의 이웃 노드들을 탐색
    for next_node in graph_var[start]:
        # 아직 방문하지 않은 이웃 노드에 대해 재귀적으로 DFS 수행
        if next_node not in visited:
            #방문한 set에 next_node가 포함되어 있지 않으면
            dfs_recursive(graph_var, next_node, visited)

# 2. 스택 구조를 활용한 반복적 DFS 구현
def dfs_iterative(graph_var, start):
    # 방문한 노드를 저장할 set 자료구조 변수
    visited = set() # 방문한 노드를 저장할 set
    stack = [start] # 시작 노드를 스택에 추가

    # 스택이 비어있지 않은 동안 반복
    while stack:
        # 스택에서 노드를 꺼냄(가장 최근 추가된 노드)
        vertex = stack.pop() # 마지막 노드를 꺼냄
        
        # 아직 방문하지 않은 노드라면
        if vertex not in visited:
            visited.add(vertex)
            # 추출한 노드 출력
            print(vertex, end=" ") # 노드의 값을 출력한 뒤 공백문자로 마무리

            # 현재 노드의 이웃 노드들을 스택에 추가
            # 이때, visited의 요소와 비교하여 방문하지 않은 노드만 추가한다.
            to_add_vertex = [x for x in graph_var[vertex] if x not in visited]
            stack.extend(to_add_vertex)

if __name__ == "__main__":
    # 위에서 미리 만든 graph를 탐색하는데
    # 'A'노드부터 시작한다.
    # dfs_recursive(graph, 'A') # A B D E F C
    dfs_iterative(graph, 'A') # 오른쪽부터 탐색
    # A C F E B D
        
