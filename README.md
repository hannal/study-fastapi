FastAPI Study
==============

좋아요(star), 구독(follow), 알람 설정(watch)까지.

## 0. 차림판

- [FastAPI 스터디](#1-fastapi-스터디)
- [FastAPI + Poetry Boilerplate](#2-boilerplate)

----


## 1. FastAPI 스터디
- [스터디 페이지](./projects/tutorial-user-guide)
  - [FastAPI 공식 문서 Tutorial user guide 스터디](./projects/tutorial-user-guide)
  - Mob programming (예정)

----

## 2. Boilerplate

이 저장소와 [projects/hello-graphql](./projects/hello-graphql) 디렉터리가 Boilerplate 구축을 위한 것.

### Boilerplate 구성

- pyproject.toml 기반으로 Python Project 구성
- monorepo 느낌나게 패키지 분리
  - `projects` : 프로젝트 
  - `contrib` :  각 프로젝트에서 사용하는 공통 패키지
- poetry로 패키지 관리
- `Makefile`로 주요 명령어 관리
  - 프로젝트 단위로 관리하므로 프로젝트 디렉터리에 존재


### 프로젝트 구성

- 각 프로젝트는 `projects` 디렉터리 안에 위치하며, 프로젝트 이름과 동일한 디렉터리에는 해당 프로젝트의 시스템 설정 파일이 위치.
- 각 프르젝트를 구성하는 주요 단위는 앱(app)이며, `projects/<프로젝트>/apps`에 위치.
  - `projects/hello_graphql/apps/hello`는 `hello_graphql` 프로젝트의 `hello` 앱을 의미.


Scripts
--------

`projects/hello_graphql/Makefile` 파일을 기반은 명령어들.

### 패키지 관련

- `make package-install` : Poetry 패키지 설치
- `make package-update` : Poetry 패키지 업데이트
- `make package-show` : Poetry 패키지 목록 보기

### 실행 관련

- `make runserver` : local 서버 실행. (`http://127.0.0.1:8899`)
- `make shell` : Poetry 패키지 의존 관계를 반영하여 Python shell 실행 (virtualenv처럼)

### 테스트 관련

- `make test-apps` : apps의 모든 테스트 수행.
- `make test-apps/hello` : hello app의 테스트만 수행.
- `make cov-apps` : apps의 모든 테스트 수행. (coverage 검사 포함)
- `make cov-apps/hello` : hello app의 테스트만 수행. (coverage 검사 포함)

### Lint 관련

- `make lint-check` : Black을 이용해 Lint 검사 수행.
- `make lint-reformat` : Black을 이용해 Lint 검사하고 재구성(reformatting) 수행.

### Poetry 관련

- `make config-venv` : Poetry virtualenv configuration 반영.


Server Application Settings
---------------------------

### hello_graphql/settings.py

구동 환경 별로 settings 를 구성하려면 이 모듈에 작업.

- `LocalAppSettings`, `TestAppSettings` : local, test 환경에 사용할 settings.
- `EnvName` : 환경 이름.
- `environments` : `EnvName`과 `*AppSettings`를 짝지어놓은 객체.


### dot env files

`*AppSettings`는 dot env 파일을 참조하여 설정을 override 함. `*AppSettings.Config.env_file` 참조.


Editor
-------

- [Configure a Poetry environment](https://www.jetbrains.com/help/pycharm/poetry.html) : PyCharm에 Poetry 설정.

참조
-----

- [fastapi-realworld-example-app](https://github.com/nsidnev/fastapi-realworld-example-app) : 이 Boilerplate 를 만들 때 기반으로 삼은 boilerplate.
