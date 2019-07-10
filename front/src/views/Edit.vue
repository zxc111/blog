<template>
  <div>
    <markdown-editor v-model="content" ref="markdownEditor"></markdown-editor>
    <el-button type="primary" v-on:click="save">save</el-button>
    <el-button type="info" v-on:click="reset">reset</el-button>
    <!-- <el-button type="info" v-on:click="reset">reset</el-button> -->
  </div>
</template>

<script>
import markdownEditor from "vue-simplemde/src/markdown-editor";
// import func from "../../vue-temp/vue-editor-bridge";

export default {
  components: {
    markdownEditor
  },
  data() {
    return {
      content: ""
    };
  },
  methods: {
    echo: function() {
      alert(this.content);
    },
    reset: function() {
      this.content = "";
    },
    save: function() {
      this.axios.post(
         "/article/new",
        {
          title: "test",
          content: this.content
        },
      ).then(function(response) {
        console.log(response);
      });
    }
  },
  mounted() {
    this.axios
      .get("https://raw.githubusercontent.com/axios/axios/master/README.md")
      .then(response => {
        //   console.log(response.data);
        this.content = response.data;
      });
  }
};
</script>

<style>
@import "~simplemde/dist/simplemde.min.css";
</style>