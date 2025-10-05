def solution(array, commands):
    answer = []
    for (i, j, k) in commands:
        sort_array = sorted(array[i-1:j])
        answer.append(sort_array[k-1])
    return answer