<template>
  <v-container class="mt-5">    
      <ArticleList />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/Article/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.primary {
  background: linear-gradient(135deg, #4e73df 0%, #1cc88a 100%);
  padding: 1rem;
}
</style>
