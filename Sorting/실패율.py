"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889 (실패율)
"""

def solution(N, stages):
    my_dict = {i:0 for i in range(1, N+1)}
    my_list = []
    result = []
    total = len(stages)

    for stage in stages:
        if stage in my_dict:
            my_dict[stage] += 1
    
    for stage in range(1, N+1):
        if my_dict[stage] == 0:
            my_list.append((0, stage))
        else:
            my_list.append((my_dict[stage] / total, stage))
            total -= my_dict[stage]
    
    my_list.sort(key = lambda x: (-x[0], x[1]))

    for info in my_list:
        result.append(info[1])

    return result
