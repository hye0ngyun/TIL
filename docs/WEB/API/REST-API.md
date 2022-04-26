# REST API(REpresentaional State Transfer API)

API 또는 애플리케이션 프로그래밍 인터페이스는 애플리케이션이나 디바이스가 서로 간에 연결하여 통신할 수 있는 방법을 정의하는 규칙 세트이다. REST API는 REST(REpresentational State Trasnfer) 아키텍처 스타일의 디자인 원칙을 준수하는 API이다.

## REST API의 탄생

컴퓨터 과학자인 Roy Fielding 박사가 2000년에 자신의 박사학위 논문에서 처음으로 정의한 REST는 개발자에게 비교적 높은 수준의 유연성과 자유를 제공한다. 이러한 유연성은 REST API가 마이크로서비스 아키텍처에서 컴포넌트와 애플리케이션의 연결을 위한 일반적인 방법으로 등장하게 된 이유 중 단지 하나에 불과하다.

## REST 구성

- 자원(Resource) - URI
- 행위(Verb) - HTTP Method
- 표현(Representations)

## REST의 특징

1. Uniform (유니폼 인터페이스)
   URI로 지정한 리소스에 대한 조작을 **통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일**을 말한다.

2. Stateless (무상태성)
   REST는 무상태성 성격을 갖는다. 즉, **작업을 위한 상태정보를 따로 저장하고 관리하지 않는다.** 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 된다. 따라서 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않기 때문에 구현이 단순해진다.
3. Cacheable (캐쉬가능)
   REST의 가장 큰 특징 중 하나는 **HTTP라는 기존 웹표준을 그대로 사용**하기 때문에, 웹에서 사용하는 기존 인프라를 그대로 활용이 가능하다는 것이다. 따라서 HTTP가 가진캐싱 기능이 적용 가능하다. HTTP 프로토콜 표준에서 사용하는 **Last-Modified태그나 E-Tag를 이용하면 캐싱 구현이 가능**하다.
4. Self-descriptiveness (자체 표현 구조)

REST의 특징 중 하나로 **REST API 메시지만 보고도 이를 쉽게 이해**할 수 있는 자체 표현 구조를 가진다. 5. Client-Server 구조

REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 **각각의 역할이 확실히 구분**되기 때문에 클라이언트와 서버에서 개발해야 하는 내용이 명확해지고 서로 의존성이 줄어들게 된다.

6. 계층형 구조

REST 서버는 **다중 계층으로 구성**될 수 있으며 보안, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수도 있고 Proxy, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있게 한다.

## REST API 디자인 가이드

REST API 설계 시 가장 중요한 항목은 다음 두 가지로 요약할 수 있다.

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.

# 참고 자료

- https://ko.wikipedia.org/wiki/REST
- https://meetup.toast.com/posts/92
- https://www.ibm.com/kr-ko/cloud/learn/rest-apis
