# 자바스크립트 객체(JavaScript Object)

- 자바스크립트 객체 종류

  1. [네이티브 객체(Native Object)](#1-네이티브-객체)
  2. [호스트 객체(Host Object)](#2-호스트-객체)
  3. [사용자 정의 객체(User-defined Object)](#3-사용자-정의-객체)

## 1. 네이티브 객체

- 네이티브 객체(Native objects os Built-in objects or Global objects)는 ECMAScript 명세에 정의된 객체를 말한다. **네이티브 객체는 환경과 관계없이(선언, 임포트) 언제나 사용할 수 있다.**
- **Object, String, Number, Function, Array, RegExp, Date, Math**와 같은 객체 생성에 관계가 있는 함수 객체와 메소드로

```js
// 자바스크립트의 모든 함수는 Function객체이다. 다른 모든 객체들처럼 Funtion 객체는 new 연산자를 사용해 생성할 수 있다.
let adder = new Function("a", "b", "return a + b");

adder(2, 6); // 8
```

- 네이티브 객체를 Global Objects라고 부르기도 하는데 이것은 전역 객체(Global Object)와 다른 의미로 사용되므로 혼동에 주의하여야 한다.
- 전역 객체(Global Object)는 모든 객체의 최상위 객체를 의미하며 일반적으로 **Browser-side에서는 _window_**, **Server-side(Node.js)에서는 _global_** 객체를 의미한다.

## 2. 호스트 객체

- 호스트 객체(Host object)는 브라우저 환경에서 제공하는 window, XmlHttpRequest, HTMLElement 등의 DOM 노드 객체와 같이 **호스트 환경에 정의된 객체**를 말한다. 예를 들어 브라우저에서 동작하는 환경과 브라우저 외부에서 동작하는 환경의 자바스크립트(Node.js)는 다른 호스트 객체를 사용할 수 있다.
- 브라우저에서 동작하는 환경의 호스트 객체는 전역 객체인 **window**, **BOM(Browser Object Model)** 과 **DOM(Document Object Model)** 및 XMLHttpRequest 객체 등을 제공한다.

## 3. 사용자 정의 객체

- 사용자 정의 객체(User-defined object)는 말 그대로 코드에서 사용자가 정의한 객체를 말한다.

```js
const obj1 = {
  name: "Shin",
  sayHi: function () {
    console.log("Hello " + this.name);
  },
};

obj1.sayHi(); // Hello Shin
```

- 위 코드에서 `obj1`는 사용자 정의 객체이다.
