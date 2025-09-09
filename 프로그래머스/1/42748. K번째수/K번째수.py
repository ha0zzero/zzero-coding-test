def solution(array, commands):
    answer = []

    for r in range(len(commands)):
        i = commands[r][0]
        j = commands[r][1]
        k = commands[r][2]
    
        arr = array[i-1:j]
        arr2 = sorted(arr) # [2,3,5,6]
        arr3 = arr2[k-1]
        answer.append(arr3)
    return answer