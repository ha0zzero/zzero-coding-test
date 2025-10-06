import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        frist_spicy = heapq.heappop(scoville) # 가장 맵지 않은 애
        second_spicy= heapq.heappop(scoville) # 두번째로 맵지 않은 애
        mix_spicy = frist_spicy + (second_spicy*2) # 섞인 음식
        heapq.heappush(scoville, mix_spicy) # 섞인 음식 넣기
        answer += 1

    return answer