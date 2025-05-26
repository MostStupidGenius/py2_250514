# part3_sort_heap.py
# 힙 정렬
# 최대 힙(max heap) 구조를 활용한 정렬 방법으로
# 최대 힙이란, 완전이진트리구조에서 루트 노드를 가장 큰 값으로 정렬한 것이다.
# 정확히 표현하면, 부모노드는 자식노드보다 크거나 같은 값을 가지게
# 설정하는 것을 가리킨다.
# 루트 노드가 가장 큰 값이라는 것을 이용한 선택정렬의
# 개선 알고리즘이다.

# 힙정렬을 수행하는 함수
def heap_sort(data: list) -> list:
    # 데이터의 길이 확인
    n = len(data)

    # 최대 힙 구성 단계
    # 마지막 비단말 노드부터 시작하여 루트까지 heapify 수행
    # (n // 2 - 1)은 마지막 비단말 노드의 인덱스
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    
    # 정렬 단계
    # 힙에서 최대값(루트 노드의 데이터)를 하나씩 꺼내어
    # 배열 끝부터 채운다.
    for i in range(n-1, 0, -1):
        # 최대값을 현재 힙의 마지막 요소와 교환
        data[0], data[i] = data[i], data[0]
        # 루트 노드에 대해 heapify를 수행하여 최대 힙 속성 복구
        heapify(data, i, 0)
    
    # 정렬 완료, 반환
    return data

def heapify(data: list, n: int, i: int) -> None:
    # largest는 인덱스를 담는 변수로 
    # 현재 heapify 대상이 된 노드 중 가장 큰 노드를 찾아내기 위해
    # 사용된 변수다.
    # 현재 노드를 largest로 초기화
    # 가장 큰 값을 찾기 위해 초기값을 설정하는 것이다.
    largest = i

    # 왼쪽 자식 노드의 인덱스 계산(2i + 1)
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식노드가 힙 크기 범위 내에 있고
    # 현재 largest보다 큰 경우
    if left < n and data[left] > data[largest]:
        # 가장 큰 인덱스를 left로 설정
        largest = left
    
    # 오른쪽 자식 비교
    if right < n and data[right] > data[largest]:
        largest = right

    # largest가 현재 노드(i)와 다르다면 가장 큰 값이 i가 아닌 것이므로
    # 가장 큰 요소와 i간의 교환이 필요하다.
    if largest != i:
        # 현재 노드와 largest 위치의 값을 교환
        data[i], data[largest] = data[largest], data[i]
        # 교환된 자식 노드에서 다시 heapify를 수행하여
        # 최대 힙 속성 유지
        heapify(data, n, largest)

if __name__ == "__main__":
    import random

    # 예시 데이터 준비
    # data = [3, 6, 8, 9, 1, 2, 1]
    # 랜덤 데이터 만들기
    data = [random.randrange(1, 100, 1) for i in range(100)]
    print(data)
    # 퀵 정렬 진행
    sorted = heap_sort(data)
    # 정렬된 데이터 확인
    print(sorted) # 1, 1, 2, 3, 6, 8