def solution(citations):
    answer = 0
    
    # h번 이상 인용된 논문 h편 이상
    # 나머지 논문(else) h번 이하
    # h의 최댓값
    

    # [0, 1, 3, 5, 6]
    for h in range(len(citations) + 1):   # h 후보: 0 ~ 논문 수
        count = 0                           # 여기서 초기화
        for cite in citations:
            if cite >= h:
                count += 1
        if count >= h:
            answer = max(answer, h)
    return answer