from itertools import permutations
def solution(numbers):
    prime_set = set() # 만들 수 있는 모든 소수
    
    #1. 모든 숫자 조합을 만든다.
    for i in range(len(numbers)):
        numbers_permutation = permutations(list(numbers), i+1)
        numbers_perm_list = list(map(int,map(''.join, numbers_permutation)))
        prime_set |= set(numbers_perm_list)
    
    #2. 소수가 아닌 수를 제외한다.
    prime_set -= set(range(0,2))
    lim = int(max(prime_set) ** 0.5) + 1
    for i in range(2, lim):
        prime_set -= set(range(i*2,max(prime_set)+1, i))
        
    return len(prime_set)