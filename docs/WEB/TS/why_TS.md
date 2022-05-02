# TypeScript를 사용하는 이유

## 타입 안정성

더 나은 개발자 경험, 적은 버그, 적은 런타임 에러, 생상선 증대

ex) 자바스크립트의 타입에대한 관대함 (단점)

```js
// 1. 암묵적 타입 변환
const ex1 = [1, 2, 3, 4] + false; // array + boolean
console.log(ex1); // '1,2,3,4false' - string

// 2. 함수 매개변수 타입 관대, 전달되지 않은 경우 undefined로 변경
function divide(a, b) {
  // 매개변수로 숫자(number)타입 두 개를 받기 원함
  return a / b;
}
divide(2, 3); // 0.66666666
divide("xxxxx"); // NaN ('xxxxx'/undefined)

// 3. 런타임 에러
const shin = { name: "shin" };
shin.hello(); // 에러 발생 TypeError: shin.hello is not a function, not undefined가 아닌 not a function이라고 나타남(런타임 에러)
```

타입스크립트에선 암묵적 타입 변환, 함수 매개변수 에러, 런타임 에러가 발생하지 않도록 알려줌
