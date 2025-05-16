// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SearchView from '@/views/SearchView.vue'
import DetailView from '@/views/DetailView.vue'
import WatchLaterView from '@/views/WatchLaterView.vue'
import FavoriteChannels from '@/views/FavoriteChannels.vue'
import VideoDetail from '@/views/VideoDetail.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/search', name: 'search', component: SearchView },
  { path: '/detail/:id', name: 'detail', component: DetailView },
  { path: '/watch-later', name: 'watchLater', component: WatchLaterView }, 
  { path: '/video/:id', name: 'video-detail', component: VideoDetail },
  { path: '/channels', name: 'channels', component: FavoriteChannels },

]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
