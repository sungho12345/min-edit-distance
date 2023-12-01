[![Python](https://img.shields.io/badge/Python-Used-blue.svg)](https://shields.io/#/)

# min-edit-distance_word_recommend_system

최소편집거리 알고리즘을 기반의 단어 추천 코드입니다. 사용자가 입력한 문자와 단어장 안의 문자가 같아지기 위해서 몇번의 추가(Add), 편집(Edit), 삭제(Delete)가 이루어져야 하는지를 계산해서 최소인 단어들을 추출합니다.

# Legal Terms with Korean
최소편집거리 알고리즘을 한국의 법률단어에 적용했습니다.
오탈자가 입력되면 올바른 법률용어로의 결과를 출력해줍니다.

## Installation
소프트웨어가 공개되어 있는 github링크를 복제하여 사용하시면 됩니다.
```
git clone https://github.com/sungho12345/min-edit-distance.git
```

## How to use
사용방법은 다음과 같습니다.

```
>>> from MeD.wordRecommend import wordRecommend
>>> user_word = "흡수하ㅂ병"
>>> print(wordRecommend((user_word, wordlist, sepList)))
['흡수합병']
```

## Reference
