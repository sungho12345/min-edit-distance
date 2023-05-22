[![Python](https://img.shields.io/badge/Python-Used-blue.svg)](https://shields.io/#/)

# min-edit-distance_word_recommend_system

최소편집거리 알고리즘을 기반의 단어 추천 코드


## installation
소프트웨어가 공개되어 있는 github링크를 복제하여 사용하시면 됩니다.
```
git clone https://github.com/sungho12345/min-edit-distance.git
```

## how to use
사용방법은 다음과 같습니다.
```python
>>> from MeD.wordRecommend import wordRecommend
>>> user_word = 'apple'
>>> print(wordRecommend(user_word))
['ample', 'appale', 'appl', 'Apple', 'appled', 'apples', 'apply', 'capple', 'dapple']
```
