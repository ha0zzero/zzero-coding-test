def solution(id_list, report, k):
    answer = {}
    count = {}
    board = {}
    bye = []
    aaa = {}

    report = set(report) # 동일한 유저 신고 1회 처리

    for i in id_list:
        board[i] = []
        count[i] = 0
        answer[i] = 0

    # 신고 횟수 count
    for r in report:
        신고자, 불량자 = r.split(' ')
        
        count[불량자] += 1
        board[신고자].append(불량자)
    
    # 정지된 ID 획득
    for c, _ in count.items():
        # print(count[c])
        if count[c] >= k:
            bye.append(c)
    
    print(bye)

    for 신고자, 불량자_list in board.items():
        for 불량자 in 불량자_list:
            for 정지자 in bye:
                if 불량자 == 정지자:
                    answer[신고자] += 1

    return [a for a in answer.values()]