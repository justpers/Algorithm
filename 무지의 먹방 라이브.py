def solution(food_times, k):
    while k > 0:
        answer = 0
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= 1
                k -= 1
                answer = i + 1
        if answer == 0:
            break
    
    if answer == 0:
        answer = -1
    else:
        if answer >= len(food_times):
            answer -= len(food_times)    
            
        for j in range(answer, len(food_times)):
            if food_times[j] == 0:
                continue
            else:
                answer = j
                break
            
        if food_times[answer] == 0:
            for k in range(0, answer):
                if food_times[k] == 0:
                    continue
                else:
                    answer = k
                    break
        answer += 1
    
    return answer