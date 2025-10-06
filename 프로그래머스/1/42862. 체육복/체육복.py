def solution(n, lost, reserve):
    # n: 전체 학생 수, lost: 도난당한 학생 배열, reserve: 여분 학생 배열
    # return: 전체학생수-여전히못빌린학생수
    
    # 여벌이 있지만 도난당한 학생 중복 제거
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    # 정렬
    new_lost.sort()
    new_reserve.sort()
    
    for l in new_lost[:]:
        if l - 1 in new_reserve:
            new_reserve.remove(l - 1)
            new_lost.remove(l)
        elif l + 1 in new_reserve:
            new_reserve.remove(l + 1)
            new_lost.remove(l)
    return n - len(new_lost)