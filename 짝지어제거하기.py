#짝지어 제거하기.py  Lv.2
def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])  # stack이 비어있다면 push()
            
        else:
            if s[i] == stack[-1]:       # stack 마지막 값과 s[i]가 같다면 pop()
                stack.pop()
            else:
                stack.append(s[i])      # stack 마지막 값과 s[i]가 다르면 push()

    if stack : 
        return 0                 # stack이 비어있지 않다면 return 0
    else : 
        return 1                     # stack이 비어있다면 return 1


# pop()
# 리스트의 i 번째 원소를 리턴하고 삭제
# list = [0,1,2,3]
# list.pop()  [맨마지막 원소 pop]
# list.pop(2) [0,1,3]
 