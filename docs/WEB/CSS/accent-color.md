<style>
  .example {
    border: 1px solid #aaa;
    padding: 1rem;
  }
</style>

# accent-color

CSS `accnet-color` 속성은 UI 컨트롤 요소의 accent(악센트) 색상을 변경할 수 있다. 변경되는 accent 색상에 따라 체크요소나 배경색은 시각적으로 확인하기 적절한 색상으로 변경된다.

브라우저는 `accent-color`속성은 아래와 같은 HTML element에 적용된다.

- `<input type="checkbox">`
- `<input type="radio">`
- `<input type="range">`
- `<progress>`

## 문법

```css
/* Keyword values */
accent-color: auto;

/* <color> values */
accent-color: red;
accent-color: #5729e9;
accent-color: rgb(0, 200, 0);
accent-color: hsl(228, 4%, 24%);

/* Global values */
accent-color: inherit;
accent-color: initial;
accent-color: revert;
accent-color: revert-layer;
accent-color: unset;
```

## 예시

기존 accent-color

```html
<input type="radio" checked />
<input type="checkbox" checked />
<input type="range" />
<progress></progress>
```

<div class="example">
  <input type="radio" checked/>
  <input type="checkbox" checked/>
  <input type="range" />
  <progress></progress>
</div>

속성값을 변경한 accent-color

```html
<style>
  .accent-red {
    accent-color: red;
  }
  .accent-hex {
    accent-color: #cf74eb;
  }
  .accent-rgb {
    accent-color: rgb(255, 155, 128);
  }
  .accent-hsl {
    accent-color: hsl(250, 100%, 34%);
  }
</style>
<input class="accent-red" type="radio" checked />
<input class="accent-hex" type="checkbox" checked />
<input class="accent-rgb" type="range" />
<progress class="accent-hsl"></progress>
```

<style>
  .accent-red {
    accent-color: red;
  }
  .accent-hex {
    accent-color: #cf74eb;
  }
  .accent-rgb {
    accent-color: rgb(255, 155, 128);
  }
  .accent-hsl {
    accent-color: hsl(250, 100%, 34%);
  }
</style>
<div class="example">
  <input class="accent-red" type="radio" checked />
  <input class="accent-hex" type="checkbox" checked />
  <input class="accent-rgb" type="range" />
  <progress class="accent-hsl"></progress>
</div>

## 참고 자료

- [MDN - accent-color](https://developer.mozilla.org/en-US/docs/Web/CSS/accent-color)
