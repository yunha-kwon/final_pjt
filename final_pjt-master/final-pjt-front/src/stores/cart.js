import { ref, computed, watch } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCounterStore } from './counter'

export const useCartStore = defineStore('cart', () => {
  const { currentUser } = storeToRefs(useCounterStore())
  const customer = ref(null)
  const storedDepositProducts = ref([])
  const storedSaveProducts = ref([])
  
  watch(currentUser, (newUser) => {
      if(newUser !== customer.value) {
        storedDepositProducts.value = []
        storedSaveProducts.value = []
          customer.value = newUser
      }
  })

  const toggleStoredDepositProducts = (product) => {    
    const idx = storedDepositProducts.value.findIndex((item) => item.id === product.id)
        if (idx === -1) {
          storedDepositProducts.value.push(product)
        } else {
          storedDepositProducts.value.splice(idx, 1)
        }
    }
  
  const toggleStoredSaveProducts = (product) => {    
    const idx = storedSaveProducts.value.findIndex((item) => item.id === product.id)
        if (idx === -1) {
          storedSaveProducts.value.push(product)
        } else {
          storedSaveProducts.value.splice(idx, 1)
        }
    }
 
  return {
    storedDepositProducts,
    storedSaveProducts,
    toggleStoredDepositProducts,
    toggleStoredSaveProducts
  }
}, { persist: true })
