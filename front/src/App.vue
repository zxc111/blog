<template>
  <div id="app">
    <!-- <div>
      <p>
        If Element is successfully added to this project, you'll see an
        <code v-text="'<el-button>'"></code>
        below
      </p>
      <el-button>el-button</el-button>
    </div> -->
    <el-row>
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
      <el-col :span="12">
        <div>
          <!-- <HelloWorld msg="Title" body="test111" /> -->
        <router-view/>

           <!-- <li><router-link :to="{ name: 'about' }">foo</router-link></li> -->
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>
  </div>
</template>



<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
  /* width: 760px; */
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
