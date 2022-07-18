# 변수 (Variable)

## Table of Contents

- [변수 (Variable)](#변수-variable)
  - [Table of Contents](#table-of-contents)
  - [타입](#타입)
    - [원시 타입 (Primitive Data Type)](#원시-타입-primitive-data-type)
      - [number](#number)
      - [string](#string)
      - [boolean](#boolean)
      - [undefined](#undefined)
      - [null](#null)
      - [symbol](#symbol)
    - [객체 타입 (Object type, Reference type)](#객체-타입-object-type-reference-type)
  - [선언](#선언)
    - [ES6 전후 비교](#es6-전후-비교)
      - [var lifecycle](#var-lifecycle)
      - [let lifecycle](#let-lifecycle)
  - [스코프](#스코프)
    - [전역변수](#전역변수)
    - [지역변수](#지역변수)
  - [참고 자료](#참고-자료)

## 타입

데이터 타입(Data Type)은 프로그래밍 언어에서 사용할 수 있는 데이터(숫자, 문자열, 불리언 등)의 종류를 말한다.

자바스크립트의 모든 값은 데이터 타입을 갖는다. ECMAScript 표준(ES6)은 7개의 데이터 타입을 제공한다.

- 원시 타입 (primitive data type)
  - boolean
  - null
  - undefined
  - number
  - string
  - symbol
- 객체 타입 (object / reference type)
  - object

### 원시 타입 (Primitive Data Type)

원시 타입의 값은 변경 불가능한 값(immutable value)이며 pass-by-value(값에 의한 전달)이다.

#### number

숫자(number) 타입은 모든 숫자 데이터를 나타내는데 사용한다.
C, Java언어의 경우는 정수(int)와 실수(float)를 구분하지만, 자바스크립트는 독특하게 하나의 숫자 타입만 존재한다. 자바스크립트는 하나의 숫자 타입만 존재하므로 모든 숫자 값은 실수로 처리한다.

```js
var integer = 10; // 정수
var double = 10.12; // 실수
var negative = -20; // 음의 정수
var binary = 0b01000001; // 2진수
var octal = 0o101; // 8진수
var hex = 0x41; // 16진수
console.log(interger, double, negative); // 10, 10.12, -20
console.log(binary, octal, hex); // 65, 65, 65

// typeof 연산자는 타입을 나타내는 문자열을 반환한다.
console.log(typeof integer, typeof binary); // number number
```

추가적으로 3가지 특별한 값들도 표현할 수 있다.

- `Infinity`: 양의 무한대
- `-Infinity`: 음의 무한대
- `NaN`: 산술 연산 불가(not-a-number)

```js
var pInf = 10 / 0; // 양의 무한대
console.log(pInf); // Infinity

var nInf = 10 / -0; // 음의 무한대
console.log(nInf); // -Infinity

var nan = 1 * "string"; // 산술 연산 불가
console.log(nan); // NaN
```

#### string

문자열(string) 타입은 텍스트 데이터를 나타내는데 사용한다.
문자열은 작은 따옴표('')또는 큰 따옴표("")안에 텍스트를 넣어 생성한다. 추가적으로 ES6문법인 백틱(``)표현도 문자열을 생성한다.

```js
var str = "string"; // 큰 따옴표
str = "string"; // 작은 따옴표
str = `string`; // 백틱(ES6 템플릿 리터럴)

str = "큰 따옴표 안의 '작은 따옴표'는 문자열이다.";
str = '작은 따옴표 안의 "큰 따옴표"는 문자열이다.';

console.log(typeof str); // string
```

#### boolean

불리언(boolean) 타입의 값은 논리적 참, 거짓을 나타내는 `true`와 `false` 뿐이다.

```js
var foo = true;
var bar = false;

console.log(typeof foo, typeof bar); // boolean boolean
```

불리언 타입의 값은 참과 거짓을 구분해 조건에 의해 프로그램 로직을 제어하는 조건문에서 자주 사용한다.
비어있는 문자열과 `null`, `undefined`, 숫자 0은 `false`로 간주된다.

#### undefined

undefined 타입의 값은 `undefined`가 유일하다. 선언 이후 값을 할당하지 않은 변수는 `undefined`값을 갖는다. 즉, 선언은 했지만 값을 할당하지 않은 변수에 접근하거나 존재하지 않는 객체 프로퍼티에 접근할 경우 undefined가 반환된다.

```js
var foo;
console.log(foo); // undefined
```

값의 의미처럼 말 그대로 정의되지 않은 값이라는것을 개발자가 알 수 있다. 그러면 개발자가 의도적으로 값이 아직 정의되지 않았다고 하고싶은 경우가 있을 경우가 있다면 `undefined` 대신 `null`을 할당해야 한다.

#### null

null 타입의 값은 `null`이 유일하다. 자바스크립트는 대소문자를 구별하므로 `null`은 Null, NULL등과 다르다.
프로그래밍 언어에서 `null`은 의도적으로 변수에 값이 없다는 것을 명시할 때 사용한다. 이는 변수가 기억하는 메모리 주소의 참조 정보를 제거하는 것을 의미하며 가비지 컬렉션이 수행된다.

```js
var foo = "Lee";
foo = null; // 참조 정보가 제거됨
```

또는 함수가 호출됐으나 유효한 값을 반환할 수 없을 때 명시적으로 `null`을 반환하기도 한다. 예를 들어 DOM을 선택하는 `document.querySelector()`를 호출했을 때 조건에 부합하는 HTML 요소를 검색할 수 없는 경우, `null`을 반환한다.

```js
var elem = document.querySelector(".myElem");
// HTML 문서에 myElem 클래스를 갖는 요소가 없다면 null을 반환한다.
console.log(elem); // null
```

타임을 나타내는 문자열을 반환하는 `typeof` 연산자로 null 값을 연산하면 `null`이 아닌 `object`가 나오는데, 이는 자바스크립트 설계의 오류다.

```js
var foo = null;
console.log(typeof foo); // object
```

따라서 null 타입을 확인하기 위해서는 typeof 연산자를 사용하는것이 아니라 일치 연산자(===)를 사용해야 한다.

```js
var foo = null;
console.log(typeof foo === null); // false
console.log(foo === null); // true
```

#### symbol

심볼(Symbol)은 ES6에서 새롭게 추가된 7번째 타입으로 변경 불가능한 원시 타입의 값이다. 심볼은 주로 이름의 충돌 위험이 없는 유일한 객체 프로퍼티 키(property key)를 만들기 위해 사용한다. 심볼은 Symnbol 함수를 호출해 생성한다. 이때 생성된 심볼 값은 다른 심볼 값들과 다른 유일한 심볼 값이다.

### 객체 타입 (Object type, Reference type)

객체는 데이터와 그 데이터에 관련한 동작(절차, 방법)을 모두 포함할 수 있는 개념적 존재이다. 객체는 이름과 값을 가지는 데이터를 의미하는 **프로퍼티(property)**와 동작을 의미하는 **메소드(method)**를 포함할 수 있는 독립적 주체이다.

자바스크립트는 객체(object) 기반의 스크립트 언어로서 자바스크립트를 이루고 있는 거의 "모든 것"이 객체이다. 원시 타입(Primitive)를 제외한 나머지 값들(배열, 함수, 정규표현식)은 모두 객체이다. 또한 객체는 pass-by-reference(참조에 의한 전달)방식으로 전달된다.

## 선언

자바스크립트는 기존에 `var`라는 키워드로 변수를 선언했는데, ES6 이후 `let`, `const` 키워드가 나타났다.

### ES6 전후 비교

변수 선언 키워드를 크게 ES6이전, 이후로 비교한 표는 아래와 같다.
||ES6이전 | ES6이후|
|---|---|---|
|키워드|var|let, const|
|스코프|Function Level|Block Level|
|초기화 시점|선언과 동시에|선언 이후|

#### var lifecycle

![var-lifecycle](./img/var-lifecycle.png)

#### let lifecycle

![let-lifecycle](./img/let-lifecycle.png)
초기화 시점이 중요한 이유는 변수 호이스팅(Hoisting)과 연관돼있는 개념이기 때문인데, 결론은 `var`, `let` 모두 변수 호이스팅이 일어난다.

하지만 변수 선언과 초기화 시점이 같은 `var` 키워드는 프로그래밍 흐름에서 선언 및 초기화 전에 호출해도 에러가 발생하지 않고 undefined로 값으로 호출되는 반면, `let` 키워드는 초기화 전에 호출하게되면 초기화 전에 호출 했다고 Reference Error가 발생한다.

## 스코프

스코프는 변수의 활동 범위를 지정하는 개념인데, 변수 선언 키워드에 따라 스코프가 달라진다.
`var`키워드는 함수 레벨 스코프(Function level scope), `let`, `const` 키워드는 블록 레벨 스코프(Block level scope)를 갖는다.

- 함수 레벨 스코프

> 함수 내에서 선언된 변수는 함수 내에서만 유효하며 함수 외부에서는 참조할 수 없다. 즉, 함수 내부에서 선언한 변수는 지역 변수이며 함수 외부에서 선언한 변수는 모두 전역 변수이다.

- 블록 레벨 스코프

> 모든 코드 블록(함수, if문, for문, while문, try/catch문 등) 내에서 선언된 변수는 코드 블록 내에서만 유효하며 코드 블록 외부에서는 참조할 수 없다. 즉, 코드 블록 내부에서 선언한 변수는 지역 변수이다.

### 전역변수

어디에서든 참조할 수 있는 변수이다.

### 지역변수

변수가 속한 지역에서만 참조할 수 있는 변수이다.

## 참고 자료

- [poiemaweb - data type, variable](https://poiemaweb.com/js-data-type-variable)
