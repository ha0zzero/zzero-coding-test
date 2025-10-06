from collections import deque
def solution(bridge_length, weight, truck_weights):
    time,total_weight = 0,0
    waiting = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    
    while bridge: # 다리 위에 트럭이 남아 있는 동안
        time += 1
        total_weight -= bridge.popleft() # 맨 앞 트럭, 빈칸 나가기
        
        if waiting: # waiting이 비어있지 않으면
            if total_weight + waiting[0] <= weight:
                truck = waiting.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
    
    return time