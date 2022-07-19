# vue slick (scoped) style not working

## case (사례)

vue-slick으로 슬라이드를 만들고 pagination, next prev arrow의 디자인을 커스터마이징 하려 할 때 css가 적용되지 않음

## cause (원인)

vue-slick으로 만들어진 slide DOM에는 vue scoped style의 적용 원리인 `data-v-123a456`같은 속성이 추가가 안돼있음, 따라서 scoped style이 적용이 안됨

## solution (해결책)

SFC에서 scoped style 태그를 사용하지 않고 style 태그를 이용해 slick slide css 커스터마이징 진행하니 css가 정상적으로 적용됨

> ps. scoped가 아니어도 컴포넌트 최상위 Element에 고유한 id 값을 지정해 scoped style 처럼 구현하는게 좋다. - 스타일 충돌 방지

## slick slide에 css 적용할 때 주의할 점

vue에서는 주로 SFC(Single File Component) 방식으로 컴포넌트를 작성한다.
여기서 스타일을 적용하는 경우도 각 컴포넌트간 간섭을 주지 않기 위해 **scoped style**로 작성을한다.

**scoped style**의 작동 원리는 컴포넌트에 고유 속성값(ex - data-v-123a456)을 주고 셀렉터에 속성값을 추가해 스타일의 범위를 제한하는 것이다.
예를 들어 아래와 같이 css 범위를 지정하게 되면

```vue
<!-- title.vue -->
<template>
  <h1 class="title">Hello</h1>
</template>
<style scoped>
.title {
  font-size: 24px
  color: red;
}
</style>
```

아래와 같이 고유 속성이 붙으며, css에도 속성값을 기준으로 스타일을 적용하도록 변경된다.

```html
<!-- rendered DOM -->
<h1 class="title" data-v-123a456>Hello</h1>
<!-- scoped css -->
<style>
  .title[data-v-123a456] {
    font-size: 24px
    color: red;
  }
</style>
```

여기까지 vue scoped style에 대한 설명이었고

slick에 스타일을 적용할 때 scoped style이 적용이 안되는데, 이유는 slick으로 생성된 slide는 vue의 `data-v-123a456`같은 고유 속성이 적용되지 않기 때문이다.
따라서 다른 **일반 style 태그**를 열어 전역적으로 적용하되, 컴포넌트의 최상위 엘리먼트에 id값을 줘 scoped style처럼 구현하면 된다.
scoped style처럼 구현하는 이유는 다른 컴포넌트에서 slick 커스터마이징을 하는 경우 스타일 충돌이 일어나지 않게 하기 위함이다.

## 참고 자료

- 2시간 동안의 삽질과 구글 크롬 검사도구
