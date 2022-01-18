from math import ceil


def solution(fees, records):
    answer = []
    park, cars = {}, {}
    for recode in records:
        tmp = recode.split(' ')
        if tmp[-1] == 'IN':
            park[tmp[1]] = tmp[0]
        else:
            in_h, in_m = map(int, park[tmp[1]].split(':'))
            out_h, out_m = map(int, tmp[0].split(':'))
            total = ((out_h*60)+out_m) - ((in_h*60)+in_m)
            if tmp[1] not in cars.keys():
                cars[tmp[1]] = total
            else:
                cars[tmp[1]] += total
            del park[tmp[1]]
    if len(park) >= 1:
        for k in park:
            in_h, in_m = map(int, park[k].split(':'))
            out_h, out_m = 23, 59
            total = ((out_h*60)+out_m) - ((in_h*60)+in_m)
            if k not in cars.keys():
                cars[k] = total
            else:
                cars[k] += total
    
    cars = sorted(cars.items())
    for car in cars:
        if car[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (ceil((car[1] - fees[0]) / fees[2]) * fees[3]))
    return answer
