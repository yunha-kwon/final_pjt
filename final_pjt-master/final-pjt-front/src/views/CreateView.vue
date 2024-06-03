<template>
  <v-container class="container-custom mt-5">
    <v-card class="shadow-sm border-0" style="height: auto;">
      <v-card-title class="bg-primary text-white d-flex justify-content-between align-items-center">
        <h2 class="mb-0">게시글 작성</h2>
        <!-- 취소 버튼 추가 -->
      </v-card-title>
      <v-card-text>
        <form @submit.prevent="createArticle">
          <v-text-field v-model.trim="title" label="제목" outlined></v-text-field>
          <v-textarea v-model.trim="content" label="내용" outlined rows="5"></v-textarea>
          <v-btn type="submit" color="primary">작성</v-btn>
          <v-btn color="error" @click="cancel">취소</v-btn> 
        </form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log(response.data)
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

const cancel = () => {
  router.push({ name: 'ArticleView' })
}
</script>

<style scoped>
.container-custom {
  max-width: 800px;
}

.card-header {
  background: linear-gradient(135deg, #4e73df 0%, #1cc88a 100%);
  padding: 1rem;
}

.card-header h2 {
  margin: 0;
}

.card-body {
  padding: 2rem;
}

.form-label {
  font-weight: bold;
}

.form-control {
  margin-top: 0.5rem;
  margin-bottom: 1rem;
}

.btn {
  margin-top: 1rem;
  color: white;
}
</style>
