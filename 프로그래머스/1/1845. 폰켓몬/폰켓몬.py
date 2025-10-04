from collections import Counter
def solution(nums):
    
    # 1. nums를 counter
    count_num = Counter(nums)
    # 2. len(counter.key) < len(nums)/2 : len(counter.key) 아니면 len(nums)/2
    if len(list(count_num.keys())) < len(nums)/2:
        return len(list(count_num.keys()))
    else: 
        return len(nums)/2