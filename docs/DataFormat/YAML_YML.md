# YAML, YML

- YAML은 XML, C, 파이썬, 펄에서 정의된 e-mail 양식에서 개념을 얻어 만들어진 '사람이 쉽게 읽을 수 있는' 데이터 직렬화 양식이다.
- 데이터 포맷 중 하나인 JSON은 YAML의주석 스타일을 제외하고 매우 비슷하다.
- docker-compose에서 사용한다.

## YAML 요소

- YAML은 모든 데이터를 리스트, 해시, 스칼라 데이터의 조합으로 표현된다.

```YAML
# 리스트
--- # Favorite movies, block format
- Casablanca
- Spellbound
- Notorious
--- # Shopping list, inline format
[Casablanca, Spellbound, Notorious]
```

```YAML
# 해시
--- # Block
name: John Smith
age: 33
--- # Inline
{name: John Smith, age: 33}
```

```YAML
# 해시의 리스트
- [name: John Smith, age: 33]
- name: Mary Smith
  age: 2

# 리스트의 해시
men: [John Smith, Bill Jones]
women:
  - Mary Smith
  - Susan Williams
```
