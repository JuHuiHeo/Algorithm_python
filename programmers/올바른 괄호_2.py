def solution(s):    
    sum = 0
    answer = ""
    
    for i in range(len(s)) :
        if s[i] == "(" :
            sum += 1
        else :
            sum -= 1
        if sum < 0 :
            return False
    if sum == 0 :
        return True
    else :
        return False