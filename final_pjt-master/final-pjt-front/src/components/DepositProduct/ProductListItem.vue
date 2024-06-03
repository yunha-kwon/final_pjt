<template>
  <div>
    <div class="container">
      <button @click="toggleHeartColorAndSaveProduct" class=" ra">
        <v-icon :color="isHeartRed ? 'red' : 'black'">{{ mdiHeart }}</v-icon>
      </button><br><br>
      <h4 class="ra">금융 상품명 : <span>{{ product.fin_prdt_nm }}</span></h4>
      <p>금융상품 코드 : {{ product.fin_prdt_cd }}</p>
      <p>금융 회사명 : {{ product.kor_co_nm }}</p>
      <p>주요 유의사항 : {{ product.etc_note }}</p>
      <RouterLink 
        :to="{ name: 'ProductDetailView', params: { fin_prdt_cd: product.fin_prdt_cd }}"
      >
        [DETAIL]
      </RouterLink>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { mdiHeart } from '@mdi/js'
import { RouterLink } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'
const cart = useCartStore()

const props = defineProps({
  product: Object
})

const { storedDepositProducts } = storeToRefs(cart);
const isHeartRed = computed(() => {
  return storedDepositProducts.value.some(p => p.id === props.product.id)
})

// 로컬 스토리지에서 초기 상태 복원
onMounted(() => {
})

// 하트 상태 변경 시 로컬 스토리지에 저장된 상품 정보 업데이트
const toggleHeartColorAndSaveProduct = () => {
  if (isHeartRed) {
    cart.toggleStoredDepositProducts(props.product) // Pinia 스토어에 저장
  }
}
</script>

<style>
/* 추가 스타일이 필요하다면 여기에 작성 */
.ra {
  display: inline-block;
}

</style>
