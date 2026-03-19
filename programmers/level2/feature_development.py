# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 문제 요약: 각 기능의 완료일을 구하고, 앞 기능 완료일 기준으로 배포 그룹 묶기
# 접근: 완료일 배열 생성 후 standard/count 패턴으로 그룹화

import math

def solution(progresses, speeds):
    answer = []
    job = []

    for p, s in zip(progresses, speeds):
        job.append(math.ceil((100 - p) / s))

    count = 1
    standard = job[0]
    for i in range(1, len(job)):
        if job[i] <= standard:
            count += 1
        else:
            answer.append(count)
            count = 1
            standard = job[i]
    answer.append(count)

    return answer