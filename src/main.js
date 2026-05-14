import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from './router'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

const options = {
    toastClassName: 'my-custom-toast-class',
    bodyClassName: 'custom-body-class'};

const app = createApp(App)
app.use(Toast,options)
app.use(router)
app.mount('#app')