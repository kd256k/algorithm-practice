# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 문제 요약: arr에서 연속으로 나타나는 숫자는 하나만 남기고 제거. 순서 유지.
# 접근: prev 변수로 이전 값 기억

def solution(arr):
    prev = arr[0]
    output = [prev]
    
    for value in arr[1:]:
        if value != prev:
            output.append(value)
        prev = value
    return output