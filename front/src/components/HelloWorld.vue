<template>
  <div class="hello">
    <el-row>
      <el-col :span="20">
        <div class="grid-content">
          <!-- <h1>{{ msg }}</h1> -->
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content">
          <el-link icon="el-icon-edit" @click="edit()">编辑</el-link>
        </div>
      </el-col>
    </el-row>
    <vue-markdown :source="body" :breaks="false"></vue-markdown>
    <!-- <vue-markdown >{{ body }}</vue-markdown> -->
  </div>
</template>

<script>
import VueMarkdown from "vue-markdown";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
    aid: Number,
    body: String
  },
  components: {
    VueMarkdown
  },

  data() {
    return {};
  },
  methods: {
    edit: function() {
      console.log(123);
      location.href = "/edit/" + this.aid;
    }
  }
};
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
