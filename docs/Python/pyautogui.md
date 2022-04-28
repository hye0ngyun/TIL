# pyautogui

마우스 움직임을 제어하는 라이브러리, 티스토리 블로그의 스킨을 변경했을 때 다크테마에서 예전에 작성했던 글의 가독성에 문제가 생기는 바람에 모든 글을 수정하려는데, 글을 수정할 때 티스토리 에디터에서는 글자 색을 변경하려면 모두 마우스로 작업해야 한다.
이 과정에서 손목에 굉장한 피로가 올 것으로 파악돼 드래그된 글을 원하는 색으로 변경하는 마우스 매크로를 만들기 위해 학습한다.

## installation

설치는 cmd에서 아래 명령어 입력

```cmd
pip install pyautogui
```

라이브러리 적용은 파이썬 파일의 상단에 아래 코드 입력

```python
import pyautogui as auto # pyautogui를 pyautogui대신 auto라고 사용하기 위해(라이브러리명은 짧은게 코드를 작성하기 편하다.)
```

## pyautogui의 기본적인 함수

- `size()`: 주모니터의 사이즈를 (w, h) 튜플 형태로 반환한다.

```python
print(auto.size()) # Size(width=1920, height=1080)
screenWidth, screenHeight = auto.size()
print(screenWidth, screenHeight) # (1920, 1080)
```

- `position()`: 현재 마우스 포인터의 좌표값을 (x, y) 튜플 형태로 반환한다.

```python
position = auto.position()
currentMouseX, currentMouseY = auto.position()
print(position) # Point(x=556, y=57)
print(currentMouseX, currentMouseY) # (556, 57)
```

- `moveTo(x, y)`: 마우스를 x좌표, y좌표로 이동한다.

```python
auto.moveTo(100, 150) # 100, 150으로 마우스 포인터 이동
```

- `click([x, y])`: 현재 마우스 포인터 위치에서 클릭 이벤트를 발생시킨다. x, y좌표가 입력된 경우 해당 위치로 이동(moveTo)후 클릭 이벤트를 발생(클릭한다.)시킨다.

```python
auto.click() # 현재 마우스 포인터 위치 클릭
auto.click(50, 50) # 50, 50 좌표 클릭
```

- `write(str, [interval=sec])`: 현재 포커싱된(클릭된 입력창)곳에 str을 입력한다. interval이 입력된 경우 입력된 값의 초(sec)마다 str을 0번인덱스부터 마지막 인덱스까지 입력한다.

```python
auto.write('hello world')
```

- `press(key_name)`: 입력된 key_name을 누르는 이벤트를 발생시킨다.

```python
auto.press('esc') # esc 키 입력
print(auto.KEY_NAMES) # auto.press()에 전달 가능한 모든 키 이름을 출력
```


# 참고 자료

- https://pyautogui.readthedocs.io/en/latest/
