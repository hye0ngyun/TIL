# 네이밍 컨벤션
하나 이상의 영어 단어로 구성된 식별자(변수, 함수, 객체 등)를 만들 때 가독성 좋게 단어를 한눈에 구분하기 위해 규정한 명명 규칙

## 네이밍 컨벤션 유형
- 카멜 케이스(camelCase)

```js
var firstName;
```
- 스네이크 케이스(snake_case)

```js
var first_name;
```
- 파스칼 케이스(PascalCase)

```js
var FirstName;
```
- 헝가리안 케이스(typeHungarianCase)

```js
var strFirstName; // type + identifier
var $elem = document.getElementById('myId'); // DOM 노드
var observable$ = fromEvent(document, 'click'); // RxJS 옵저버블
```

## 자바스크립트의 네이밍 컨벤션
1. 변수나 함수: 카멜 케이스
2. 생성자 함수, 클래스: 파스칼 케이스
3. ECMAScript 사양 함수, 객체: 카멜, 파스칼 케이스