# vue

## vue composition api

### `<script setup>`

`<script></script>`같은 일반적인 script 태그의 경우는 컴포넌트가 처음 import될 때 한번 실행된다.
반면 `<script setup></script>`는 컴포넌트 인스턴스가 생성될 때마다 실행된다.

`<script setup></script>`태그는 모듈을 포함할 수 없다.(`<script setup>` cannot contain ES module)

### 반응형 기초

#### reactive()를 사용한 반응형

reactive() 함수를 사용하여 **객체 또는 배열을 반응형**으로 만들 수 있다.

```js
import { reactive } from "vue";

const state = reactive({ count: 0 });
```

reactive() API는 두 개의 제한 사항이 있다.

객체, 배열 그리고 Map이나 Set과 같은 컬렉션 유형에만 작동합니다. string, number 또는 boolean과 같은 기본 유형에 사용할 수 없다.

Vue의 반응형 변경 감지는 속성에 접근함으로써 작동하므로, 항상 반응형 객체에 대한 동일한 참조를 유지해야 합니다. 즉, 첫 번째 참조에 대한 반응형 연결이 손실되기 때문에 반응형 객체를 쉽게 "교체"할 수 없음을 의미한다.

#### ref()를 사용한 반응형

Vue는 reactive()의 제한 사항을 해결하기 위해, 어떠한 유형의 데이터라도 반응형으로 재정의할 수 있는 ref() 함수를 제공한다.

```js
import { ref } from "vue";

const count = ref(0);
```

ref는 받은 인수를 .value 속성을 포함하는 ref객체에 래핑 후 반환한다.
따라서 값에 접근하려면 .value로 접근해야한다.

```js
console.log(count); // {value: 0}
console.log(count.value); // 0
count.value++;
console.log(count.value); // 1
```

#### reactive()와 ref()의 차이점

reactive는 기존 뷰 문법의 data 속성 느낌이고, ref는 좀 더 리액티브 속성을 개별적으로 선언하는 느낌이다.
reactive는 `객체.값`으로 접근 가능하고 ref는 `값.value`로 접근 가능하다.

```js
// reactive
const event = reactive({
  count: 3,
  doubled: computed(() => event.count * 2),
});

// ref
const count = ref(3);
const doubled = computed(() => count.value * 2);
```

참고

- [https://joshua1988.github.io/vue-camp/vue3.html#reactive%E1%84%8B%E1%85%AA-ref%E1%84%8B%E1%85%B4-%E1%84%8E%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%A5%E1%86%B7](https://joshua1988.github.io/vue-camp/vue3.html#reactive%E1%84%8B%E1%85%AA-ref%E1%84%8B%E1%85%B4-%E1%84%8E%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%A5%E1%86%B7)

### 속성 바인딩

#### `v-bind`

`v-bind`디렉티브를 이용해서 속성 바인딩을 할 수 있다.
`v-bind:속성명=속성값"`으로 속성을 바인딩하며 바인딩 할 때는 동적 값을 `{{속성값}}`이 아닌 `"속성값"`으로 바인딩한다. 축약형은 `:속성명="속성값"`으로 똑같이 바인딩 할 수 있다.
속성에 동적 값을 바인딩하는것이 아닌 정적 값을 넣고 싶은 경우는 `속성명="속성값"`으로 기존과 동일하게 적용 가능하다.

> 이후 부모 컴포넌트에서 자식 컴포넌트로 props를 전달할 때도 `v-bind`디렉티브를 이용해 동적 값을 전달할 수 있다.

```vue
<script setup>
import { ref } from "vue";
const titleId = ref("title");
</script>
<template>
  <div v-bind:id="dynamicID" class="a">글자가 빨간 색이 됩니다.</div>
</template>
<style>
#title {
  color: red;
}
.a {
  background-color: blue;
}
</style>
```

### 이벤트 리스너

#### `v-on`

`v-on`디렉티브를 사용해서 DOM 이벤트틑 수신할 수 있다.
`v-bind`디렉티브와 동일하게 `v-on:이벤트명="함수명"`로 이벤트를 바인딩할 수 있으며, 축약형은 `@:이벤트명="함수명"`으로 똑같이 바인딩 할 수 있다.

> 이후 자식 컴포넌트의 emit으로 전달한 이벤트를 부모 컴포넌트에서 `v-on`디렉티브를 이용해 이벤트를 전달받을 수 있다.

```vue
<script setup>
import { ref } from "vue";

const count = ref(0);
const increment = () => {
  count.value++;
};
</script>

<template>
  <button v-on:click="increment">숫자 세기: {{ count }}</button>
</template>
```

### 폼(form) 바인딩

#### `v-bind`와 `v-on`

`v-bind`와 `v-on`디렉티브를 함께사용해서 폼 안의 입력 엘리먼트에 양방향 바인딩을 구현할 수 있다.

```vue
<script setup>
import { ref } from "vue";

const text = ref("");

function onInput(e) {
  text.value = e.target.value;
}
</script>

<template>
  <input :value="text" @input="onInput" placeholder="여기에 입력하기" />
  <p>{{ text }}</p>
</template>
```

#### `v-model`

vue는 이런 양방향 바인드를 단순화하기 위해, 위 문법을 간편하게 표기하는 `v-model`디렉티브를 제공한다.

```vue
<script setup>
import { ref } from "vue";

const text = ref("");
</script>

<template>
  <input v-model="text" placeholder="여기에 입력하기" />
  <p>{{ text }}</p>
</template>
```

v-model은 텍스트 입력 외에도 체크박스, 라디오 버튼, 셀렉트 드롭다운과 같은 다른 입력 타입에서도 작동한다. 따라서 `v-bind`, `v-on`으로 양방향 바인딩하는것보다 `v-model`을 이용하도록 하자.

### 조건부 렌더링

#### `v-if`와 `v-else`

vue에서는 조건부 렌더링을 위해 `v-if`디렉티브를 제공한다.
사용법으로 `v-if="boolean value"`에서 `boolean value"`가 참인 경우만 해당 앨리먼트가 렌더링 된다. `v-else`디렉티브는 `v-if="boolean value"`가 거짓인 경우 렌더링 된다.
여기서 중요한 점은 `boolean value`값이 `truthy`인 경우만 렌더링 되며, `falsy`값으로 변경되면 DOM에서 제거된다.

```vue
<script setup>
import { ref } from "vue";

const awesome = ref(true);

function toggle() {
  awesome.value = !awesome.value;
}
</script>

<template>
  <button @click="toggle">토글 버튼</button>
  <!-- h1은 awesome값이 truthy인 경우만 렌더링 되며, falsy값으로 변경되면 DOM에서 제거된다. -->
  <h1 v-if="awesome">Vue는 굉장해! 엄청나!</h1>
  <h1 v-else>오 안돼 😢</h1>
</template>
```

#### `v-else-if`

`v-else-if`디렉티브도 존재하는데, 이건 js에서 else if의 개념과 비슷하다.

```vue
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  A/B/C 아님
</div>
```

#### `v-show`

`v-show`디렉티브도 엘리먼트를 조건부로 표시하는 방법 중 하나이며 참인 경우 보여주고, 거짓인 경우 보여주지 않는다. `v-show`디렉티브를 사용한 엘리먼트는 조건에 상관없이 항상 렌더링되고 DOM에 남아있다. 즉, `v-show`는 엘리먼트를 렌더링 해놓고 `display`css 속성만 전환한다.

`v-if` vs `v-show`

> 엘리먼트를 매우 자주 전환해야 하는 경우 v-show를 사용하는 것이 좋고
> 실행 중에 조건이 변경되지 않는 경우 v-if를 사용하는 것이 좋다.

#### `v-if` with `v-for`

`v-if`와 `v-for`를 함께 사용되는것은 권장되지 않는다. `v-if` vs `v-for`를 함께 사용하면 `v-if`가 먼저 평가된다.

### 리스트 렌더링

#### `v-for`

`v-for`디렉티브를 사용해서 배열이나 객체을 엘리먼트 리스트로 렌더링할 수 있다.

```vue
<script setup>
import { ref } from "vue";

// 각 할 일에 고유한 ID 부여
let id = 0;

const todos = ref([
  { id: id++, text: "HTML 배우기" },
  { id: id++, text: "JavaScript 배우기" },
  { id: id++, text: "Vue 배우기" },
]);
</script>

<template>
  <ul>
    ****
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.text }}
      <button>X</button>
    </li>
  </ul>
</template>
```

### 계산된 속성(computed)

템플릿 내 표현식`{{표현식}}`은 매우 편하지만 간단한 작업만을 위한 것이다.
템플릿에 너무 많은 논리를

```vue
<script setup>
import { ref, computed } from "vue";
const message = ref("hello vue!");
const reversedMessage = computed(() => {
  return message.value.split("").reverse().join("");
});
// 컴포넌트 로직
</script>

<template>
  <h1>original message: {{ message.split("").reverse().join("") }}</h1>
  <h1>computed message: {{ reversedMessage }}</h1>
  <h1>
    expression method message:
    {{
      (() => {
        return message.split("").reverse().join("");
      })()
    }}
  </h1>
</template>
```

위 코드에서 모든 h1태그에 `message.split("").reverse().join("")`과 `computedMessage`, 익명함수는 동일하게 렌더링된다.

### 생명주기와 템플릿 참조

아래는 vue의 instance가 생성될 때 진행되는 생명주기이다.
기본적인 흐름으로 `Create => Mount => Update => Unmount` 순서로 진행되며 각각 이전(ex] beforeOnMount)과 이후(ex] onMounted)가 존재한다.
![lifecycle](https://v3-docs.vuejs-korea.org/assets/lifecycle.c92cb034.png)

```vue
<script setup>
import { ref, onMounted } from "vue";

const p = ref(null);
onMounted(() => {
  p.value.innerText = "1234";
});
</script>

<template>
  <p ref="p">안녕</p>
</template>
```

#### 참고

- [https://v3-docs.vuejs-korea.org/guide/essentials/lifecycle.html#lifecycle-diagram](https://v3-docs.vuejs-korea.org/guide/essentials/lifecycle.html#lifecycle-diagram)
- [https://v3-docs.vuejs-korea.org/api/composition-api-lifecycle.html](https://v3-docs.vuejs-korea.org/api/composition-api-lifecycle.html)

### 감시자(watch)

vue에서 `watch(데이터, 콜백함수)`함수는 해당 데이터가 변경됐을 때 전달된 콜백함수를 실행하도록 한다.
react의 `useEffet(콜백함수, 데이터)`훅과 비슷한 동작을 한다.

```vue
<script setup>
import { ref, watch } from "vue";

const todoId = ref(1);
const todoData = ref(null);

async function fetchData() {
  todoData.value = null;
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/todos/${todoId.value}`
  );
  todoData.value = await res.json();
}

fetchData();
watch(todoId, fetchData);
</script>

<template>
  <p>할 일 id: {{ todoId }}</p>
  <button @click="todoId++">다음 할 일 가져오기</button>
  <p v-if="!todoData">로딩...</p>
  <pre v-else>{{ todoData }}</pre>
</template>
```

#### 참고

- [https://v3-docs.vuejs-korea.org/guide/essentials/watchers.html](https://v3-docs.vuejs-korea.org/guide/essentials/watchers.html)
- [https://imagineu.tistory.com/74](https://imagineu.tistory.com/74)

### 컴포넌트(component)

컴포넌트란 조합하여 화면을 구성할 수 있는 블록을 의미한다. 컴포넌트를 활용하면 중복되는 코드를 줄일 수 있고 화면을 구조화해 일괄적인 패턴으로 개발할 수 있다. 즉, 코드를 쉽게 이해하고 재사용할 수 있다.

```vue
<!-- App.vue -->
<script setup>
import ChildComp from "./ChildComp.vue";
</script>

<template>
  <ChildComp />
</template>
```

```vue
<!-- ChildComp.vue -->
<template>
  <h2>자식 컴포넌트입니다!</h2>
</template>
```

#### 참고

- [https://v3-docs.vuejs-korea.org/guide/essentials/component-basics.html](https://v3-docs.vuejs-korea.org/guide/essentials/component-basics.html)
- [https://velog.io/@sms8377/Javascript-Vue-%EC%97%90%EC%84%9C-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EB%9E%80](https://velog.io/@sms8377/Javascript-Vue-%EC%97%90%EC%84%9C-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EB%9E%80)

### Props

자식 컴포넌트는 props를 통해 부모로부터 데이터를 받는다. 그리고 props를 받기 위해서는 `defineProps()`를 이용해 props를 선언해야 한다. props를 선언할 때 타입스크립트의 인터페이스처럼 받을 prop의 이름과 타입을 정해줘야 한다.

참고로 `defineProps()`는 컴파일 타임 매크로이므로 import할 필요가 없다.

부모는 props를 전달할 때 속성을 사용하는 것 처럼 propr을 전달할 수 있는데, 동적 값을 전달하기 위해 `v-bind`문법을 사용할 수도 있다.

```vue
<!-- App.vue -->
<script setup>
const greeting = "부모 컴포넌트가 전달한 msg입니다.";
</script>
<template>
  <ChildComp :msg="greeting" staticMsg="정적 값을 전달하는 메시지입니다." />
</template>
```

```vue
<!-- ChildComp.vue -->
<script setup>
const props = defineProps({
  msg: String,
  staticMsg: String,
});
</script>
<template>
  <h2>{{ msg || "prop이 아직 전달되지 않았습니다." }}</h2>
  <h3>{{ staticMsg }}</h3>
</template>
```

### Emits

자식 컴포넌트는 부모로부터 props를 받는것 뿐만 아니라 이벤트를 emit(발송)할 수 있다.

자식 컴포넌트에서 `defineEmits([이벤트명1, 이벤트명2, ...])`를 이용해 이벤트를 생성한다. 생성한 이벤트는 `defineEmits()`가 반환된 객체가 만약 `emit`이라고 한다면 `emit('이벤트명', '보낼 메세지')`로 이벤트와 함께 메세지를 전달할 수 있다.

아래는 emit을 활용한 간단한 예제이다.

```vue
<script setup>
import { ref } from "vue";
import ChildComp from "./ChildComp.vue";

const childMsg = ref("자식 컴포넌트로부터 아직 메시지를 받지 못했어요!");
</script>

<template>
  <ChildComp @response="(msg) => (childMsg = msg)" />
  <p>{{ childMsg }}</p>
</template>
```

```vue
<script setup>
const emit = defineEmits(["response"]);

emit("response", "자식 컴포넌트로부터 🌷를 받았어요!");
</script>

<template>
  <h2>자식 컴포넌트</h2>
</template>
```

## 참고 자료

- [vuejs tutorial - https://v3-docs.vuejs-korea.org/tutorial](https://v3-docs.vuejs-korea.org/tutorial)
- [vuejs docs - https://v3-docs.vuejs-korea.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive](https://v3-docs.vuejs-korea.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive)
