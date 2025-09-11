def solution(arr):
    answer = []
    j = 0
    
    for i in arr:
        if j == 0:
            answer.append(i)
            j+=1
        else:
            if i == answer[j-1]:
                pass
            else: 
                answer.append(i)
                j+=1
    return answer