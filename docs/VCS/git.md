# 깃(git)

git은 프로젝트의 형상 관리를 위한 도구(Version Control System)중 하나이다.
팀 프로젝트 간에 주요하게 사용되는 협업 툴이다.
깃허브라는 내 깃 내역을 업로드할 수 있는 웹 사이트가 있다.

## 깃 워크플로우(git workflow)
- working directory
  - untrack
    - 새로 만들어진 파일이거나 기존에 존해하는 프로젝트에서 깃을 초기화 하는 경우 파일의 정보가 없는 트래킹하지 않은 파일
  - track
    - unmodified
      - 수정되지 않았다. staging area로 이동할 수 없다.
    - modified
      - 수정됐다. staging area로 이동할 수 있다.
- staging area
  - git add 명령어를 통해 파일이 들어오는 공간
- .git directory
  - git commit 명령어를 통해 파일이 들어오는 공간

## 깃 이그노어(git ignore)

## 깃 명령어

- `git commit` - 세이브한다.
  - 게임의 세이브에 해당하는 행동을 git에서 커밋이라 한다. 즉, 언제든 커밋한 시점으로 되돌아 갈 수 있다. 커밋을 하려면 저장을 **원하는 파일들을 묶어서** 커밋 명령을 수행한다.
- `git add` - 스테이지에 올린다.
  - 커밋을 할 때 파일들을 묶는다고 했는데, 이 묶는 작업이 **스테이지에 파일을 올리는 작업**이다.
- `git push` - github에 업로드한다.
  - 스테이지와 커밋은 로컬에서만 저장이 된다. 깃허브라는 리모트(원격 서버)에 내 깃 내역을 업로드 한다.
- `git fetch`
- `git pull`
- `git clone`
