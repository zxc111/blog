<template>
  <div>
    <div style="margin-top: 15px;">
      <el-input placeholder="标题" v-model="title">
      </el-input>
    </div>
    <markdown-editor v-model="content" ref="markdownEditor"></markdown-editor>
    <el-button type="primary" v-on:click="save">save</el-button>
    <el-button type="info" v-on:click="reset">reset</el-button>
  </div>
</template>

<script>
import markdownEditor from "vue-simplemde/src/markdown-editor";

export default {
  components: {
    markdownEditor
  },
  data() {
    return {
      content: "",
      title: "",
    };
  },
  props: {
    aid: String
  },
  methods: {
    reset: function() {
      this.content = "";
    },
    save: function() {
      var url = ""
      if (this.aid == "" ) {
        url = "/article/new"
      } else {
        url = "/article/"+this.aid
      }
      this.axios
        .post(url, {
          title: this.title,
          content: this.content
        })
        .then(function(response) {
          console.log(response);
        });
    }
  },
  mounted() {
    console.log(123);
    if (this.aid == "") {
      this.content = "";
      return;
    }
    this.axios.get("/article/" + this.aid).then(response => {
      this.content = response.data.article.content;
      this.title = response.data.article.title;
    });
  }
};
</script>

<style>
@import "~simplemde/dist/simplemde.min.css";
.markdown-editor .CodeMirror {
  height: 600px;
}
</style>