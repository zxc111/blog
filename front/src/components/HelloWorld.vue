<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
       <li><router-link :to="{ name: 'about' }">foo</router-link></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  <div v-html="bbb"></div>
<!-- <vue-markdown>this is the default slot</vue-markdown> -->
<vue-markdown :source="body"></vue-markdown>

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
    aaa: "<a href='http://zxc111.xyz'>zxc111.xyz</a>",
    bbb: "<el-link  href='http://zxc111.xyz'>123</el-link>",
//     body: "# vue-cli-plugin-element\n\n\
// Element plugin for `@vue/cli` 3.0.\n\n\
// ### Install\n\n\
// First you need to install `@vue/cli` globally (follow the instructions [here](https://cli.vuejs.org/)).\n\n\
// Then create a project and add the Element plugin:"
    }
  }
}
// var a = "<a url='http://zxc111.xyz'>zxc111.xyz</a>";
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
