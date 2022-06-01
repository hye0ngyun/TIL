# ES6 spread(...) operator

스프레드 연산자는 array, map, set, objet와 같이 **반복 가능한 객체**(python의 반복 가능 객체와 비슷한 개념)를 펼칠 수 있게 해준다. 이 기능은 더 적게 쓰고 더 많은 것을 할 수 있게 한다.

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr); // [1,2,3,4,5]
console.log(...arr); // 1 2 3 4 5
```

이후로 7가지 스프레드 연산자 트릭에대해 알아본다.

## 1. 배열의 push()메소드를 사용하는 더 나은 방법

배열에 배열을 삽입하는 경우 apply()메소드를 이용해서 배열을 삽입할 수 있지만 그다지 편한 방법은 아니다.

```js
const arr = [1, 2];
arr.push.apply(arr, [3, 4]);
console.log(arr); // [1,2,3,4]
```

위와 같은 결과를 내는 코드를 스프레드 연산자로 더 간단하게 작성할 수 있다.

```js
const arr = [1, 2];
arr.push(...[3, 4]);
console.log(arr); // [1,2,3,4]
```

## 2. 배열 복사하기

배열 복사하기는 스프레드 연산자의 가장 편리한 기능 중 하나이다.

```js
const arr = [1, 2, 3, 4];
// 스프레드 사용x
const copyArr1 = arr.slice(0);
// 스프레드 사용o
const copyArr2 = [...arr];
// 잘못된 스프레드 사용법
// const copyArr3 = ...arr // SyntaxError: Unexpected token '...'
```

> 참고로 스프레드 연산자로 복사한 중첩 배열은 얕은 복사가 된다. 즉, 복사된 중첩 배열의 요소를 변경하면 원본 배열의 해당 요소도 변경된다.

```js
// 1차원 배열의 요소들은 깊은 복사가 된다.
const arr = [1, 2, 3, 4];
const copyArr = [...arr];
copyArr[2] = 10;
console.log(copyArr, arr); // [1,10,3,4], [1,2,3,4]

// 2차원 배열의 경우 중첩된 배열의 값은 얕은 복사가 되어 복사 값을 변경하면 원본에도 적용된다.
const arr2 = [1, 2, [3, 4]];
const copyArr2 = [...arr2];
copyArr2[0] = 100;
copyArr2[2][0] = 300;
console.log(copyArr2, arr2); // [100,2,[300,4]], [1,2,[300,4]]
```

## 3. 배열에서 중복값 제거하기

배열의 중복값들을 set 데이터 구조와 스프레드 연산자를 이용해 제거할 수 있다.

```js
const arr = [1, 1, 2, 3, 3, 3, 4];
const uniqueArray = [...new Set(arr)];
console.log(uniqueArray); // [1,2,3,4]
```

## 4. 복수 배열 연결하기

스프레드 연산자를 이용해서 여러 배열을 연결시켜 새로운 배열을 만들 수 있다.

```js
const arr1 = [1, 2];
const arr2 = [3, 4];
const arr = [...arr1, ...arr2];
console.log(arr); // [1,2,3,4]
```

## 5. NodeList를 진짜 배열로 변환하기

DOM 조작은 프론트엔드 개발자가 매일 하는 일인데, document.querySelectorAll()함수를 이용해서 NodeList를 얻을 때, 스프레드 연산자를 이용해 NodeList를 일반 배열로 변환시킬 수 있다. 그러면 forEach, map등 배열 함수를 이용할 수 있게 된다.

```js
const elDivs = document.querySelectorAll("div");
const elArrayDivs = [...elDivs];
console.log(Array.isArray(elDivs), Array.isArray(elArrayDivs)); // false, true
```

## 6. 구조 분해 할당

스프레드 연산자는 종종 배열과 객체의 구조 분해 할당에 사용된다.

- 배열의 구조 분해 할당

```js
const [num0, ...others] = [1, 2, 3, 4, 5, 6];
console.log(num0); // 1
console.log(others); // [2,3,4,5,6]
```

- 객체의 구조 분해 할당

```js
const obj = { name: "fatfish", age: 100, luckyNumber: 6 };
const { name, ...others } = obj;
console.log(name); // fatfish
console.log(others); // {age: 100, luckyNumber: 6}
```

## 7. 문자열을 배열로 변환하기

문자열 또한 반복 가능한 객체이므로 스프레드 연산자를 사용해 배열로 변환할 수 있다.

```js
const name = "fatfish";
const nameArray = [...name];
console.log(nameArray); // ['f', 'a', 't', 'f', 'i', 's', 'h']
```

## 참고자료

- [velog [번역] 모든 개발자가 알아야 하는 7가지 ES6 스프레드 연산자 트릭](https://velog.io/@jonghunbok/%EB%B2%88%EC%97%AD-%EB%AA%A8%EB%93%A0-%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%98%EB%8A%94-7%EA%B0%80%EC%A7%80-ES6-%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C-%EC%97%B0%EC%82%B0%EC%9E%90-%ED%8A%B8%EB%A6%AD)
- [javascripttutorial.net/es6/javascript-spread/](javascripttutorial.net/es6/javascript-spread/)
