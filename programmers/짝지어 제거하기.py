def solution(s):
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    if len(stack) != 0 :
        answer = 0
    else :
        answer = 1
        
    return answer