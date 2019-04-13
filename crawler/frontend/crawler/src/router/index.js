import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Crawler from '@/components/Crawler'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/crawler',
      name: 'Crawler',
      component: Crawler
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
