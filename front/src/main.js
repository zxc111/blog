import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'


Vue.config.productionTip = false
import axios from 'axios'
import VueAxios from 'vue-axios'
 
import Prism from 'prismjs';
import "prismjs";
import "prismjs/themes/prism-tomorrow.css";

// import Bulma from 'bulma/css/bulma.css'

Prism.highlightAll();
Vue.use(VueAxios, axios)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
