import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'


import axios from 'axios'
import VueAxios from 'vue-axios'
 
import Prism from 'prismjs';
// import "prismjs";
// import "prismjs/themes/prism-tomorrow.css";

// import Bulma from 'bulma/css/bulma.css'
Vue.config.productionTip = false

Prism.highlightAll();
Vue.use(VueAxios, axios)
Vue.prototype.$prism = Prism;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
