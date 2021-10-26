# Vue.js(뷰)

## Creating Vue App
```js
// app.js
const app = Vue.createApp({
  data() {
    return {
      product: 'Boots'
    }
  }
})
```
```html
<!-- main.html -->
<div id="#app">
</div>

<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```

## Attribute Binding
v-bind:attributeName

```js
// app.js
const app = Vue.createApp({
    data() {
        return {
            product: 'Socks', 
            image: './assets/images/socks_green.jpg', 
            url: 'https://google.com'
        }
    }
})
```
```html
<!-- main.html -->
<div id="#app">
  <!-- display product data with mustache -->
  <h2>{{ product }}</h2>
  <!-- bind image to src attribute -->
  <img v-bind:src="image">
  <!-- bind url to herf attribute (':' is v-bind shorthand) -->
  <a :href="url">google</a>
</div>
<!-- load app.js -->
<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```

## Conditional Rendering
v-if=""
v-else-if=""
v-else

v-show=""
```js
// app.js
const app = Vue.createApp({
    data() {
        return {
            inventory: 9, 
            onSale: true
        }
    }
})
```
```html
<!-- main.html -->
<div id="#app">
  <!-- inventory가 10개 초과일 경우 -->
  <p v-if="inventory > 10">In Stock</p>
  <!-- inventory가 0개 초과 10개 미만인 경우 -->
  <p v-else-if="inventory <= 10 && inventory > 0">Almost Sold Out!</p>
  <!-- 그외, 0개 미만인 경우 -->
  <p v-else>Out Of Stock</p>

  <!-- 만약 onSale이 true라면 보여주고 false라면 display: none;을 갖는다. -->
  <p v-show="onSale">On Sale</p>
</div>
<!-- load app.js -->
<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```

## List Rendering
v-for=""

```js
// app.js
const app = Vue.createApp({
    data() {
        return {
            details: ['50% cotton', '30% wool', '20% polyester'], 
            variants: [
              { id: 2234, color: 'green', image: './assets/images/socks_green.jpg' },
              { id: 2235, color: 'blue', image: './assets/images/socks_blue.jpg' },
            ]
        }
    }
})
```
```html
<!-- main.html -->
<div id="#app">
  <!-- python의 for문과 유사하다. -->
  <ul>
    <li v-for="detail in details">{{ detail }}</li>
  </ul>
  <!-- :key는 각 돔 앨리먼트에 id값을 넣어준다. -->
  <div v-for="variant in variants" :key="variant.id">{{ variant.color }}
    </div>
</div>
<!-- load app.js -->
<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```
### key
특수한 속성 key는 주로 Vue의 가상 DOM 알고리즘이 노드의 ID를 식별하기 위한 힌트로 사용된다. 이를 통해 Vue는 어느 시점에 기존 노드를 가져오고 재사용 할 수 있는지, 또 재정렬과 재생성이 필요한 때가 언제인지 파악한다.

## Class & Style Binding
:style="{ property: value }"
:style="styles object"
:class="{ class name: condition }"
:class="[conditon ? true class name : false class name]"

```js
// app.js
const app = Vue.createApp({
    data() {
        return {
            cart: 0, 
            details: ['50% cotton', '30% wool', '20% polyester'], 
            variants: [
              { id: 2234, color: 'green', image: './assets/images/socks_green.jpg' },
              { id: 2235, color: 'blue', image: './assets/images/socks_blue.jpg' },
            ], 
            styles {
              color: 'red', 
              fontSize: '14px'
            }, 
            activeClass: true, 
            isActive: true
        }
    }
})
```
```html
<!-- main.html -->
<div id="#app">
  <!-- style binding -->
  <!-- camelCase -->
  <div :style="{ backgroundColor: variant.color }"></div>
  <!-- kebab-case -->
  <div :style="{ 'background-color': variant.color }"></div>
  <!-- styles object -->
  <div :style="styles"></div>

  <!-- class binding -->
  <!-- Multiple Classes -->
  <!-- activeClass가 참인 경우 class에 active가 추가된다. -->
  <div class="color-circle" :class="{ active: activeClass }">
  </div>
  <!-- Ternary Operators -->
  <!-- 삼항 조건 연산자를 이용해 isActive가 참이라면 activeClass를 클래스명으로 추가, 거짓이라면 ''를 추가 -->
  <div :class="[isActive ? activeClass : '']">
  </div>
</div>
<!-- load app.js -->
<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```
## Computed Properties

```js
// app.js
const app = Vue.createApp({
    data() {
        return {
            brand: 'Vue Mastery', 
            product: 'Socks',
            selectedVariant: 0
            variants: [
              { id: 2234, color: 'green', image: './assets/images/socks_green.jpg', quantity: 50 },
              { id: 2235, color: 'blue', image: './assets/images/socks_blue.jpg', quantity: 50 },
            ], 
            onSale: true
        }
    }, 
    methods: {
      updateVariant(index) {
        this.selectedVariant = index
      }
    },
    computed: {
      title() {
        return this.brand + " " + tihs.product
      }, 
      image() {
        return this.variants[this.selectedVariant].image
      }, 
      inStock() {
        return this.variants[this.selectedVariant].quantity
      }, 
      sale() {
        if(this.onSale) {
          return this.title + " is on sale"
        }
      }
    }
})
```
```html
<!-- main.html -->
<div id="#app">
  <!-- computed property  -->
  <!-- Vue Mastery Socks -->
  <h2>{{ title }}</h2>
  <!-- Vue Mastery Socks is on sale -->
  <p>{{ sale }}</p>
  <img :src="image">
  <!-- (variant, index) in variants는 python의 enumerate처럼 인덱스를 같이 가져오는것 같음 -->
  <div class="color-circle" v-for="(variant, index) in variants" :key="variant.id" @mouseover="updateVariant(index)" :style="{ backgroundColor: variant.color }">
  </div>
</div>
<!-- load app.js -->
<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```