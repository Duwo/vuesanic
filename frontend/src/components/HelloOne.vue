<template>
  <div>
    <h1>HelloOne</h1>
    {{ message }}
  </div>
</template>

<script>
const axios = require('axios')
export default {
  name: 'HelloOne',
  data () {
    return {
      message: null
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000')
      .then(response => { this.message = response.data })
  }
}
</script>
