def solution(n):
    answer = 0
    i_num = 0
    num = n+1
    for i in str(bin(n)[2:]) :
        if i == '1' :
            i_num += 1
    
    while True :
        i_num_2 = 0
        
        for i in str(bin(num)[2:]) :
            if i == '1' :
                i_num_2 += 1
                
        if i_num_2 == i_num :
            answer = num
            break
        num += 1

    return answer

# num1 = bin(n).count('1')
# count 함수 쓰는 법 까먹었음