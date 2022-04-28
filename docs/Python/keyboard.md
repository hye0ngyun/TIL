# keyboard

python에서 키 입력을 감지하는 라이브러리

## installation

cmd

```cmd
pip install keyboard
```

python

```python
import keyboard as key
```

## keyboard의 기본적인 함수

- `add_hotkey(str, func)`: str에 전달된 핫키를 입력시, func에 전달된 함수가 실행되도록 등록한다.

```python
def mac1():
  print('pressed ctrl+shift+1')
key.add_hotkey('ctrl+shift+1', mac1) # ctrl+shift+1이 입력된 경우 mac1함수가 실행된다.
```

- `remove_hotkey(str)`: str에 등록된 핫키를 삭제한다.

```python
key.remove_hotkey('ctrl+shift+1') # ctrl+shift+1 핫키가 삭제된다.
```

- `remove_all_hotkeys()`: 등록된 모든 핫키를 삭제한다.

```python
key.remove_all_hotkey() # 등록된 모든 핫키를 삭제한다.
```
- `read_key()`: 키입력 이벤트가 발생 시 입력되는 키 값을 반환한다.
```python
while True:
  if key.read_key() == 'esc:
    print('esc pressed. break')
    break
  else:
    print(key.read_key())
```