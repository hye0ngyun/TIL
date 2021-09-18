# API(Application Programming Interface)

## API 간단 설명

**API는 메뉴판이다.**
웹툰 보내주는 서버가 있다면 아래와 같이 메뉴가 있을 것이다.

1. 신과함께(메뉴1)
2. 이말년시리즈(메뉴2)
3. 헬퍼(메뉴3)
   위처럼 세 가지 메뉴가 있을 때 유저가 3번 보여주세요~ 하면 `웹툰서비스 API`(메뉴판)를 이용해서 메뉴3인 헬퍼를 보여준다.
   `웹툰서비스 API`: 웹툰서버와 손님이 웹툰을 주고받기위한 방법(코드)

```js
// 이'/detail/:id' url로 get 요청을 하면~
app.get('/detail/:id', function(req, res) { // 이 부분이 API
  df.collection('웹툰').fundOne({ _id: parseInt(요청.params.id) }, function (에러, 결과) {
    console.log(결과);
    res.render('detail.ejs', { data: 결과 }); // 이 코드를 실행해주세요~
});
```

## API가 가져야 할 내용

1. 요청방식(method)

   - 데이터 달라고 할것인지(get)
   - 데이터 보낼 것인지(post)

2. 무슨자료를 요청할지(url; endpoint)

   - 어떤 데이터를 요청할 것인지?(웹툰, 댓글, 뉴스)

3. 자료요청에 필요한 추가정보(parameter)

   - 내 아이디, 이름, 몇화 보고싶은지

4. +웹의 경우 `REST API`라는 원칙에 따라 작성하면 좋음

## 실생활 API 사용 예

브라우저라는 API 요청 도구가 있다.
브라우저 주소창이 API 요청 코드를 짜는 곳(GET요청 가능)
그러나 일반인이 직접 코드를 짜는 것이 아닌 버튼을 클릭할 경우 웹상에서 코드가 작성이 되어 요청된다.
즉, 우리는 매일 API를 요청하고 있다.

## API 종류

1. public API

   - 누구나 사용 가능한 공개 API

2. private API

   - 사내에서 몰래쓰는 API

3. partner API

   - 미리 정해둔 사람들만 쓰는 API

4. +모든 프로그램은 API를 가질 수 있다.

   - Windows API: 윈도우 운영체제 기능들을 사용할 수 있는 API(알림, 설치/삭제,)
   - Database 관리프로그램 API: DB 입출력 기능들을 사용할 수 있는 API
   - XX 프로그램 API: XX 기능들을 사용할 수 있는 API
