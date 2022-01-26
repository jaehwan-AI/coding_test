import pandas as pd


# pandas solution - 효율성 테스트 시간 초과
def solution(info, query):
    answer, langs, jobs, careers, foods, scores = [], [], [], [], [], []
    for i in info:
        tmp = i.split(' ')
        langs.append(tmp[0])
        jobs.append(tmp[1])
        careers.append(tmp[2])
        foods.append(tmp[3])
        scores.append(int(tmp[4]))
    df = pd.DataFrame({'lang':langs, 'job':jobs, 'career':careers, 'food':foods, 'score':scores})
    
    for que in query:
        con_df = df.copy()
        query_split = [q for q in que.split(' ') if q != 'and']
        for j in range(len(query_split)):
            if j == 0:
                if query_split[j] != '-':
                    con_df = con_df[(con_df.lang == query_split[j])]
            elif j == 1:
                if query_split[j] != '-':
                    con_df = con_df[(con_df.job == query_split[j])]
            elif j == 2:
                if query_split[j] != '-':
                    con_df = con_df[(con_df.career == query_split[j])]
            elif j == 3:
                if query_split[j] != '-':
                    con_df = con_df[(con_df.food == query_split[j])]
            elif j == 4:
                con_df = con_df[(con_df.score >= int(query_split[j]))]
        answer.append(con_df.shape[0])
    return answer

# list solution - 효율성 테스트 시간 초과
def solution(info, query):
    answer, infos = [], []
    
    for i in info:
        infos.append(i.split(' '))
    
    for que in query:
        cnt = 0
        querys = [q for q in que.split(' ') if q != 'and']
        print(querys)
        for person in infos:
            lang_flag, job_flag, career_flag, food_flag, score_flag = False, False, False, False, False
            for j in range(len(querys)):
                if j == 0:
                    if querys[j] != '-':
                        if person[j] == querys[j]:
                            lang_flag = True
                        else:
                            break
                    else:
                        lang_flag = True
                elif j == 1:
                    if querys[j] != '-':
                        if person[j] == querys[j]:
                            job_flag = True
                        else:
                            break
                    else:
                        job_flag = True
                elif j == 2:
                    if querys[j] != '-':
                        if person[j] == querys[j]:
                            career_flag = True
                        else:
                            break
                    else:
                        career_flag = True
                elif j == 3:
                    if querys[j] != '-':
                        if person[j] == querys[j]:
                            food_flag = True
                        else:
                            break
                    else:
                        food_flag = True
                elif j == 4:
                    if int(person[j]) >= int(querys[j]):
                        score_flag = True
            if lang_flag and job_flag and career_flag and food_flag and score_flag :
                cnt += 1
        answer.append(cnt)
    return answer
