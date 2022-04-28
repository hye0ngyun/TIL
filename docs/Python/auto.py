from turtle import width
import keyboard as key
import pyautogui as auto

# 티스토리 글작성 에디터에서 글자 색 변경 단축키가 없어서 만든 프로그램
# 1920x1280 크기 화면에 브라우저를 전체화면으로 한 경우 정확히 적용 가능하다.
# 추후 추가적인 학습으로 프로그램 확장 가능성 존재

color_open_x = 830
color_open_y = 140

def mac1():
  temp_x, temp_y = auto.position()
  auto.click(color_open_x, color_open_y)
  auto.click(785, 216)
  auto.moveTo(temp_x, temp_y)

def mac2():
  temp_x, temp_y = auto.position()

  auto.click(color_open_x, color_open_y) # 글자색 열기 버튼
  auto.click(756, 193) # 글자색 버튼

  auto.click(856, 137) # 글자 배경색 열기 버튼
  auto.click(783, 192) # 글자 배경색 버튼

  auto.moveTo(temp_x, temp_y)
key.add_hotkey('ctrl+shift+x', mac1)
key.add_hotkey('ctrl+shift+z', mac2)

while True: # 프로그램 실행 동안 핫키를 입력받을 수 있도록 하기 위해
  if key.read_key() == 'esc': # 프로그램을 종료하기 위해서 esc키를 입력하면 된다.
    print('esc break')
    break

print(key.remove_all_hotkeys()) # 프로그램이 종료될 때는 매핑된 핫키를 모두 삭제해주기 위해
# 만약 삭제하지 않은 경우 컴퓨터 사용에 의도치 않은 동작이 발생할 수 있기 때문에 keyboard 라이브러리를 사용해서 핫키를 매핑한 경우 프로그램 마지막엔 반드시 핫키를 삭제해주자.
