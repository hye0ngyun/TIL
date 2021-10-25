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
<div id="#app">
</div>

<script src="app.js"></script>
<script>
  const mountedApp = app.mount('#app');
</script>
```

## Attribute Binding
v-bind

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