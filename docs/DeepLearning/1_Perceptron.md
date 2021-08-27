# 퍼셉트론

- 퍼셉트론은 `다수의 신호`를 `입력`으로 받아 `하나의 신호`를 `출력`한다.
- 여기서 말하는 `신호`는 전류나 강물처럼 `흐름`이라고 생각하면 좋다.
- 퍼셉트론 신호는 '흐른다/안 흐른다(1이나 0)'의 두 가지 값을 가질 수 있다.

![perceptron](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99BDCE4D5B98A1022C)

- 위 그림은 입력으로 2개의 신호를 받은 퍼셉트론이다.
- $x_1, x_2$는 **입력 신호**, $y$는 **출력**, $w_1, w_2$는 **가중치**를 뜻한다.
- 그림의 원을 **뉴런** 혹은 **노드**라고 부른다.
- 입력 신호가 뉴런에 보내질 때는 각각 고유한 **가중치**가 곱해진다($w_1x_1, w_2x_2$).
- 뉴런에서 보내온 신호의 총 합이 정해진 한계를 넘을 때만 1을 출력한다(이는 '뉴런이 활성화 한다'라 표현하기도 함).
- 이 한계를 **임계값**이라 하며, $\theta$ 기호$^{theta, 세타}$로 나타냅니다.

## AND 게이트

AND 진리표

| x1  | x2  | y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 1   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 1   | 1   |

```python
def AND(x1, x2):
  w1, w2, b = 0.5, 0.5, -0.7
  y = (w1*x1 + w2*x2) + b
  if y <= 0:
    return 0
  elif y > 0:
    return 1

print(AND(0, 0)) # 0
print(AND(1, 0)) # 0
print(AND(0, 1)) # 0
print(AND(1, 1)) # 1
```

## NAND 게이트

NAND 진리표

| x1  | x2  | y   |
| --- | --- | --- |
| 0   | 0   | 1   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 0   |

```python
def NAND(x1, x2):
  w1, w2, b = -0.5, -0.5, 0.7
  y = (w1*x1 + w2*x2) + b
  if y <= 0:
    return 0
  elif y > 0:
    return 1

print(NAND(0, 0)) # 1
print(NAND(1, 0)) # 1
print(NAND(0, 1)) # 1
print(NAND(1, 1)) # 0
```

## OR 게이트

OR 진리표

| x1  | x2  | y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 1   |

```python
def OR(x1, x2):
  w1, w2, b = 0.5, 0.5, -0.2
  y = (w1*x1 + w2*x2) + b
  if y <= 0:
    return 0
  elif y > 0:
    return 1

print(OR(0, 0)) # 0
print(OR(1, 0)) # 1
print(OR(0, 1)) # 1
print(OR(1, 1)) # 1
```

## XOR 게이트

- XOR는 하나의 직선(단층 퍼셉트론)으로는 구분할 수 없는 문제이다.
- 여러 개의 퍼셉트론(다층 퍼셉트론)으로 구분할 수 있다.

XOR 진리표

| x1  | x2  | s1  | s2  | y   |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1   | 0   |
| 1   | 0   | 1   | 1   | 1   |
| 0   | 1   | 1   | 1   | 1   |
| 1   | 1   | 1   | 0   | 0   |

```python
def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

print(XOR(0, 0)) # 0
print(XOR(1, 0)) # 1
print(XOR(0, 1)) # 1
print(XOR(1, 1)) # 0
```
