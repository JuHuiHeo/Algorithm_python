def solution(n, words):
    answer = []
    seen = set()
    
    # 나머지 > 자기 순서 >> wrong_turn % n
    # 가장 먼저 탈락하는 사람의 번호
    # 그 사람이 자신의 몇 번째 차례에 탈락하는지 >> wrong_turn//n + 1
    seen_word = ""
    wrong_turn = 0
    
    for i, word in enumerate(words) :   
        if i == 0 :
            seen.add(word)
            seen_word = word   
        elif seen_word[-1] != word[0] :
            wrong_turn = i+1
            break
        elif word in seen:
            print(word, seen)
            wrong_turn = i+1         
            break
        else :
            seen_word = word
            seen.add(word)
    print(wrong_turn)
    
    if wrong_turn == 0 :
        return [0, 0]
    
    if wrong_turn % n == 0 :
        answer.append(n)
        answer.append(wrong_turn//n)
    else :
        answer.append(wrong_turn % n)
        answer.append(wrong_turn//n + 1)
    
#     print(wrong_turn, n)
#     answer.append(wrong_turn//n)
    
#     wrong / n = 몇번째 + 나머지
    return answer

# set 자료형 은근 많이 쓰이니까 파악해 놓기
# in !!! 짱 좋으니까 기억하기