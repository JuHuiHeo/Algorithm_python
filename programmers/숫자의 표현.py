def solution(n):
    # 투포인터
    count = 0
    start, end, total = 1, 1, 1
    
    while start <= n :
        if total == n :
            count += 1
            end += 1
            total += end
        elif total <= n :
            end += 1
            total += end
        else :
            total -= start
            start += 1
    return count