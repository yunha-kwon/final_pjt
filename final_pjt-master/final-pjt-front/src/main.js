import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faUser, faEnvelope } from '@fortawesome/free-solid-svg-icons';

library.add(faUser, faEnvelope);
//Vuetify
import 'vuetify/styles'
import {createVuetify} from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import {aliases, mdi} from 'vuetify/iconsets/mdi-svg'

const vuetify = createVuetify({
    components,
    directives,
    icons : {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    }
})
const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)
app.use(vuetify)
app.mount('#app')
app.component('font-awesome-icon', FontAwesomeIcon);