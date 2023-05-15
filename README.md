[![Python](https://img.shields.io/badge/Python-Used-blue.svg)](https://shields.io/#/)

# min-edit-distance_word_recommend_system

최소편집거리 알고리즘을 기반의 단어 추천 코드

## Requirements
해당 소프트웨어를 사용하고자 하시는 분들은 다음의 파이썬 기반 패키지들을 우선적으로 설치해주셔야 합니다.

* python >= 3.6

## Installation
소프트웨어가 공개되어 있는 github링크를 복제하여 사용하시면 됩니다.

```
git clone https://github.com/sungho12345/min-edit-distance
```

## How to use
```
f = open("./englishwords.txt", 'r')
line = f.readlines()
f.close()

words_list = []
for each in line:
  words_list.append(each.replace("\n", ''))
print(words_list)

user_word = input()   # 단어 입력받기

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


# 단어 리스트와 편집거리 리스트를 딕셔너리로 만듦 (단어:편집거리) 
dic = {name:value for name, value in zip(words_list, minEditDistance_list)}

minEditDistance_list.sort()   # 편집거리를 sort함

# minED_list = minEditDistance_list

minEditDistance_set = set(minEditDistance_list)

minED_list = list(minEditDistance_set)    # 리스트를 튜플 -> 리스트 변환(중복 제거)

min_word_list = []

# 최소편집거리가 제일 작은 두개의 인덱스를 이용해 딕셔너리 key값 출력
for i in range(0, 2): 
  for key,value in dic.items():
    if value == minED_list[i]:
      min_word_list.append(key)
print(min_word_list)
```
