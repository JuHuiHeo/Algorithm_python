def solution(n):
    a, b = 0, 1
    for _ in range(n):
        # 여기서 a, b를 한 칸씩 밀면서 % 1234567
        a, b = b, (a+b) % 1234567
        
    return a

## (a+b)modm=((amodm)+(bmodm))modm
## 시간 복잡도 : O(n) = 2 + n * 1 = n