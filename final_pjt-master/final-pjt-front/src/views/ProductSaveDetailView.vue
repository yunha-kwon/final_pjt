<template>
    <div class="container mt-5">
        <div class="card shadow-sm border-0" style="background-color: #f8f9fa;">
        <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
          <h2 class="mb-0">상품 상세 정보</h2>
          <RouterLink :to="{ name: 'ProductSaveView'}" class="btn btn-light">
            [BACK]
          </RouterLink>
        </div>
        <div class="card-body">
          <ProductSaveListItemDetail/>
        </div>
        <div class="card-footer text-muted">
          <small>은행 상품 상세정보를 제공합니다.</small>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink, useRoute } from 'vue-router'
  import ProductSaveListItemDetail from '@/components/SaveProduct/ProductSaveListItemDetail.vue'
  
  const route = useRoute()
  const store = useCounterStore()
  
  onMounted(() => {
    store.getSaveProductOption(route.params.fin_prdt_cd)
  })
  </script>
  
  <style scoped>
  .container {
    max-width: 900px;
  }
  
  .card-header {
    background: linear-gradient(135deg, #4e73df 0%, #1cc88a 100%);
    padding: 1rem;
  }
  
  .card-header h2 {
    font-size: 1.5rem;
  }
  
  .card-body {
    padding: 2rem;
  }
  
  .card-footer {
    background-color: #f8f9fa;
    text-align: center;
  }
  </style>
  