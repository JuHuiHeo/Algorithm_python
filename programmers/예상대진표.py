def solution(n,a,b):

    answer = 0
    a_turn, b_turn, a_num, b_num = 0, 1, 0, 0
    
    # 1 2 3 4 5 6
    # 0 1 1 2 2 3
    # 1 0 1 0 1 0
    
    # 2로 나눈 나머지가 1이면 +1 해서 2로 나눈 값
    # 2로 나눈 나머지가 0 이면 자기 자신을 2로 나눈 값
    
    while True :
        a_num , b_num = a % 2, b % 2
        
        if a_num == 1 :
            a_turn = (a + 1) // 2
        else : 
            a_turn = a // 2
        if b_num == 1 :
            b_turn = (b + 1) // 2
        else :
            b_turn = b // 2
        answer += 1 

        if (a_turn == b_turn) :
            break
        
        
        a, b = a_turn, b_turn
        
    return answer