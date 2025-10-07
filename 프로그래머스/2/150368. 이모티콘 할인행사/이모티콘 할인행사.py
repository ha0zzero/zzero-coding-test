def dcFunc(dc, emoticons):
    return [(c, int((100-c)*0.01*emo)) for c, emo in zip(dc, emoticons)]

from itertools import product
def solution(users, emoticons):
    n = len(emoticons) # 전체 emoticons 수
    discount = [10, 20, 30, 40]

    # 1. 사용자가 받을 수 있는 전체 할인 조합
    all_discount = list(product(discount, repeat = n))

    max_plus = 0
    max_total = 0

    # 2. 할인 조합에 따라서 사용자가 구매할 수 있는 금액
    for dc in all_discount:
        dc_emoticons = dcFunc(dc, emoticons)

        plus = 0
        total = 0

        for user_discount, user_budget in users: # [40, 10000]
            user_sum = 0

            for dc_d, dc_p in dc_emoticons:
                # 유저의 최소 할인율보다 높은 이모티콘만 구매
                if user_discount <= dc_d:
                    user_sum += dc_p
                    
            if user_sum >= user_budget:
                plus += 1
            else:
                total += user_sum

        # 3. 카카오에 최대 이득이 되는 금액 찾기
        if plus > max_plus or (plus == max_plus and total > max_total):
            max_plus = plus
            max_total = total

    return [max_plus, max_total]