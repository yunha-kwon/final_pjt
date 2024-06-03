<template>
  <v-container class="container-custom">
    <h1 class="title">게시글 목록</h1>
    <v-btn class="create-button"  @click="$router.push({ name: 'CreateView' })">글쓰기</v-btn>
    <br><br>
    <v-data-table
      :headers="headers"
      :items="reversedArticles"
      class="elevation-1"
    >
      <template v-slot:item="{ item, index }">
        <tr :class="{ 'odd-row': index % 2 === 0 }">
          <td>
            <h5><router-link :to="{ name: 'ArticleDetailView', params: { id: item.id } }" class="article-link"><strong></strong> {{ item.id }}</router-link></h5>
          </td>
          <td>
            <h5><router-link :to="{ name: 'ArticleDetailView', params: { id: item.id } }" class="article-link"><strong></strong> {{ item.title }}</router-link></h5>
          </td>
          <td>
            <h5><strong>작성자</strong> : {{ item.username }}</h5>
          </td>          
          <td class="text-right">
            <h5>{{ formatDate(item.updated_at) }}</h5>
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script setup>
import { computed } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const headers = [
  { text: '제목', value: 'title' },
  { text: '작성자', value: 'username' },
  { text: '작성일', value: 'created_at', align: 'end' },
  { text: '수정일', value: 'updated_at', align: 'end' } // 수정일 항목 추가
]

const formatDate = (dateString) => {
  const options = { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}

const reversedArticles = computed(() => {
  return [...store.articles].reverse()
})
</script>

<style scoped>
.container-custom {
  max-width: 1200px;
  margin: 0 auto;
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.create-button {
  float: right;
  color : black;
  background-color: #ffffff;
}

.article-link {
  color: inherit;
  text-decoration: none;
  transition: color 0.3s;
}
.article-link:hover {
  color: #f5c1e8;
}

.text-right {
  text-align: right;
}

.odd-row {
  background-color: rgb(230, 236, 255);
  color : rgb(0, 0, 0);
}
</style>
