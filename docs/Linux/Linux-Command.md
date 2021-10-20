# 리눅스 명령어

## 현재 작업 디렉터리 확인
- `pwd` - present working directory
  - 

## 작업 디렉터리 이동
- `cd [dirname]` - change directory
  - 작업 디렉터리를 `[dirname]`으로 변경(이동)한다.
  - ex) `cd d1` - d1이라는 디렉터리로 이동한다.

## 
- `ls` - list
  - 작업 디렉터리의 목록을 보여준다.

## 디렉터리 생성
- `mkdir` - make directory
  - 새로운 디렉터리를 만든다.

## 삭제
- `rm` - remove
  - 파일이나 디렉터리를 삭제한다.
  - `rm [dirname]`
    - 디렉터리를 삭제한다. 디렉터리 내부에 파일이 없을 경우에만 삭제된다. 내부에 파일이 있을 경우 삭제되지 않는다.
  - `rm -r [dirname]`
    - 디렉터리를 삭제한다. 디렉터리 내부의 파일들을 모두 재귀적(r opt)으로 없앤다. 즉, 디렉터리를 강제로 삭제한다.
  - `rm [filename]`
    - 파일을 삭제한다.