<template>
  <div>
    <div class="row" v-for="(row, index) in dividedRows" :key="index">
      <ProductSaveListItem 
      v-for="(saveproduct, index) in row"
        :key="saveproduct.id"
        :saveproduct="saveproduct"
      />
    </div>
    <button @click="previousPage" :disabled="currentPage === 1"><v-icon :icon="mdiArrowLeftBoldCircle "/></button>
    <span> {{ currentPage }} / {{ totalPages }} </span>
    <button @click="nextPage" :disabled="currentPage === totalPages"><v-icon :icon="mdiArrowRightBoldCircle "/></button>
  </div>
</template>
  
<script setup>
import { ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProductSaveListItem from '@/components/SaveProduct/ProductSaveListItem.vue'
import { mdiArrowLeftBoldCircle, mdiArrowRightBoldCircle  } from '@mdi/js';

const store = useCounterStore()

const itemsPerPage = 4 // 한 페이지당 4개의 항목으로 수정
const currentPage = ref(1)

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage)
const endIndex = computed(() => startIndex.value + itemsPerPage)

const totalPages = computed(() => Math.ceil(store.products.length / itemsPerPage))

const dividedRows = computed(() => {
  return [store.saveproducts.slice(startIndex.value, endIndex.value)]
})

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

function previousPage() {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}
</script>
<style scoped>
.row {
  display: flex;
  justify-content: space-between;
}
</style>