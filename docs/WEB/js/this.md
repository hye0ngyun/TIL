# 자바스크립트에서의 this

## 함수 호출 방식에 의해 결정되는 this

자바스크립트의 함수는 호출될 때, 매개변수로 전달되는 인자값 이외에, arguments 객체와 this를 암묵적으로 전달받는다.

```js
function square(number) {
  console.log(arguments); // 10, 20, 30
  console.log(this); // window
  return number * number;
}
console.log(square(10, 20, 30)); // 100
```

## 함수 호출 방식과 this 바인딩

자바스크립트의 경우 함수 호출 방식에 의해 this에 바인딜할 어떤 객체가 동적으로 결정된다. 다시 말해 함수를 선언할 때 this에 바인딩 할 객체가 정적으로 결정되는 것이 아닌, **함수를 호출할 때 함수가 어떻게 호출되었는지에 따라** this에 바인딩할 객체가 동적으로 결정된다.

> 함수의 상위 스코프를 결정하는 방식인 **렉시컬 스코프(Lexical scope)는 함수를 선언할 때 결정**된다. this 바인딩과 혼동하지 않도록 주의해야 한다.

함수를 호출하는 방식은 아래와 같이 다양하다.

> 1. 함수 호출
> 2. 메소드 호출
> 3. 생성자 함수 호출
> 4. apply/call/bind 호출

```js
// 1. 함수 호출
var foo = function () {
  console.log(this);
};
foo(); // window

// 2. 메소드 호출
let obj = { foo: foo };
obj.foo(); // obj

// 3. 생성자 함수 호출
let instance = new foo(); // instance

// 4. apply/call/bind 호출
let bar = { name: "bar" };
foo.call(bar); // bar
foo.apply(bar); // bar
foo.bind(bar)(); // bar
```

### 1. 함수 호출

전역객체(Global Object)는 모든 객체의 유일한 최상위 객체를 의미하며 일반적으로 Browser-side에서는 `window`, Server-side(Node.js)에서는 `global` 객체를 의미한다.

```js
// in browser console
console.log(this === window); // true

// in node.js terminal
console.log(this === global) // true
```
