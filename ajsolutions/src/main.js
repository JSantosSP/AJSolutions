import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios' 
import VueAxios from 'vue-axios'
axios.defaults.baseURL = 'http://localhost:5000/api/'

createApp(App).use(store).use(VueAxios, axios).use(router).mount('#app')
