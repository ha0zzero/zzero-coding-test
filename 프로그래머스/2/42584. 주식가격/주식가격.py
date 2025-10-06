from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    stack = []  # 인덱스를 저장

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    # 끝까지 안 떨어진 경우
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - top - 1

    return answer


# 1: 2 3 2 3 - 4초
# 2: 3 2 3 - 3초
# 3: 2 - 1초
# 2: 3 - 1초
# 3: - 0초

