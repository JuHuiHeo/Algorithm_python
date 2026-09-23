def solution(n, left, right):
    answer = []
    # 12 22
    # 123 223 333
    # 1234 2234 3334 4444
    # 12345 22345 33345 44445 5555
    # 첫번째는 모든 숫자 순서대로
    # 두번째는 두번째숫자 2개 순서대로~
    # 세번째는 세번째숫자 3개 순서대로~
    # 마지막은 마지막 숫자 다채우기
    
    # (left // n) + (left % n) = left
    # left // n >> j
    # left % n >> 
    for k in range(left, right + 1):
        i = k // n   # 행: n개씩 묶었을 때 몇 번째 묶음인지
        j = k % n    # 열: 그 묶음 안에서 몇 번째인지
        answer.append(max(i, j) + 1)
    return answer