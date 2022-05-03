# 타입 주석 (type annotation)

## 타입 주석

```
let 변수이름: 타입 [= 초깃값]
const 변수이름: 타입 = 초깃값
```

```ts
let n: number = 1;
let s: string = "hello";
let b: boolean = true; // or false
let o: object = {};
let a: any = 1; // any 타입은 number, string, boolean, object, undefined등 모든 타입이 허용된다. 자바스크립트의 변수선언과 동일하게 작동
let u: undefined = undefined;
u = 1; // Type '1' is not assigned to type 'undefined' 오류 발생

// array
let nArr: number[] = [1, 2, 3]; // let nArr = [1, 2, 3] 타입 추론
let sArr: string[] = ["li", "ul"]; // let sArr = ['li', 'ul'] 타입 추론
let bArr: boolean[] = [true]; // let bArr = [true] 타입 추론

// object - optional type
// player 객체는 string타입 name을 가지고 있으며, number타입 age는 있어도 되고 없어도 된다.
const player: {
  name: string;
  age?: number;
} = {
  name: "shin",
};

console.log(player.age); // undefined

// typa alias - object 타입 선언
type Player = {
  name: string;
  age?: number;
};
const playerShin: Player = {
  name: "shin",
};

const playerLynn: Player = {
  name: "lynn",
  age: 12,
};

// function arguments, return type
function playerMaker(name: string): Player {
  return {
    name,
  };
}
/* or
function playerMaker(name:string): {
  name: string;
  age?: number;
} {
    return {
        name
    }
}
*/
const shin = playerMaker("shin");
shin.age = 12;

// arrow function arguments, return type
const playerMaker2 = (name: string): Player => {
  return {
    name,
  };
};
const lynn = playerMaker2("lynn");
lynn.age = 20;

// readonly - 읽기 전용 타입 (값 변경 방지)
type Person2 = {
  readonly name: string;
  age?: 12;
};

const playerMaker3 = (name: string): Player2 => {
  return {
    name,
  };
};
const shin2 = palyerMaker3("shin");
shin2.age = 24;
// shin2.name = 'lynn' // Cannot assign to 'name' because it is a read-only property.

const numbers: readonly number[] = [1, 2, 3, 4];
// numbers.push() // Property 'push' does not exist on type 'readonly number[]'.
// numbers.pop() // push와 똑같이 배열의 값을 변경시키는 함수이기 때문에 사용할 수 없다.
const newNumbers = numbers.map((i) => {
  // map함수는 값자체를 변경시키는 것이 아니라 변경된 값을 반환하기 때문에 readonly 배열에서도 사용 가능하다.
  console.log(i * 2); // 2, 4, 6, 8
  return i * 2;
});
console.log(numbers, newNumbers); // [1, 2, 3, 4], [2, 4, 6, 8]
```

### 튜플

Tuple은 array를 생성할 수 있게 한다,
최소한의 길이를 만족해야 하며,
특정 위치에 특정 타입이 존재해야 한다.

```ts
const player: [string, number, boolean] = ["shin", 12, false];
```

### unknown

값의 타입을 모르는 경우 사용하며, 조건문으로 타입 체크를 한 뒤에 사용하도록 할 수 있다.

```ts
let a: unknown;

// a + 1; // error
if (typeof a === "number") {
  let b = a + 1;
}
// a.toUpperCase(); // error
if (typeof a === "string") {
  let b = a.toUpperCase();
}
```

### void

함수의 반환 타입으로 아무 것도 반환하지 않을 때 사용한다.

```ts
function hello(): void {
  // : void를 생략해도 반환(return)이 없는 함수의 경우 타입스크립트는 해당 함수 반환 타입을 void로 추론한다.
  console.log("hello");
}
const a = hello();
// a.toUpperCase() // Property 'toUpperCase' does not exist on type 'void'.
```

### never

함수가 절대 반환하지 않을 때 사용, 타입이 여러 개인데 올바른 타입이 들어오지 않은 경우 사용

```ts
// 1. 에러 발생 시 사용
function hello2(): never {
  throw new Error("XXX");
}

// 2. 타입이 두 개일 경우
function hello3(name: string | number) {
  if (typeof name === "string") {
    name; // name: string
  } else if (typeof name === "number") {
    name; // name: number
  } else {
    // 타입이 잘못 들어온 경우이기 때문에 실행되면 안되는 부분이다.
    name; // name: never
  }
}
```

### 타입스크립트 타입 계층도

![ts 계층도](./img/img1.png)

## 객체와 인터페이스

인터페이스는 객체의 타입을 정의한다.

```
interface 인터페이스 이름 {
  속성이름[?]: 속성타입[,...]
}
```

인터페이스 속성들을 여러 줄로 표현할 때는 쉼표(,)대신 세미콜론(;)을 구분자로 쓰거나 단순히 줄바꿈을 해도 된다.

```
interface Iperson {
  name: string
  age: number
}

let good: Iperson = {name: 'Shin', age: 24}

let bad1: Iperson = {name: 'Shin'} // age 속성이 없으므로 오류
let bad2: Iperson = {age: 24} // name 속성이 없으므로 오류
let bad3: Iperson = {} // name과 age 속성이 없으므로 오류
let bad4: Iperson = {name: 'Shin', age: 24, etc: true} // etc속성이 있으므로 오류
let bad4: Iperson = {name: 25, age: 'Shin'} // name과 age에 타입이 잘못돼서 오류
```

### 선택 속성 구문

인터페이스 설계 시 있어도 되고 없어도 되는 속성은 **선택 속성**(optional property)으로 만들면 된다.
선택 속성은 속성 이름 뒤에 물음표 기호를 붙여서 만든다.

```
interface Iperson2 {
  name: string
  age: number
  etc?: boolean
}
```

### 익명 인터페이스

interface 키워드와 이름을 생략하고 인터페이스를 만들 수 있습니다.

```
let ai: {
  name: string
  age: number
  etc?: boolean
} = {name: 'Shin', age: 24}
```

또한 익명 인터페이스는 주로 함수를 구현할 때 사용된다.

```
function printMe(me: {name: string, age: number, etc?: boolean}) {
  console.log(
    me.etc ?
      `${me.name} ${me.age} ${me.etc} :
      `${me.name} ${me.age}
  )
}
printMe(ai) // Shin 24
```

자바스크립트에서 함수와 익명 함수를 같이 사용하는 것 처럼 상황에 따라 인터페이스를 선언하거나, 익명 인터페이스를 사용하면 된다.
