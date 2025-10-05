def solution(citations):
    h_list = sorted(citations, reverse = True)

    for h, c in enumerate(h_list):
        if h >= c:
            return h
    return len(citations)