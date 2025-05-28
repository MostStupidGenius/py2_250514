# part3_bfs.py
# 너비우선탐색(BFS)
# 너비우선탐색은 시작지점을 기준으로 같은 거리에 있는
# 노드부터 접근하는 방식을 취한다.
# 즉, 이진트리로 보자면 같은 레벨부터 차례로 내려가는 형태를 취한다.

def bfs(graph, start):
    # 방문한 노드를 저장할 set 자료구조 초기화
    visited = set()
    # 시작 노드를 포함한 큐 생성
    queue = [start]
    # 시작노드를 방문처리
    visited.add(start)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 가장 왼쪽(가장 오래된) 노드를 꺼냄(선입선출)
        vertex = queue.pop(0)
        # 현재 방문중인 노드를 출력(공백으로 구분)
        print(vertex, end=" ")

        # 현재 노드의 이웃 노드들을 순회하며 queue에 담기
        for neighbor in graph[vertex]:
            # 아직 방문하지 않은 이웃 노드에 대해
            if neighbor not in visited:
                # 방문 처리
                visited.add(neighbor)
                # 큐의 오른쪽(마지막)에 (방문하지 않은)이웃 노드 추가
                queue.append(neighbor)

data = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'E', 'F'],
    'D' : ['B'],
    'E' : ['B', 'C', 'F'],
    'F' : ['C', 'E', 'G'],
    'G' : ['F']
}

if __name__ == "__main__":
    from part1_dfs import graph
    # bfs(graph, 'A') # A B C D E F
    bfs(data, 'A') # A B C D E F G