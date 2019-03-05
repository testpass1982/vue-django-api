import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'

Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.min.css';

new Vue({
  render: h => h(App),
}).$mount('#app')
