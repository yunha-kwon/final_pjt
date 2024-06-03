<template>
  <div class="container mt-4">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <!-- Profile Info -->
        <div class="card profile-card mb-4">
          <img class="profile-img" src="@/assets/profile.jpg" alt="Profile Image">
          <div class="card-body">
            <h3 class="card-title">{{ currentUser }}</h3>
            <h5 class="card-subtitle mb-2 text-muted">{{ currentEmail }}</h5>
          </div>
        </div>
      </div>
      <div class="col-md-7">
        <!-- Liked Deposit Products -->
        <div class="liked-products">
          <div class="product-section">
            <h3 class="mb-4">좋아요한 예금 상품 정보</h3>
            <div class="product-cards">
              <div v-for="(storedDepositProduct, index) in currentDepositProducts" :key="'deposit_' + index" class="product-card-wrapper large-card">
                <div class="card product-card">
                  <div class="card-body">
                    <h5 class="card-title">{{ storedDepositProduct.fin_prdt_nm }}</h5>
                    <p class="card-text">금융상품 코드: {{ storedDepositProduct.fin_prdt_cd }}</p>
                    <p class="card-text">금융 회사명: {{ storedDepositProduct.kor_co_nm }}</p>
                    <p class="card-text">주요 유의사항: {{ storedDepositProduct.etc_note }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Deposit Pagination -->
          <div class="pagination">
            <button @click="prevDepositPage" :disabled="currentDepositPage === 1">이전</button>
            <span>{{ currentDepositPage }} / {{ totalDepositPages }}</span>
            <button @click="nextDepositPage" :disabled="currentDepositPage === totalDepositPages">다음</button>
          </div>
        </div>
        <!-- Liked Save Products -->
        <div class="liked-products">
          <div class="product-section">
            <h3 class="mb-4">좋아요한 적금 상품 정보</h3>
            <div class="product-cards">
              <div v-for="(storedSaveProduct, index) in currentSaveProducts" :key="'save_' + index" class="product-card-wrapper large-card">
                <div class="card product-card">
                  <div class="card-body">
                    <h5 class="card-title">{{ storedSaveProduct.fin_prdt_nm }}</h5>
                    <p class="card-text">금융상품 코드: {{ storedSaveProduct.fin_prdt_cd }}</p>
                    <p class="card-text">금융 회사명: {{ storedSaveProduct.kor_co_nm }}</p>
                    <p class="card-text">주요 유의사항: {{ storedSaveProduct.etc_note }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Save Pagination -->
          <div class="pagination">
            <button @click="prevSavePage" :disabled="currentSavePage === 1">이전</button>
            <span>{{ currentSavePage }} / {{totalSavePages}}</span>
            <button @click="nextSavePage" :disabled="currentSavePage === totalSavePages">다음</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useCartStore } from '@/stores/cart'

const cart = useCartStore()
const store = useCounterStore()

const currentUser = store.currentUser
const currentEmail = store.currentEmail
const storedDepositProducts = cart.storedDepositProducts
const storedSaveProducts = cart.storedSaveProducts
const depositItemsPerPage = 1
const saveItemsPerPage = 1

// Deposit Pagination
const currentDepositPage = ref(1)
const totalDepositPages = computed(() => Math.ceil(storedDepositProducts.length / depositItemsPerPage))
const currentDepositProducts = computed(() => {
  const startIndex = (currentDepositPage.value - 1) * depositItemsPerPage
  return storedDepositProducts.slice(startIndex, startIndex + depositItemsPerPage)
})

const prevDepositPage = () => {
  if (currentDepositPage.value > 1) {
    currentDepositPage.value--
  }
}

const nextDepositPage = () => {
  if (currentDepositPage.value < totalDepositPages.value) {
    currentDepositPage.value++
  }
}

// Save Pagination
const currentSavePage = ref(1)
const totalSavePages = computed(() => Math.ceil(storedSaveProducts.length / saveItemsPerPage))
const currentSaveProducts = computed(() => {
  const startIndex = (currentSavePage.value - 1) * saveItemsPerPage
  return storedSaveProducts.slice(startIndex, startIndex + saveItemsPerPage)
})

const prevSavePage = () => {
  if (currentSavePage.value > 1) {
    currentSavePage.value--
  }
}

const nextSavePage = () => {
  if (currentSavePage.value < totalSavePages.value) {
    currentSavePage.value++
  }
}
</script>

<style scoped>
.container {
  padding: 0 15px;
}

.profile-card {
  width : 100%;
  max-width: 400px; /* 프로필 카드 크기 조절 */
  border: none;
  border-radius: 15px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
}

.profile-img {
  width: 100%;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.card-body {
  padding: 20px;
}

.large-card {
  flex-basis: 100%; /* 카드 크기 조절 */
}
.card-title {
  font-size: 60px;
  text-align : center;
  margin-bottom: 10px;
}

.card-subtitle {
  font-size: 30px;
  text-align: center;
  margin-bottom: 15px;
}

.card-text {
  font-size: 16px;
}

.liked-products {
  margin-bottom: 30px;
}

.product-section {
  margin-bottom: 20px;
}

.product-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-card-wrapper {
  flex: 1 1 calc(50% - 20px); /* 카드 크기 조절 */
}

.product-card {
  border: none;
  border-radius: 15px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  display: flex;
  flex-direction: column;
}

.product-card .card-body {
  padding: 20px;  
}

.product-card .card-title {
  font-size: 30px;
  margin-bottom: 10px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.pagination button {
  margin: 0 5px;
}
</style>
