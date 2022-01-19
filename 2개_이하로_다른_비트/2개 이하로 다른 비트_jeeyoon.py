def solution(numbers):
    answer = []
    for num in numbers:
        if num%2 == 0:
            answer.append(num+1)
        else:
            two = list(bin(num)[2:])
            if len(set(two)) == 1:
                two.insert(1,'0')
            else:
                idx = 0
                for i, n in enumerate(two):
                    if n == '0':
                        idx = i
                two.pop(idx+1)
                two.insert(idx, '1')
            ten = int(''.join(two), 2)
            answer.append(ten)
    return answer

solution([1,3,5,7,9,11,13])
