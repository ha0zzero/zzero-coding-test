# 공통: 1, 4, 7 왼손, 3, 6, 9 오른손 // 2, 5, 8, 0 더 가까운 엄지
# 조건: if 거리 동일: 왼손잡이 - 왼손, 오른손잡이 - 오른손


# 왼손 위치 확인용, 오른손 위치 확인용 => 문자
# 사용한 손 담는 리스트

# 숫자로 접근하는게 아니라, 위치로 접근을 한다면?

def solution(numbers, hand):
    answer = ''
    keypad = {
    1: (0,0), 2: (0,1), 3: (0,2),
    4: (1,0), 5: (1,1), 6: (1,2),
    7: (2,0), 8: (2,1), 9: (2,2),
    '*': (3,0), 0: (3,1), '#': (3,2)
    }
    l_x, l_y, r_x, r_y = 3,0,3,2 
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            l_x, l_y = keypad[num]
        elif num in (3, 6, 9):
            answer += 'R'
            r_x, r_y = keypad[num]
        else:
            x, y = keypad[num]
            if abs(l_x-x)+(abs(l_y-y)) < abs(r_x-x)+abs(r_y-y):
                answer += 'L'
                l_x, l_y = x, y
            elif abs(l_x-x)+abs(l_y-y) > abs(r_x-x)+abs(r_y-y):
                answer += 'R'
                r_x, r_y = x, y
            else:
                if hand == 'left':
                    answer += 'L'
                    l_x, l_y = x, y
                else:
                    answer += 'R'
                    r_x, r_y = x, y
                                         
    return answer

