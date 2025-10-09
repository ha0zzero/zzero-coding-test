def solution(survey, choices):
    answer = {'R':0, 'T':0, 'C':0, 'F':0,
              'J':0, 'M':0, 'A':0, 'N':0} #[R, T, C, F, J, M, A, N]

    result = ''

    for s, c in zip(survey, choices):
        if c == 1: answer[s[0]] += 3
        elif c == 2: answer[s[0]] += 2
        elif c == 3: answer[s[0]] += 1
        elif c == 4: pass
        elif c == 5: answer[s[1]] += 1
        elif c == 6: answer[s[1]] += 2
        else: answer[s[1]] += 3
    
    if (answer['R'] > answer['T']) or (answer['R'] == answer['T']): result += 'R'
    else: result += 'T'

    if (answer['C'] > answer['F']) or (answer['C'] == answer['F']): result += 'C'
    else: result += 'F'

    if (answer['J'] > answer['M']) or (answer['J'] == answer['M']): result += 'J'
    else: result += 'M'

    if (answer['A'] > answer['N']) or (answer['A'] == answer['N']): result += 'A'
    else: result += 'N'

    return result