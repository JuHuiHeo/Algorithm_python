def solution(brown, yellow):
    answer = []
    # [a,b]
    # yellow = (a-2) * (b-2)
    # yellow + brown = a * b
    # b = (yellow + brown) // a
    a = 3
    while True :
        if (a-2) * ((yellow + brown) // a - 2) == yellow :
            answer = [(yellow + brown) // a, a]
            break
        else :
            a += 1   
    return answer