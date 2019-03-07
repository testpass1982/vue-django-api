import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'

Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.min.css';
import VueRouter from 'vue-router'
import VueResource from 'vue-resource';
Vue.use(VueRouter);
Vue.use(VueResource);

new Vue({
  render: h => h(App),
}).$mount('#app')
