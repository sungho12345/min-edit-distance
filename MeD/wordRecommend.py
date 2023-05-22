#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 사전을 만들어서 최소편집거리로 추천해주는 함수 
# 단어 리스트 만들기
# 최소편집거리 알고리즘을 통해 리스트의 단어와 입력받은 단어의 편집거리를 구함
# 입력된 단어와 리스트의 단어들 사이의 편집거리가 작은 단어 출력

def wordRecommend(user_word):
    f = open("englishwords.txt", 'r')
    line = f.readlines()
    f.close()

    words_list = []
    for each in line:
      words_list.append(each.replace("\n", ''))
    print(words_list)

    minEditDistance_list = []   # 편집거리 따로 리스트를 만듦

    for word in words_list:    # 단어 리스트를 반복문으로 돌면서 입력받은 단어와 리스트에 있는 단어 사이의 편집거리 계산
      len1 = len(user_word)
      len2 = len(word)

      # dp = [[0] * (len2 + 1) for j in range(len1 + 1)]

      table = []    # user_word와 word의 table 생성
      for i in range(len1 + 1):
        row = []
        for j in range(len2 + 1):
          row.append(0)
        table.append(row)
    # user_word와 word/ 리스트 첫번째 줄에 1 ~ len* + 1 입력   
      for i in range(1, len1 + 1):
        table[i][0] = i
      for i in range(1, len2 + 1):
        table[0][i] = i
    # 알고리즘
    # [1, 1]부터 시작
      for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
          if user_word[i-1] == word[j-1]:
            table[i][j] = table[i-1][j-1]
          else:
            table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) + 1

      minEditDistance_list.append(table[len1][len2])


    # 단어 리스트와 편집거리 리스트를 딕셔너리로 만듦 (단어:편집거리) https://qna.programmers.co.kr/questions/8551/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%91%90%EA%B0%9C%EC%9D%98-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A5%BC-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%9D%98-%ED%82%A4key%EC%99%80-%EB%B0%B8%EB%A5%98value-%EA%B0%92%EC%9C%BC%EB%A1%9C-%EB%84%A3%EC%9D%84-%EC%88%98-%EC%9E%88%EB%82%98%EC%9A%94
    dic = {name:value for name, value in zip(words_list, minEditDistance_list)}

    minEditDistance_list.sort()   # 편집거리를 sort함

    # minED_list = minEditDistance_list

    minEditDistance_set = set(minEditDistance_list)

    minED_list = list(minEditDistance_set)    # 리스트를 튜플 -> 리스트 변환(중복 제거)

    min_word_list = []

    # 최소편집거리가 제일 작은 두개의 인덱스를 이용해 딕셔너리 key값 출력
    for i in range(0, 1): 
      for key,value in dic.items():
        if value == minED_list[i]:
          min_word_list.append(key)
    return min_word_list


# In[6]:


user_word = 'apple'
wordRecommend(user_word)

