<template>
  <div id="app">
    <img src="./assets/logo.png">
    <p>
      <router-link to="/hello_one">Go to One</router-link>
      <router-link to="/hello_two">Go to Two</router-link>
    </p>
  <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
