<template>
  <div class="home">
    <div v-for="article in articles">
    <HelloWorld :msg="article.title" v-bind:body="article.content" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  },
  data() {
    return {
      body: "123",
      articles: [],
    }
  },
  mounted() {
    var _this = this;
     this.axios.get("/article/list?page_size=4").then(function(response) {
      if (response.status == 200 && response.data.status == 0) {
        _this.articles = response.data.data.articles;
      } else {
        alert("error");
      }
    });
  }
};
</script>
