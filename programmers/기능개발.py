def solution(progresses, speeds):
    # 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포 > queue >> progresses

    answer = []
    
    while len(progresses) != 0 :
        progresses = [x + y for x, y in zip(progresses, speeds)]
        count = 0

        while progresses and progresses[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count != 0 :
            answer.append(count)

    return answer

# 리스트끼리 더하는 법 : [x + y for x, y in zip(a, b)]