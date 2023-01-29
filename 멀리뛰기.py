#프로그래머스  멀리뛰기  lv2  python
def solution(n):
    if n<3:
        return n
    d=[0]*(n+1)
    print(d)
    d[1]=1
    d[2]=2
    print(d)
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    
    return d[n]%1234567
print("dfdf",solution(5))

#####################################
def jumpCase(num):
    answer = 0
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return jumpCase(num-1)+jumpCase(num-2)

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))