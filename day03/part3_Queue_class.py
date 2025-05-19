# part3_Queue_class.py
# queue 라이브러리에 있는 Queue 클래스를 활용하여
# Queue 자료구조 사용해보기

from queue import Queue

if __name__ == "__main__":
    q = Queue()
    # 요소 추가 .put()
    q.put(1)
    q.put(2)
    q.put(3)

    # 값을 추출
    # .get()
    print(q.get()) # 먼저 넣은 값을 추출하여 출력
    
    # Queue 클래스를 쓰는 이유는 멀티 스레드 환경에서 안전하게
    # 사용할 수 있도록 설계되어 있다.
    # 우리가 직접 만든 Queue 클래스는 멀티 스레드 환경에서 문제가 발생할 수 있다.