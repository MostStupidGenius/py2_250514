# part4_sort_select.py
# 선택 정렬
# 선택 정렬은 배열 전체를 순회하면서 가장 작은 값의 index를 저장하여
# 배열의 마지막 요소와의 비교가 끝나면, 해당 index와
# 정렬 순서의 요소를 서로 맞교환하여
# 가장 작은 값을 왼쪽으로 정렬하는 알고리즘이다.
# 시간 복잡도는 최악의 경우, 개수의 제곱 회 만큼의 정렬을 시행할 수 있다.
# O(n^2)으로 표현된다.

# 리스트 인수를 전달받아 그 요소를 작은값부터 큰값으로
# 오름차순 정렬하는 선택 정렬 함수
def selection_sort(arr: list):
    # 리스트의 길이를 추출
    n = len(arr)

    # 리스트의 전체를 순회하는 반복문
    for i in range(n):
        # 현재 위치를 최소값의 인덱스로 초기화
        min_idx = i

        # 정렬이 일어났는지 여부를 담은 변수
        has_sorted = False

        # i+1번째부터 끝까지 순회하며 최소값 찾기
        for j in range(i+1, n): # i+1번째부터 n번째(마지막)까지 순회
            # 만약 arr의 j번째 요소가 min_idx번째 요소보다 작다면
            if arr[j] < arr[min_idx]:
                # min_idx의 값을 j로 설정한다. -> 가장 작은 값의 인덱스 추출
                min_idx = j
                # print(f"현재 찾은 작은인덱스{min_idx}")
                # 정렬이 일어났으므로 has_sorted를 True로 변경
                has_sorted = True
        if not has_sorted: # 순서가 변경된 적이 없으면
            break # 다음 반복으로 이동하여 필요없는 행동 최소화
        
        # 현재 가장 작은 값이 들어갈 위치의 값과
        # 찾아낸 가장 작은 값의 위치를 서로 바꾼다.

        # - 일반적인 언어에서의 방법
        # dummy = arr[i]
        # arr[i] = arr[min_idx]
        # arr[min_idx] = dummy
        # - 파이썬에서 사용 가능한 문법
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print(arr)
    # 정렬된 리스트를 반환
    return arr # 전달받은 요소를 직접 수정하여 반환

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted = selection_sort(arr)
    print("선택 정렬 결과: ", sorted)