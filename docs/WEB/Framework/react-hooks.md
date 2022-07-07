# react hooks

hooks는 react의 state machine에 연결하는 기본적인 방법이다.
functional component에서 state를 가질 수 있게 해준다.
앱을 리액트 훅으로 만든다면 class component, did mount, render등을 해주지 않아도 된다.
즉, functional programming(함수형 프로그래밍) 스타일을 갖게된다.

## 커스텀 훅 (custom hook)

### useInput

`input`입력을 받을 때 양방향 바인딩을 지원해주는 훅. 추가적으로 `vaildator`파라미터로 콜백을 받아 조건에 맞으면 입력에 대해 업데이트를 하고, 조건에 맞지 않으면 업데이트를 중지한다.

```js
export const useInput = (initialValue, validator) => {
  const [value, setValue] = useState(initialValue);
  const onChange = (e) => {
    const {
      target: { value },
    } = e;
    let willUpdate = true;
    if (typeof validator === "function") {
      willUpdate = validator(value);
    }
    if (willUpdate) {
      setValue(value);
    }
  };
  return { value, onChange };
};
```
