<template>
  <div class="home">
    <div v-for="article in articles">
      <HelloWorld :msg="article.title" :body="article.content" :aid="article.aid" />
    </div>
    <el-pagination
      layout="prev, pager, next, total, sizes"
      :total="total"
      :page-size="page_size"
      @current-change="change_page"
      :page-sizes="[1,5,10]"
      @size-change="change_page_size"
    ></el-pagination>
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
      body: "",
      total: 0,
      page: 1,
      page_size: 1,
      articles: []
    };
  },
  methods: {
    change_page(val) {
      this.page = val;
      this.get_body();
    },
    change_page_size(val) {
      this.page_size = val;
      this.get_body();
    },
    get_body() {
      var _this = this;
      var base_url = "/article/list?";
      this.axios
        .get(base_url + "page_size=" + _this.page_size + "&page=" + _this.page)
        .then(function(response) {
          if (response.status == 200 && response.data.status == 0) {
            _this.total = response.data.data.total;
            _this.articles = response.data.data.articles;
          } else {
            alert("error");
          }
        });
        // console.log(123);
        setTimeout(_this.$prism.highlightAll, 1000)      ;
        // setTimeout(function() {console.log(321)}, 10000)      ;
        // _this.$prism.highlightElement(document.getElementsByClassName("hello"));

    }
  },
  mounted() {
    this.get_body();
  }
};
</script>
