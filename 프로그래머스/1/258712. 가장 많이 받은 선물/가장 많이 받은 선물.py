from itertools import combinations
from collections import defaultdict
def solution(friends, gifts):
    new_gifts = defaultdict(int)
    new_friends = []

    new_friends = list(combinations(friends, 2))
    
    for gift in gifts:
        giver, receiver = gift.split()
        new_gifts[(giver, receiver)] += 1

    gift_index = {f: 0 for f in friends}
    for (giver, receiver), count in new_gifts.items():
        gift_index[giver] += count      # 준 사람은 +count
        gift_index[receiver] -= count   # 받은 사람은 -count

    result = {f: 0 for f in friends}
    for A, B in new_friends:
        gift1 = new_gifts[A, B]
        gift2 = new_gifts[B, A]
        if gift1 > gift2:
            result[A] += 1
        elif gift1 < gift2:
            result[B] += 1
        else:
            # 이번 달에 주고받은 횟수가 같을 때 → 선물지수 비교
            if gift_index[A] > gift_index[B]:
                result[A] += 1
            elif gift_index[A] < gift_index[B]:
                result[B] += 1

    return max(result.values())