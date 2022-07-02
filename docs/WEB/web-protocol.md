# web protocol

## HTTP (Hyper Text Transfer Protocol)

HTTP는 인터넷상에서 데이터를 주고 받기 위한 서버/클라이언트 모델을 따르는 프로토콜이다. 여기서 프로토콜은 통신 규악을 의미한다.

HTTP는 애플리케이션 레벨의 프로토콜이고, TCP/IP 위에서 작동한다.

HTTP로 보낼 수 있는 데이터는 HTML문서, 이미지, 동영상, 오디오, 텍스트 문서 등 여러 종류가 존재한다.

## URL (Uniform Resourece Locator)

웹에서 웹 페이지를 정의하고 접근하기 위해 URL을 사용한다.
아래는 URL의 일반적인 형식이다.

```http
protocol://domain_name:port/document_name?parameters
```

위 형식에서 각 단위의 역할은 아래와 같다.

- protocol: 문서를 접근하기 위해 사용하는 프로토콜 이름
  - ex) http, https, ftp
- domain_name: 문서가 있는 컴퓨터의 도메인 이름
  - ex) naver.com, google.com
- port: 서버가 어떤 포트 숫자를 바라보고 있는지 (선택사항)
  - ex) 8080, 8000
- document_name: 서버 컴퓨터에 있는 특정 문서의 이름
  - ex) product, product/shirts
- parameter: 페이지에 넘기는 변수, `?`로 시작하며 여러 파라미터가 존재하는 경우 `&`로 이어서 표현한다. (선택사항)
  - ex) ?query=keyword, ?query=keyword&page=2

각 역할을 살펴봤을 때 아래는 실제 url의 예시이다.

```http
https://developer.mozilla.org/en-US/search?q=URL
```

위 URL을 해석하면 `https` 프로토콜을 이용하고, `developer.mozilla.org`의 이름을 갖는 컴퓨터(서버)에서 `en-US/search` 문서에서 `q`라는 파라미터에 `URL`이라는 값을 전달한다.
