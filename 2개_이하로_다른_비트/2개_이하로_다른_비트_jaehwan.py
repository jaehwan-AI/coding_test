# value
# 10진수 -> 2진수 : bin(value), format(value, 'b')
# 2진수 -> 10진수 : int(bin(value), 2)

def solution(numbers):
    answer = []
    for number in numbers:
        target = number + 1
        while 1:
            cnt = 0
            tmp = format(number ^ target, 'b')
            for s in tmp:
                if s == '1':
                    cnt += 1
            if cnt <= 2:
                break
            target += 1
        answer.append(target)
    return answer

# -> 테스트 10, 11 시간초과

def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수는 맨 뒤가 0이므로 +1해서 return
        if number % 2 == 0:
            answer.append(number+1)
        # 홀수는 맨 뒤에서부터 0인 인덱스를 찾아서 1로 바꾸고 그 뒤를 0으로 바꿔서 return
        else:
            target = list('0'+format(number, 'b'))
            idx = ''.join(target).rfind('0')
            target[idx] = '1'
            target[idx+1] = '0'
            answer.append(int(''.join(target), 2))
    return answer

# 비트 마스크 개념으로도 풀 수 있음
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-Python
