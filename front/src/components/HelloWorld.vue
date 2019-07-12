<template>
  <div class="hello">

<vue-markdown :source="body"></vue-markdown>
<!-- <vue-markdown >{{ body }}</vue-markdown> -->

  </div>
  
</template>

<script>
import VueMarkdown from 'vue-markdown'

export default {
  name: 'HelloWorld',
  props: {
    msg: String,
    id: Number,
    body: String,
  },
  components: {
    VueMarkdown
  },


  data() {
    return {
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
