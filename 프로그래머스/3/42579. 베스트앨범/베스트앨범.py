# 장르 별 가장 많이 재생된 노래 두 개씩 출력
## 재생수의 합이 가장 많은 장르 먼저 수록
## 정렬: 장르 내 재생 많이 되면 내림차순, 고유번호 오름차순 // 앞에서 2개 고유번호 return

from collections import defaultdict
def solution(genres, plays):
    # genre별 재생 수, genre별 재생횟수+고유번호
    song_sum = defaultdict(int)
    song_list = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        song_sum[g] += p
        song_list[g].append((p, i))
    # 정렬
    for g in song_list:
        song_list[g].sort(key = lambda x: (-x[0], x[1]))
        
    sorted_genres = sorted(song_sum.items(), key=lambda x: -x[1])
    
    answer = []
    for g, _ in sorted_genres:
        for p, idx in song_list[g][:2]:
            answer.append(idx)
    return answer