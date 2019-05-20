import Vue from 'vue'
import Router from 'vue-router'
import HelloOne from '@/components/HelloOne'
import HelloTwo from '@/components/HelloTwo'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/hello_world',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/hello_one',
      name: 'HelloOne',
      component: HelloOne
    },
    {
      path: '/hello_two',
      name: 'HelloTwo',
      component: HelloTwo
    }
  ]
})
