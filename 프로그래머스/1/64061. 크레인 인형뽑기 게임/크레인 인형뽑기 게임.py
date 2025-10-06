from collections import deque
def solution(board, moves):
    basket = deque() # 인형 바구니
    answer = 0
    
    for move in moves:
        move -= 1
        for j in range(len(board)):
            if board[j][move] != 0:
                인형 = board[j][move]
                board[j][move] = 0
                if basket and basket[-1] == 인형:
                    basket.pop()
                    answer +=2
                else:
                    basket.append(인형)
                break
    return answer