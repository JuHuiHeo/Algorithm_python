def solution(people, limit):
    people = sorted(people, reverse = False)
    start, end = 0, len(people)-1
    answer = 0
    # [50, 50, 70, 80]
    while start <= end :
        # print(people[start],people[end])
        if people[start] + people[end] <= limit :
            start += 1
        end -= 1
        answer += 1

    return answer

# 투 포인터
# 정렬해도 답 안 변하는데, '쌍'요구
# 가장 큰 것이 처리가 강제되는 구조
# 그리디 전략에는 예외 케이스 있는지 항상 확인하기