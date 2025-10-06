import heapq
def solution(operations):
    heap = []
    # return answer

    # 새로운 heap을 만들기
    for oper in (operations):
        if oper[0] == 'I':
            heapq.heappush(heap,int(oper[2:]))
        elif heap and oper[0] == 'D': 
            # heap is not null 이면서 ~ 의 뜻이 맞는지 확인 필요
            if int(oper[2:]) < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)
    if heap:
        return [max(heap),min(heap)]
    else:
        return [0,0]