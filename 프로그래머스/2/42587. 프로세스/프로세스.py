from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque([(i, p) for i, p in enumerate (priorities)])
    # que: (0,2) (1,1) (2,3) (3,2)
    while que:
        current = que.popleft() # (0,2)
        if any(current[1] < item[1] for item in que):
            que.append(current)
        else:
            answer+=1
            if current[0] == location:
                return answer