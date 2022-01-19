from collections import defaultdict
import math
def solution(fees, records):
    in_dic = defaultdict(int)
    result = defaultdict(int)
    # 출차시간 - 입차시간을 result에 더해서 저장
    for case in records:
        time, car, i_o = case.split(' ')
        car = int(car)
        h,m = time.split(':')
        time = int(m) + int(h)*60
        if i_o == 'IN':
            in_dic[car] = time
        if i_o == 'OUT':
            result[car] += time - in_dic[car]
            del in_dic[car]
    # 출차를 하지 않은 경우
    if len(in_dic) != 0:
        for k, v in in_dic.items():
            result[k] += 23*60+59 - v
    # 주차 비용 계산
    for k, v in result.items():
        new_v = fees[1]
        if v > fees[0]:
            new_v += fees[3]*math.ceil(float(v-fees[0])/fees[2]) # int 연산자끼리의 나눗셈은 소수점이 안나오나??
        result[k] = int(new_v)
    sorted_result = [i[1] for i in sorted(result.items(), key = lambda x:x[0])]
    return sorted_result