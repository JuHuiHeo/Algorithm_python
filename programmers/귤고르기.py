from collections import Counter

def solution(k, tangerine):
    c = sorted(Counter(tangerine).values(), reverse=True)

    sum = 0
    check = 0
    for i, name in enumerate(c) :
        if sum < k :
            check += 1
            sum += name
        if sum >= k :
            return check


# 유의 할 점 : list의 끝까지 다 훑는 테스트 케이스 체크해보기

# 그리디 + 카운팅
# 빈도수 세기(Counter) → 내림차순 정렬 → 앞에서부터 누적하며 조건 만족 시 중단

# 1) 목표를 나타내는 말
# "종류의 수를 최소로"
# "최소 몇 개를 골라야"
# "최대 몇 명에게 나눠줄 수 있는지"

# 2) 중복이 존재한다는 신호
# "같은 것이 여러 개 있다", "크기별로", "종류별로", "이름이 같은"
# 예시 배열에 값이 반복되어 나옴 ([1, 3, 2, 5, 4, 5, 2, 3])

# 3) 총량 조건
# "k개를 채워야 한다", "절반 이상", "전체의 X% 이상"
# 누적합이 어떤 기준선을 넘으면 되는 구조