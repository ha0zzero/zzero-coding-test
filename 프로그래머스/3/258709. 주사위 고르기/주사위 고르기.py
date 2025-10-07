from itertools import combinations, product
from collections import Counter

def solution(dice):
    n = len(dice)  # 주사위 개수
    all_dice = set(range(n))
    comb_A = list(combinations(all_dice, n // 2))  # A가 가져갈 조합들

    best_prob = 0
    best_comb = None

    for comb in comb_A:
        A = set(comb)
        B = set(all_dice) - A

        # 1. A, B 각각의 주사위 눈 리스트
        dice_A = [dice[i] for i in A]
        dice_B = [dice[i] for i in B]

        # 2. 가능한 모든 합 계산
        sum_A = [sum(p) for p in product(*dice_A)]
        sum_B = [sum(p) for p in product(*dice_B)]

        # 3. 각 합의 빈도 계산
        count_A = Counter(sum_A)
        count_B = Counter(sum_B)

        # 4. A 승리 확률 계산
        win = 0
        total = sum(count_A.values()) * sum(count_B.values())
        for a_sum, a_count in count_A.items():
            for b_sum, b_count in count_B.items():
                if a_sum > b_sum:
                    win += a_count * b_count

        win_prob = win / total

        # 5. 최적 조합 업데이트
        if win_prob > best_prob:
            best_prob = win_prob
            best_comb = list(A)

    return [i + 1 for i in best_comb]
