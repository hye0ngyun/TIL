# 객체와 클래스

## 클래스 선언문

```ts
class 클래스 이름 {
  [private | protected | public] 속성 이름[?]: 속성 타입[...]
}
```

```ts
class Person1 {
  name: string;
  age?: number;
}

let shin1: Person1 = new Person1();
shin1.name = "Shin";
shin1.age = 24;
console.log(shin1); // Person1 {name: 'Shin', age: 24}
```

## 접근 제한자

클래스의 속성은 public, private, protected가 존재하고 속성 앞에 붙일 수 있다. 접근제한자를 생략할 경우 public으로 간주한다.

## 생성자

```ts
class Person2 {
  constructor(public name: string, public age?: number) {}
}
let shin2: Person2 = new Person2("Shin", 24);
console.log(shin2); // Person2 {name: 'Shin', age:24 }
```

타입스크립트의 생성자의 매개변수에 public과 같은 접근 제한자를 붙이면 해당 매개변수의 이름을 가진 속성이 클래스에 선언된 것처럼 동작한다. Person2는 다음 Person3을 함축해서 구현한 것이다.

```ts
class Person3 {
  name: string;
  age?: number;
  constructor(name: string, age?: number) {
    this.name = name;
    this.age = age;
  }
}
let shin3: Person3 = new Person3("Shin", 24);
console.log(shin3); // Person3 {name: 'Shin', age:24 }
```

## 인터페이스 구현

```
class 클래스 이름 implements 인터페이스 이름 {
  ...
}
```

인터페이스는 이러이러한 속성이 있어야 한다는 규약(spec)에 불과할 뿐 물리적으로 해당 속성을 만들지는 않는다. 따라서 클래스 몸통에는 반드시 인터페이스가 정의하고 있는 속성을 멤버 속성으로 표시해야 한다.

```ts
interface Iperson4 {
  name: string;
  age?: number;
}

class Person4 implements IPerson4 {
  name: string;
  age: number;
}
```

다음은 Person2 구현방식을 인터페이스 구현에 응용한것이다.

```ts
interface Iperson4 {
  name: string;
  age?: number;
}

class Person4 implements IPerson4 {
  constructor(public name: string, public age?: number) {}
}
let shin4: IPerson4 = new IPerson4("Shin", 24);
console.log(shin4); // Person4 {name: 'Shin', age:24 }
```

## 추상 클래스

타입스크립트는 abstract 키워드를 사용해 추상 클래스를 만들 수 있다.
추상 클래스는 자신의 속성이나 메서드 앞에 abstract를 붙여 나를 상속하는 다른 클래스에서 이 속성이나 메서드를 구현하게 한다.

```ts
abstract class 클래스 이름 {
  abstract 속성 이름: 속성 타입
  abstract 메서드 이름() {}
}
```

다음 Abstract Person5는 name속성 앞에 abstract가 붙었으므로 new 연산자를 통해 객체를 만들 수 없다.

```ts
abstract class AbstractPerson5 {
  abstract name: string;
  constructor(public age?: number) {}
}
```

## 클래스의 상속

extends 키워드를 사용해 상속 클래스를 만든다.

```ts
class 상속 클래스 extends 부모 클래스 { ... }
```

다음 Person5 클래스는 AbstractPerson5 추상 클래스를 상속해 AbstractPerosn5가 구현할 age를 얻고, AbstractPerson5를 상속받은 클래스가 구현해야 할 name 속성을 구현한다. 부모 클래스의 생성자는 super 키워드로 호출할 수 있다.

```ts
class Person5 extends AbstractPerson5 {
  constructor(public name: string, public age?: number) {
    super(age);
  }
}
let shin5: Person5 = new Person5("shin", 24);
console.log(shin5); // Person5 { name: 'shin', age: 24 }
```

## static 속성

static 키워드를 이용해 클래스의 정적인 속성을 정의할 수 있다.

```ts
class 클래스 이름 {
  static 정적 속성 이름: 속성 타입
}
```

다음 코드의 클래스 A는 initValue라는 정적 속성을 가진다. `A.initValue`형태로 정적 속성에 접근이 가능하다.

```ts
class A {
  static initValue = 1;
}

let initVal = A.initValue; // 1
```
