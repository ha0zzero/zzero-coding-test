# 대기큐: 작업 번호, 요청 시각, 소요 시간 - 처음에는 비어있음
# 대기큐가 비어있지 않으면 -> 우선순위 높은 작업을 꺼래는데, (소요 시간 짧을 수록, 요청 시각이 빠를 수록, 작업 번호가 작을 수록)
# 작업 수행 시작하면 그 작업만 수행

# jobs: [[0, 3], [1, 9], [3, 5]] # 요청 시각, 소요 시간, 작업 번호는 없구나.. 작업번호를 추가..!해주면 됨

import heapq

def solution(jobs):
    answer = 0        # 총 소요시간 합
    time = 0          # 현재 시각
    cnt = 0           # 처리한 작업 수
    start = -1        # 직전 작업이 끝난 시점
    heap = []

    jobs.sort()  # 요청 시각 기준으로 정렬

    while cnt < len(jobs):
        # 현재 시각까지 들어온 요청들 heap에 넣기 (소요시간 기준)
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, (job[1], job[0]))  # (소요시간, 요청시각)
        
        if heap:
            work_time, req_time = heapq.heappop(heap)
            start = time
            time += work_time
            answer += (time - req_time)  # 요청~완료까지 걸린 총 시간
            cnt += 1
        else:
            time += 1  # 대기중이라면 시간 1초 증가

    return answer // len(jobs)