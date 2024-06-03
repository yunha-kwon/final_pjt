<template>
  <nav class="navbar flex navbar-expand-lg navbar-light" :class="{ 'dark-mode': isDarkMode }">
    <div class="container">
      <RouterLink class="navbar-brand" to="/"><img src="@/assets/bank_logo.png" width="180" alt="Logo"></RouterLink>
      
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <div class="navbar-nav ms-auto">
          <RouterLink :class="{ 'nav-link': true, 'active': $route.path === '/' }" to="/"><v-icon :icon="mdiHome"/>{{ isEnglish ? 'Home' : '메인' }}</RouterLink>
          
          <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="productsDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <v-icon :icon="mdiViewList"/>{{ isEnglish ? 'View All Products' : '전체 상품 조회' }}
            </a>
           
            <ul class="dropdown-menu" aria-labelledby="productsDropdown">
              <li><RouterLink class="dropdown-item" :to="'/products'">{{ isEnglish ? 'Deposits' : '예금' }}</RouterLink></li>
              <li><RouterLink class="dropdown-item" :to="'/saveproducts'">{{ isEnglish ? 'Savings' : '적금' }}</RouterLink></li>
              <li><RouterLink class="dropdown-item" :to="'/personal'">{{ isEnglish ? 'Custom Financial Products' : '맞춤 금융상품' }}</RouterLink></li>

            </ul>
          </div>
          
          <RouterLink :class="{ 'nav-link': true, 'active': $route.path === '/map' }" :to="'/map'"><v-icon :icon="mdiMapMarker"/>{{ isEnglish ? 'Find Nearby Banks' : '주변 은행 찾기' }}</RouterLink>
          
          <RouterLink :class="{ 'nav-link': true, 'active': $route.path === '/exchange' }" :to="'/exchange'"><v-icon :icon="mdiCurrencyUsd"/>{{ isEnglish ? 'Currency Exchange' : '환율 계산' }}</RouterLink>
          
          <RouterLink :class="{ 'nav-link': true, 'active': $route.path === '/articles' }" :to="'/articles'"><v-icon :icon="mdiForum"/>{{ isEnglish ? 'Community' : '커뮤니티' }}</RouterLink>
          
          <RouterLink v-if="store.isLogin" class="nav-link" to="/profile"><v-icon :icon="mdiAccount"/>{{ isEnglish ? 'Profile' : '마이페이지' }}</RouterLink>
          <RouterLink v-if="!store.isLogin" class="nav-link" to="/signup"><v-icon :icon="mdiAccountPlus"/>{{ isEnglish ? 'Sign Up' : '회원가입' }}</RouterLink>
          
          <RouterLink v-if="!store.isLogin" class="nav-link" to="/signin"><v-icon :icon="mdiLogin"/>{{ isEnglish ? 'Sign In' : '로그인' }}</RouterLink>
          
          <RouterLink v-if="store.isLogin" class="nav-link mr-3" to="/logout"><v-icon :icon="mdiLogout"/>{{ isEnglish ? 'Log Out' : '로그아웃' }}</RouterLink>
          
          <button @click="toggleDarkMode" class="mode-button">
            <img v-if="isDarkMode" src="@/assets/moon-solid.svg" alt="moon" class="modeImg animate-rotate-y">
            <img v-else src="@/assets/sun-solid.svg" alt="sun" class="modeImg animate-rotate-y">
          </button>
          
          <RouterLink
            :class="{ 'nav-link2': true, 'active': $route.path === '/translate' }"
            to="/translate"
            @click="toggleTranslate"
          >
          <img v-if="isEnglish" src="@/assets/usa.jpg" width="30" alt="en" />
          <img v-else src="@/assets/korea.jpg" width="30" alt="kr" />
          </RouterLink>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { mdiHome, mdiViewList, mdiMapMarker, mdiCurrencyUsd, mdiForum, mdiAccount, mdiAccountPlus, mdiLogin, mdiLogout, mdiTranslate } from '@mdi/js';
import { useDarkMode } from '@/composables/useDarkMode';
import { computed } from 'vue';

const store = useCounterStore();
const { isDarkMode, toggleDarkMode } = useDarkMode();
const route = useRoute();
const router = useRouter();

const toggleTranslateLink = computed(() => {
  return route.path === '/translate' ? '/' : '/translate';
});

const toggleTranslate = (event) => {
  event.preventDefault();
  const targetPath = route.path === '/translate' ? '/' : '/translate';
  router.push(targetPath);
};

const isEnglish = computed(() => {
  return route.path === '/translate';
});
</script>

<style scoped>
.nav-link.active {
  font-weight: bold;
}

.nav-link:hover {
  color: #333333; 
}

.navbar-brand img {
  width: 80px;
}

.space {
  margin-top: 20px;
}

.navbar {
  background: #ffffff;
  margin: 0; 
  padding: 0; 
}

.navbar.dark-mode {
  background: #333333; 
}

.navbar-brand {
  padding: 0.5rem 1rem;
}

.navbar-brand img {
  width: 80px;
  border-radius: 50%;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  color: #000000; 
  font-weight: 600;
  transition: 0.3s;
  font-size: medium;
}

.nav-link v-icon {
  margin-right: 0.6rem;
}
.nav-link2 {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  color: #000000; 
  font-weight: 600;
  transition: 0.3s;
  font-size: medium;
}

.nav-link:hover {
  background: rgba(0, 0, 0, 0.1); 
  color: #000000; 
}

.navbar-text {
  color: #000000; 
  padding: 0.5rem 1rem;
}

.dropdown-menu {
  background-color: #ffffff; 
}

.dropdown-item {
  color: #000000; 
  transition: 0.3s;
}

.dropdown-item:hover {
  background-color: rgba(0, 0, 0, 0.1);
  color: #333333; 
}

.dark-mode .nav-link,
.dark-mode .navbar-text {
  color: #e0e0e0;
}

.dark-mode .dropdown-item {
  color: black;
}

.dark-mode .nav-link:hover,
.dark-mode .dropdown-item:hover {
  color: #ffffff;
}

.modeImg {
  width: 24px;
  height: 24px;
}

.us-flag {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
}

.mr-3 {
  margin-right: 1rem;
}

.mode-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}
</style>