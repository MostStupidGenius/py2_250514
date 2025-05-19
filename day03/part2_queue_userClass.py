# part2_queue_userClass.py
# list를 상속받아서 queue 클래스를 직접 만들어보자.

class Queue(list):
    def pop(self, index=0): # index의 기본값을 0번째 요소로 수정
        super().pop(index) # 나머지 기능은 부모 클래스인 list의 기능을
        # 그대로 사용한다.

if __name__ == "__main__":
    que = Queue()
    que.append(1)
    que.append(2)
    que.append(3)
    print(que)

    que.pop()
    print(que)