import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProductView from '@/views/ProductView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import LogInView from '@/views/LogInView.vue'
import MapView from '@/views/MapView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import ProductSaveView from '@/views/ProductSaveView.vue'
import ProductSaveDetailView from '@/views/ProductSaveDetailView.vue'
import PersonalProductView from '@/views/PersonalProductView.vue'
import TranslateView from '@/views/TranslateView.vue'

    
import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/personal',
      name: 'PersonalProductView',
      component: PersonalProductView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/signin",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/exchange",
      name: "ExchangeRateView",
      component: ExchangeRateView,
    },
    {
      path: "/products",
      name: "ProductView",
      component: ProductView,
    },
    {
      path: "/products/:fin_prdt_cd",
      name: "ProductDetailView",
      component: ProductDetailView,
    },
    {
      path: "/saveproducts",
      name: "ProductSaveView",
      component: ProductSaveView,
    },
    {
      path: "/saveproducts/:fin_prdt_cd",
      name: "ProductSaveDetailView",
      component: ProductSaveDetailView,
    },
    {
      path: "/translate",
      name: "TranslateView",
      component: TranslateView,
    },
   
    {
      path: "/logout",
      beforeEnter: (to, from) => {
        const store = useCounterStore();
        store.clear();
        return "/";
      },
      component: {
        template: "",
      },
    },
  ]
})
router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "HomeView" && !store.isLogin) {
    window.alert("로그인이 필요합니다");
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    window.alert("이미 로그인 되어있습니다.");
    return { name: "HomeView" };
  }
});
export default router
