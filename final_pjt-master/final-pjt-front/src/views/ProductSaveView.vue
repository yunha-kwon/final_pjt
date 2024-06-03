<template>
    <div class="container mt-5">
      <div class="card shadow-sm border-0">
        <div class="card-header custom-bg text-white d-flex justify-content-between align-items-center">
          <h2 class="mb-0">모든 적금 상품 조회</h2>
          <RouterLink :to="{ name: 'HomeView'}" class="btn btn-light">
            [BACK]
          </RouterLink>
        </div>
        <div class="card-body">
          <ProductSaveList/>
        </div>
        <div class="card-footer text-muted text-center">
          <small>은행 상품 정보를 제공합니다.</small>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink } from 'vue-router'
  import ProductSaveList from '@/components/SaveProduct/ProductSaveList.vue'
  
  const store = useCounterStore()
  
  onMounted(() => {
    store.getSaveProduct()
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
    margin: 0;
  }
  
  .card-body {
    padding: 2rem;
  }
  
  .card-footer {
    background-color: #f8f9fa;
    padding: 1rem;
  }
  
  .btn-light {
    color: #4e73df;
    border: 1px solid #4e73df;
    background-color: #ffffff;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .btn-light:hover {
    background-color: #4e73df;
    color: #ffffff;
  }
  </style>
  