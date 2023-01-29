#programmers h-index.py   lv2 
#citations[i]는 i번 논문이 인용된 횟수이고 article_count-i는 인용된 논문의 개수를 최댓값부터 하나씩 줄여나간 것이다. (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
def solution(citations):
    citations.sort()
    article_count = len(citations)  # 5

    for i in range(article_count): # (0,1,2,3,4)
        if citations[i] >= article_count-i:
            print("df",article_count-i)
            return article_count-i    #5-2=3
        
    return 0
