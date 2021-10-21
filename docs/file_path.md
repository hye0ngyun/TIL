# 파일 경로(file path)
파일 경로는 파일 시스템에서 각 파일들이 위치하는 경로이다.
파일 경로는 OS에 따라 표현 방식이 상이하다.
- Windows
  - 
- Linux

## 작업 디렉토리(working directory)
- CLI에서 현재 위치하는 디렉토리를 작업하는 디렉토리, 작업 디렉토리 라고 한다.
  - ex) windows 기준 CLI에 `D:\projects>`라고 표현된다면 현재 작업 디렉토리는 `D:\projects>`이다.

## 파일 경로 표현
- 절대 경로(absolute path)
  - 루트 디렉토리부터 표현하려는 파일까지의 경로를 모두 표현하는 방식
  - ex) `C:\Users\username\Documents\f1.txt`
- 상대 경로(relative path)
  - 작업 디렉토리부터 표현하려는 파일까지의 경로를 상대적으로 표현하는 방식
  - ex) 작업 디렉토리가 C:\Users\username 라고 한다면 `.\Documents\f1.txt`

## 와일드카드(wild card)
- `/var/log/**`
  - /var/log 디렉토리에서 모든 파일들, 모든 자식 디렉토리를 재귀적으로 일치시킨다.
- `/var/log/**/*.log`
  - /var/log 디렉토리에서 이름이 `.log`로 끝나는 모든 파일과 모든 하위 디렉토리의 모든 파일을 반복적으로 일치시킨다.
- `/home/*/.bashrc`
  - 모든 사용자의 홈 디렉토리에 있는 모든 `.bashrc` 파일과 일치시킨다.
- `/home/*/.ssh/**/*.key`
  - 모든 사용자의 홈 디렉토리안의 모든 사용자의 `.ssh` 디렉토리의 모든 `.key`로 끝나는 파일과 일치시킨다.

## 참고자료
- [경로에서 와일드카드의 사용법](https://help.sumologic.com/03Send-Data/Sources/04Reference-Information-for-Sources/Using-Wildcards-in-Paths)