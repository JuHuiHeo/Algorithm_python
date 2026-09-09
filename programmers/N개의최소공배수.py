def solution(arr):
    # 두 수의 배수 중 공통이 되는 가장 작은 숫자
    # 배열 안의 수 공배수로 나누고 배열안 다 곱한뒤 공배수 곱하기
    # 최소공배수 : 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다. > 유클리드 호제법
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    answer = 1
    for n in arr:
        answer = answer * n // gcd(answer, n)   # lcm으로 접어나가기

    return answer

# 근데 파이썬은 lcm 지원한다 import math