from collections import Counter

def solution(want, number, discount):
    answer = 0   
    
    # 해당 자리부터 슬라이싱 해서 10개 끊고 개수 반환
    # number이랑 dic 합쳐서 일치하면 result += 1
    # 자리 += 1
    answer_want = []

    for k in range(len(number)) :
        for p in range(number[k]) :
            answer_want.append(want[k])

    answer_count = Counter(answer_want)

    for i in range(len(discount)) :
        if (10+i) > len(discount) :
            break
        ten = discount[i:10+i]
        ten_count = Counter(ten)

        mi = answer_count - ten_count
        if len(mi) == 0 :
            answer += 1
    return answer

## counter끼리 빼면 동일 요소 검사할 수 있음