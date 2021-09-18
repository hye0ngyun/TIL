# 호이스팅(Hoisting)
변수 선언문이 코드의 선두로 끌어 올려진 것처럼 동작하는 자바스크립트의 고유의 특징이다.
호이스팅은 끌어올리다 라는 의미이다.
모든 선언문은 호이스팅 된다.

var 키워드의 호이스팅
```js
// 스코프의 선두에서 선언 단계와 초기화 단계가 동시에 실행된다.
// 따라서 변수 선언문 이전에 변수를 참조할 수 있다.
console.log(foo); // undefined
var foo; // 변수 선언문

foo = 1; // 변수 할당문, 할당 단계가 일어난다.
console.log(foo); // 1
```
![var-lifecycle](./img/var-lifecycle.png)

let 키워드의 호이스팅
```js
// 스코프의 선두에서 선언 단계가 실행된다.
// 아직 변수가 초기화(메모리 공간 확보와 undefined로 초기화)되지 않았다.
// 따라서 변수 선언문 이전에 변수를 참조할 수 없다.
console.log(foo); // ReferenceError: foo is not defined

let foo; // 변수 선언문에서 초기화 단계가 실행된다.
console.log(foo); // undefined

foo = 1; // 할당문에서 할당 단계가 실행된다.
console.log(foo); // 1
```
![let-lifecycle](./img/let-lifecycle.png)

let 키워드 호이스팅 2
```js
let foo = 1; // 전역 변수

{
  console.log(foo); // ReferenceError: foo is not defined
  let foo = 2; // 지역 변수
}
```
## 변수 선언 시점
변수 선언은 소스코드가 한 줄씩 순차적으로 실행되는 시점, 즉 런타임(runtime)이 아니라 그 이전 단계에서 실행된다.

변수 선언 3단계
1. 선언 단계(Declaration phase)
변수 객체에 변수를 등록한다. 이 변수 객체는 스코프가 참조하는 대상이 된다.
2. 초기화 단계(Initiallization phase)
변수 객체에 등록된 변수를 메모리에 할당한다. 이 단계에서 변수는 undefined로 초기화된다.
3. 할당 단계(Assignment phase)
undefined로 초기화된 변수에 실제값을 할당한다.

## var vs let vs const
- ES6를 사용한다면 var 키워드는 사용하지 않는다.
- 재할당이 필요한 경우에 한정해 let 키워드를 사용한다. 이때 변수의 스코프는 최대한 좁게 만든다.
- 변경이 발생하지 않는(재할당이 필요 없는 상수) 원시 값과 객체에는 const 키워드를 사용한다. const 키워드는 재할당을 금지하므로 var, let 보다 안전하다.