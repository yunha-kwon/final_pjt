<template>
  <div class="container">
    <div class="select-container">
      <select v-model="selectedSaveTrm" class="custom-select">
        <option v-for="trm in availableSaveTrmOptions" :value="trm">{{ trm }} 개월</option>
      </select>
    </div>
    <div class="product-list">
      <h1 v-if="store.options.length > 0" class="product-title">금융 상품 코드 : {{ store.options[0].fin_prdt_nm }}</h1>
      <hr class="divider">
      <ProductOption v-for="option in filteredOptions" :key="option.id" :option="option" />
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import ProductOption from '@/components/DepositProduct/ProductOption.vue'
import { useCounterStore } from '@/stores/counter'
import { ref, computed, watchEffect } from 'vue'

const store = useCounterStore()
const route = useRoute()

const selectedSaveTrm = ref(1)

const availableSaveTrmOptions = computed(() => {
  const uniqueSaveTrms = new Set(store.options.map(option => option.save_trm))
  return Array.from(uniqueSaveTrms).sort((a, b) => a - b)
})

// Watch the availableSaveTrmOptions and set the default value to the smallest option
watchEffect(() => {
  if (availableSaveTrmOptions.value.length > 0) {
    selectedSaveTrm.value = availableSaveTrmOptions.value[0]
  }
})

const filteredOptions = computed(() => {
  return store.options.filter(option => option.save_trm == selectedSaveTrm.value)
})
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.select-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.custom-select {
  width: 100%;
  max-width: 300px;
  padding: 12px 20px;
  border: 2px solid #007BFF; /* 변경된 부분 */
  border-radius: 8px;
  font-size: 16px;
  background-color: #f9f9f9;
  color: #333;
  transition: border-color 0.3s, box-shadow 0.3s, transform 0.3s;
}

.custom-select:hover {
  border-color: #0056b3; /* 변경된 부분 */
}

.custom-select:focus {
  border-color: #0056b3; /* 변경된 부분 */
  box-shadow: 0 0 0 4px rgba(0, 123, 255, 0.25);
  outline: none;
}

.product-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.product-list {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.divider {
  margin-top: 20px; /* 변경된 부분 */
  margin-bottom: 20px;
  border: none; /* 변경된 부분 */
  border-top: 2px solid #007BFF; /* 변경된 부분 */
}
</style>
