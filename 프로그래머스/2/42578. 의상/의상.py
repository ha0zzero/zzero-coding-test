from collections import defaultdict
def solution(clothes):
    # 해시 테이블 만들기
    hash_map = defaultdict(int)
    for name, category in clothes:
        hash_map[category] += 1
    # 2. 모든 카테고리별 (입거나 안 입거나) 조합 곱하기
    answer = 1
    for count in hash_map.values():
        answer *= (count + 1)
    # 3. 아무것도 안 입는 경우는 제외
    return answer - 1