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
console.log(this === global); // true
```

전역 객체는 전역 스코프(Global Scope)를 갖는 전역변수(Global Variable)를 프로퍼티로 소유한다. 글로벌 영역에 선언한 함수는 전역객체의 프로퍼티로 접근할 수 있는 변수의 메소드이다.

```js
var ga = "Global variable";

console.log(ga); // Global variable
console.log(window.ga); // Global variable
console.log(this.ga); // Global variable

function foo() {
  console.log("invoked!");
}
console.log(foo()); // invoked!
console.log(window.foo()); // invoked!
console.log(this.foo()); // invoked!
```

기본적으로 `this`는 전역객체(Global object)에 바인딩된다. 전역함수는 물론이고 심지어 내부함수의 경우도 `this`는 외부함수가 아닌 전역객체에 바인딩된다.

```js
function foo() {
  console.log("foo's this: ", this); // window
  function bar() {
    console.log("bar's this: ", this); // window
  }
  bar();
}
foo();
```

또한 객체의 프로퍼티인 메소드의 내부함수일 경우에도 `this`는 전역객체에 바인딩된다.

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    console.log("foo's this: ", this); // obj
    console.log("foo's this.value: ", this.value); // 100
    function bar() {
      console.log("bar's this: ", this); // window
      console.log("bar's this.value: ", this.value); // 1
    }
    bar();
  },
};
obj.foo();
```

콜백함수의 경우에도 `this`는 전역객체에 바인딩된다.

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    setTimeout(function () {
      console.log("callbacks's this: ", this); // window
      console.log("callbacks's this.value: ", this.value); // 1
    }, 100);
  },
};
obj.foo();
```

**내부함수는 일반 함수, 메소드, 콜백 함수 어디에서 선언되었든 관계없이 tihs는 전역객체를 바인딩한다.** 더글라스 크락포드는 “이것은 설계 단계의 결함으로 메소드가 내부함수를 사용하여 자신의 작업을 돕게 할 수 없다는 것을 의미한다” 라고 말한다. 내부함수의 this가 전역객체를 참조하는 것을 회피방법은 아래와 같다.

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    var that = this; // Workaround : this === obj

    console.log("foo's this: ", this); // obj
    console.log("foo's this.value: ", this.value); // 100
    function bar() {
      console.log("bar's this: ", this); // window
      console.log("bar's this.value: ", this.value); // 1

      console.log("bar's that: ", that); // obj
      console.log("bar's that.value: ", that.value); // 100
    }
    bar();
  },
};

obj.foo();
```

위 방법 이외에도 자바스크립트는 this를 명시적으로 바인딩할 수 있는 apply, call, bind 메소드를 제공한다.

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    console.log("foo's this: ", this); // obj
    console.log("foo's this.value: ", this.value); // 100
    function bar(a, b) {
      console.log("bar's this: ", this); // obj
      console.log("bar's this.value: ", this.value); // 100
      console.log("bar's arguments: ", arguments); // 1, 2
    }
    bar();
    bar.apply(obj, [1, 2]);
    // bar.apply(obj, [1, 2]); === bar.apply(this, [1, 2]);
    bar.call(obj, 1, 2); // ===
    bar.bind(obj)(1, 2); // ===
  },
};

obj.foo();
```

### 2. 메소드 호출

함수가 객체의 프로퍼티 값이면 메소드로서 호출된다. 이때 메소드 내부의 this는 해당 메소드를 소유한 객체, 즉 해당 메소드를 호출한 객체에 바인딩된다.

```js
var obj1 = {
  name: "Lee",
  sayName: function () {
    console.log(this);
    console.log(this.name);
  },
};

var obj2 = {
  name: "Kim",
};
// obj2에 sayName이라는 메소드 프로퍼티 추가
obj2.sayName = obj1.sayName;

obj1.sayName(); // Lee
obj2.sayName(); // Kim
```

프로토타입 객체도 메소드를 가질 수 있다. 프로토타입 객체 메소드 내부에서 사용된 this도 일반 메소드 방식과 마찬가지로 해당 메소드를 호출한 객체에 바인딩된다.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.getName = function () {
  return this.name;
};

var me = new Person("Lee");
console.log(me.getName()); // Lee

Person.prototype.name = "Kim";
console.log(Person.prototype.getName()); // Kim
```
