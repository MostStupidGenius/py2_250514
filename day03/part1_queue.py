# part1_queue.py
# 자료구조 - Queue
# 큐 자료구조는 먼저 입력한(선입) 데이터를 먼저 내보내는(선출)
# 자료구조를 의미한다.
# 큐 자료구조는 주로 실행 순서를 정렬하고 먼저 들어온 작업부터
# '순서대로' 진행하기 위해 만들어진 자료구조다.
# 이러한 queue 자료구조는 파이썬 라이브러리 deque로도 구현가능하지만
# list의 pop(0)로도 충분히 구현이 가능하다.

# deque로 queue 자료구조 구현하기
from collections import deque

def play_deque():
    que = deque() # 대기열이 비어있는 que 생성
    # 요소 추가
    que.append(1) # 1번째로 입력된 값
    que.append(2) # 2번째
    que.append(3)

    print(que)

    # queue 자료구조는 먼저 들어간 값부터 순서대로 추출하여 사용한다.
    que.popleft() # 순서상 먼저 들어간 1번이 왼쪽에 위치하므로
    # popleft()를 통해 먼저 들어간 값을 추출한다.
    # 추출 후, 2번째 값은 1번 위치로 이동한다.
    
    print(que) # 가장 먼저 들어간 1이 삭제된 queue를 출력한다.

# list를 이용한 queue 구현하기
def play_list_queue():
    que = list() # 빈 리스트 만들기
    que.append(1) # append는 마지막에 값을 붙여넣는다.
    que.append(2)
    que.append(3)

    # 먼저 들어간 0번째 요소를 .pop(0)로 제거, 추출한다.
    poped = que.pop(0)
    
    # 남은 que를 확인한다.
    print(que)

if __name__ == "__main__":
    # play_deque()
    play_list_queue()





