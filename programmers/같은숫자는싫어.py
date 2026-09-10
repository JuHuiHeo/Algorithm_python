def solution(arr):
    answer = []
    
    # 배열에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    # 배열 arr의 원소들의 순서 유지
    # 즉, 스택에서 순차적으로 담되, 이미 있으면 버리기
    
    for i, num in enumerate(arr) :
        if i == 0 :
            answer.append(num)
        if num != answer[-1] :
            answer.append(num)
    return answer