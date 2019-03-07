import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'


export default new Router({
  routes: [
    {
      path: '/api/products',
      name: 'api',
      component: APIDemo
    }
  ]
})