# 리눅스 명령어

## 현재 작업 디렉터리 확인
- `pwd` - print working directory

## 작업 디렉터리 이동
- `cd [dirname]` - change directory
  - 작업 디렉터리를 `[dirname]`으로 변경(이동)한다.
  - ex) `cd d1` - d1이라는 디렉터리로 이동한다.

## 파일 목록 출력
- `ls` - list
  - 작업 디렉터리의 목록을 보여준다.

## 디렉터리 생성
- `mkdir [dirname]` - make directory
  - 새로운 디렉터리를 만든다.

## 삭제
- `rm` - remove
  - 파일이나 디렉터리를 삭제한다.
  - `rm [filename]`
    - 파일을 삭제한다.
  - `rm -r [dirname]`
    - 디렉터리를 삭제한다. 디렉터리 내부의 파일들을 모두 재귀적(r opt)으로 없앤다. 즉, 디렉터리를 강제로 삭제한다.
  

## 원하는 파일 목록 출력
- `grep` - globally search a regular expression and print

## 서버 포트 오픈 확인
- `nc` - NetCat
  - 대상 서버의 포트가 오픈됐는지 확인한다.
  - `nc [대상서버 IP] [대상 PORT]`

## 압축
- `tar`
  - `tar -cvf` 압축
  - `tar -xvf` 압축 해제

## 파일 내용 출력
- `cat [option] [filename]` - concateneate
  - `cat filename`
    - 파일을 출력한다.
  - `cat filename1 filename2`
    - 여러 파일을 순서대로 이어서 출력한다.
  - `cat filename1 filename2 > filename3`
    - 1, 2의 내용을 3에 저장한다.
    - 만약 3이 존재한다면 덮어쓰고, 없다면 생성한다.
  - `cat filename1 >> filename2`
    - 1의 내용을 2에 덧붙인다.
  - `cat > newfilename`
    - 새로운 파일을 만들 때 사용한다.
    - `touch newfilename`과 비슷하지만, `cat newfilename`은 내용을 입력하고 `CTRL + D`를 눌러 입력한 내용을 저장한다.

## 파일 내용 상단 출력
- `head [filename]`
  - 위에서 10줄을 출력한다.

## 파일 내용 하단 출력
- `tail [filename]`
  - 아래서 10줄을 출력한다.

## 포트 상태 확인
- `netstat -anop | grep {port} `