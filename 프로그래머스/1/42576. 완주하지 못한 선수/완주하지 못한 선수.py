# participant에는 있고 competion에는 없는 한 명을 찾기

def solution(participant, completion):
    answer = ''
    # 두 리스트를 sorting
    participant.sort()
    completion.sort()
    # completion list의 length 만큼 돌면서, participant list에 존재하지 않는 한 선수 찾기
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 전부 다 돌아도 없을 경우, 마지막 주자가 완주 못한 선수
    return participant[len(participant)-1]