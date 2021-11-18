# 리눅스 쉘(shell) 파일

## 출력
- echo: 출력하고 자동 줄바꿈
- printf: c언어와 유사한 동작

`print.sh` 쉘 파일
```sh
#!bin/bash

echo 'echo shell'
echo echo 입니다.
printf 'prinf shell'
```
`$ print.sh` 쉘 파일 실행 결과
```
echo shell
echo 입니다.
printf shell
```


## 파라미터 전달
`test.sh` 쉘 파일
```sh
#!/bin/bash

echo "shell parameter test"

echo "파라미터 개수: $#"
echo "첫 번째 파라미터: $1"
echo "모든 파라미터 내용: $@"
```
`$ test.sh 1 2 3` 쉘 파일 실행 결과
```
shell parameter test
파라미터 개수: 3
첫 번째 파라미터 1
모든 파라미터 내용 1 2 3
```

## 함수
```sh
function name() { # 함수 선언
  echo 'name function'
}
name # 함수 호출
```
