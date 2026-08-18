def solution(x):
    answer = []
    answer = list(x)
    
    i = 0
    count_1 = 0
    count_2 = 0
    
    answer_count = []

    
    while True :
        count_1 += 1
        wo_x = []
        for i in answer:
            if i != '0' :
                wo_x.append(i)
            else :
                count_2 += 1
        answer = list(bin(len(wo_x))[2:])

        
        if len(wo_x) == 1 :
            break

    answer_count.append(count_1)
    answer_count.append(count_2) 
    return answer_count

print(solution("110010101001"))