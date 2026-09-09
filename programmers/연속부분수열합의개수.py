def solution(elements):
    answer = 0
    el = elements + elements
    
    
    sum_list = []
    # 중복 제거는 set으로
    
    start, end, total = 0, 0, 1
    sum_num = el[start]
    
    while start < len(elements):
        # print(start, end)
        if start == end :
            sum_list.append(el[end])
        if total < len(elements) :
            end += 1
            sum_num += el[end]
            sum_list.append(sum_num)
            total += 1
        else :
            start += 1
            sum_num = el[start]
            end = start
            total = 1
        
    sum_list = set(sum_list)
    answer = len(sum_list) 
        
    return answer

# 그냥 작성하면 되는 코드인데 너무 투포인터와 같은 방법론에 매몰
# set을 마지막에 쓰면 메모리 낭비