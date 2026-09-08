def solution(n):
    mod = 1234567
    
    if n <= 2 :
        return n
    pre, curr = 1, 2
    for _ in range(3, n+1) :
        pre, curr = curr , (pre + curr) % mod
        
    return curr

# 점화식 dynamic programming
# 선택지가 매 단계 유한하게 반복
# "마지막 한 수"를 되감아 보는 습관
# 결과가 폭발적으로 커지는데 "나머지를 리턴하라"고 할 때