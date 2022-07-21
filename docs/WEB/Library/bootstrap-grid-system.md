<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<style>
  .container > .row > div {
    border: 1px solid rgba(39,41,43,0.1);
    padding: 10px;
    background-color: #f8f8f8;
  }
</style>

# Bootstrap Grid System

부트스트랩의 그리드 시스템은 레이아웃을 행과 열로 관리하며, 열은 최대 12개의 열을 기준으로 한다.
또한 그리드를 관리할 때 **6개의 반응형 중단점**을 이용한다. 중단점은 `min-width` 미디어 쿼리를 기반으로 한다. 즉, 중단점과 그 위에 있는 모든 중단점에 영향을 미친다.(md는 992px이상의 크기에서 모두 적용된다.)

## Table of Contents

- [Bootstrap Grid System](#bootstrap-grid-system)
  - [Table of Contents](#table-of-contents)
  - [그리드 옵션 (반응형 중단점)](#그리드-옵션-반응형-중단점)
  - [열 레이아웃](#열-레이아웃)
    - [열 자동 레이아웃](#열-자동-레이아웃)
      - [Equal-width `col`](#equal-width-col)
      - [한 열의 너비 설정 `col-${number}`](#한-열의-너비-설정-col-number)
      - [가변 너비 열 (fit-content) `col-auto`](#가변-너비-열-fit-content-col-auto)
      - [행열 `row-cols-${number}`](#행열-row-cols-number)
    - [반응형 클래스 (중단점 지정)](#반응형-클래스-중단점-지정)
      - [중단점 한 열의 너비 설정 `col-${break}-${number}`](#중단점-한-열의-너비-설정-col-break-number)
      - [중단점 가변 너비 열 (fit-content) `col-${break}-auto`](#중단점-가변-너비-열-fit-content-col-break-auto)
      - [중단점 행열 `row-cols-${break}-${number}`](#중단점-행열-row-cols-break-number)

## 그리드 옵션 (반응형 중단점)

- Extra samll (xs)
- Small (sm)
- Medium (md)
- Large (lg)
- Extra large (xl)
- Extra extra large(xxl)

이런 중단점을 기준으로 그리드 시스템을 관리할 경우 클래스 접두사와 수정자 접미사가 존재한다.
예시로 `col-`이 클래스 접두사이고, `6`이 수정자라면 `col-6`이 클래스명이 된다. `col-6`의 의미는 후술하겠지만, xs이상 즉, 전체 크기에서 6열을 차지하는 열을 의미한다.

|                      | xs <br/> (<576px) | sm <br/> (>=576px) | md <br/> (<768px) | lg <br/> (<992px) | xl <br/> (<1200px) | xxl <br/> (<1400px) |
| -------------------- | ----------------- | ------------------ | ----------------- | ----------------- | ------------------ | ------------------- |
| 컨테이너 `max-width` | 없음 (자동)       | 540px              | 720px             | 960px             | 1140px             | 1320px              |
| 클래스 접두사        | `.col-`           | `.col-sm-`         | `.col-md-`        | `.col-lg-`        | `.col-xl-`         | `.col-xxl-`         |

## 열 레이아웃

열의 레이아웃을 설정하는 클래스들을 설명한다.
이후 나오게 될 클래스명에서 `${break}`는 `sm`~`xxl`같은 중단점을 의미하고, `${number}`는 `1`~`12`까지의 그리드 열 개수를 의미한다.

### 열 자동 레이아웃

#### Equal-width `col`

디바이스 크기 전체 구간에서 ~~한 행당 최대 12개의 열 까지 반응형으로 들어간다.~~ 한 행당 `col`의 개수에 따라서 `col`의 width가 동일하게 들어간다.

<!-- 어느 기준으로 행 넘김이 발생하는지 확실하지 않지만, 실험해본 결과 12개의 `col`을 넣고 `col-5`(5열 차지)를 추가한 경우 행 넘김이 발생하지 않고, 같은 조건에서 `col-6`(6열 차지)를 추가한 경우 행 넘김이 발생했다. -->

`col`과 함께 열 너비 지정 `col-${number}`을 한 행에 같이 사용한다면, 최소 content width가 지켜지지 않는 순간 줄 넘김이 발생하는듯하다.

```html
<div class="container">
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col-5">col-5</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col-6">col-6</div>
  </div>
</div>
```

<div class="container">
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col-5">col-5</div>
  </div>
    <div class="row">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col-6">col-6</div>
  </div>
</div>

#### 한 열의 너비 설정 `col-${number}`

디바이스 크기 전체 구간에서 열이 차지하는 너비가 적용된다.

```html
<div class="container">
  <div class="row">
    <div class="col">col</div>
    <div class="col-6">col-6</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col-5">col-5</div>
    <div class="col">col</div>
  </div>
</div>
```

<div class="container">
  <div class="row">
    <div class="col">col</div>
    <div class="col-6">col-6</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col">col</div>
    <div class="col-5">col-5</div>
    <div class="col">col</div>
  </div>
</div>

#### 가변 너비 열 (fit-content) `col-auto`

전체 구간에서 열의 content width만큼의 너비가 적용된다.

```html
<div class="container">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">1 of 3</div>
    <div class="col-auto">Variable width content</div>
    <div class="col col-lg-2">3 of 3</div>
  </div>
</div>
```

<div class="container">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">
      1 of 3
    </div>
    <div class="col-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
</div>

#### 행열 `row-cols-${number}`

전체 구간에서 Equal-width인 `col`의 너비를 `${number}`의 개수에 맞춰 너비를 지정한다.

```html
<div class="container">
  <div class="row row-cols-2">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row row-cols-3">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
</div>
```

<div class="container">
  <div class="row row-cols-2">
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row row-cols-3">
    <div class="col-6">col-6</div>
    <div class="col">col</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
</div>

### 반응형 클래스 (중단점 지정)

모든 열을 제어하는 반응형 클래스는 중단점 아래로 내려간 경우 `12`개의 열을 차지하도록 돼있다.
따라서 `col`을 주어 반응형 너비를 유지하게 하거나, 더 낮은 중단점의 반응형 클래스를 주어 너비를 제어할 수도 있다.

같은 원리로 행열을 제어할 때도 `row`는 기본이고, `row-cols-lg-${numbe}`를 적용하고 lg이하에서 행열을 제어하고 싶으면 `row-cols-${number}`를 주어 전체 구간에서 행열을 제어할 수 있다.

#### 중단점 한 열의 너비 설정 `col-${break}-${number}`

중단점에 해당하는 구간에서 열이 차지하는 너비가 적용된다.

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">col-md-6</div>
    <div class="col-md-6">col-md-6</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
  </div>
</div>
```

<div class="container">
  <div class="row">
    <div class="col-md-6">col-md-6</div>
    <div class="col-md-6">col-md-6</div>
    <div class="col">col</div>
    <div class="col">col</div>
  </div>
  <div class="row">
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
    <div class="col col-md-6">col col-md-6</div>
  </div>
</div>

#### 중단점 가변 너비 열 (fit-content) `col-${break}-auto`

중단점에 해당하는 구간에서 열의 content width만큼의 너비가 적용된다.

```html
<div class="container">
  <div class="row">
    <div class="col">1 of 3</div>
    <div class="col-md-auto">Variable width content</div>
    <div class="col col-lg-2">3 of 3</div>
  </div>
</div>
```

<div class="container">
  <div class="row">
    <div class="col">
      1 of 3
    </div>
    <div class="col-md-auto">
      Variable width content
    </div>
    <div class="col col-lg-2">
      3 of 3
    </div>
  </div>
</div>

#### 중단점 행열 `row-cols-${break}-${number}`

중단점에 해당하는 구간에서 Equal-width인 `col`의 너비를 `${number}`의 개수에 맞춰 너비를 지정한다.

```html
<div class="container">
  <div class="row row-cols-2 row-cols-lg-3">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
  </div>
</div>
```

<div class="container">
  <div class="row row-cols-2 row-cols-lg-3">
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
    <div class="col-4 col-lg-2">Column</div>
  </div>
</div>