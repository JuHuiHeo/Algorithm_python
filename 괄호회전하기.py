def solution(s):
    # 어케 밀수있을까 두개를 붙여
    pair = {"]" :"[", ")" : "(" , "}" : "{"}

    new_s = s+s
    check = 0
    
    for i in range(len(s)) :
        check_s = new_s[i:len(s)+i]
        stack = []
        flag = True
        
        for word in new_s[i:len(s)+i] :
            if word in "[({" :
                stack.append(word)
            else :
                if not stack or (pair[word] != stack[-1]) :
                    flag = False
                    break
                stack.pop()

        if flag == True and len(stack)==0 :
            check += 1
    return check

# 마지막 것 비교 할때 stack