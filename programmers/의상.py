from collections import Counter

def solution(clothes):
    # 코니는 각 종류별로 최대 1가지 의상만
    # 하루에 최소 한 개의 의상
    # 하나라도 다르면 다른 의상
    
    count_arr = []
    for day in clothes :
        count_arr.append(day[1])
    
    count_arr = Counter(count_arr)
    
    answer = 1
    for i in count_arr.values():
        answer *= (i + 1)

    return answer - 1