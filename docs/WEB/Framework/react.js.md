# react.js

## useState

리엑트에서는 돔에서 변경될 부분은 useState를 사용한다.

```js
const root = document.querySelector("#root");
function App() {
  const [counter, setCounter] = React.useState(0);
  return (
    <main>
      <h3>Total count: {counter}</h3>
      <button onClick={setCounter(counter + 1)}>click</button>
    </main>
  );
}
ReactDOM.render(<App />, root);
```

### 렌더링 방식

state가 변경된 컴포넌트에 대해서 컴포넌트가 재생성되면서 재 렌더링된다.
또한 vanilla js로 DOM의 값을 변경 시켜주는 경우 태그와 값이 같이 재 렌더링 되는데,
react state를 사용할 경우는 변경된 값만 재 렌더링 된다.

```js
const root = document.querySelector("#root");
function Component() {
  const [counter, setCouner] = React.useState(0);
  console.log("하위 컴포넌트 재 랜더링");
  return (
    <div>
      <h3>Sub Total count: {counter}</h3>
      <button onClick={setCounter(counter + 1)}>sub click</button>
      /* 하위 컴포넌트의 버튼을 클릭하면 "하위 컴포넌트 재 랜더링"만 로그에
      나온다. */
    </div>
  );
}
function App() {
  const [counter, setCounter] = React.useState(0);
  console.log("상위 컴포넌트 재 렌더링");
  return (
    <main>
      <h3>Total count: {counter}</h3>
      <button onClick={setCounter(counter + 1)}>click</button>
      /* 상위 컴포넌트의 버튼을 클릭하면 "상위 컴포넌트 재 랜더링"과 "하위
      컴포넌트 재 랜더링"가 모두 로그에 나온다. */
      <Component />
    </main>
  );
}
ReactDOM.render(<App />, root);
```

## props

```js
const Btn = (props) => {
  return (
    <button
      style={{
        backgroundColor: "tomato",
        border: 0,
        color: "white",
        padding: "10px 20px",
        borderRadius: 10,
      }}
    >
      {props.text}
    </button>
  );
};
const App = () => {
  return (
    <div>
      <Btn text="Save Changes" />
      <Btn text="Continue" />
    </div>
  );
};
const root = document.getElementById("root");
ReactDOM.render(<App />, root);
```

props를 받을 떄 아래처럼 받을 수 있다. 위와 아래 모두 동일하게 작동한다.

```js
const Btn = ({ text }) => {
  return (
    <button
      style={{
        backgroundColor: "tomato",
        border: 0,
        color: "white",
        padding: "10px 20px",
        borderRadius: 10,
      }}
    >
      {text}
    </button>
  );
};
const App = () => {
  return (
    <div>
      <Btn text="Save Changes" />
      <Btn text="Continue" />
    </div>
  );
};
const root = document.getElementById("root");
ReactDOM.render(<App />, root);
```
