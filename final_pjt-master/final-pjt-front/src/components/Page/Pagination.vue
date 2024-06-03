<template>
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <button class="page-link" @click="prevPage">&laquo;</button>
        </li>
        <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: page === currentPage }">
          <button class="page-link" @click="changePage(page)">{{ page }}</button>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <button class="page-link" @click="nextPage">&raquo;</button>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    props: {
      currentPage: {
        type: Number,
        required: true
      },
      totalPages: {
        type: Number,
        required: true
      }
    },
    methods: {
      changePage(page) {
        this.$emit('page-change', page);
      },
      prevPage() {
        if (this.currentPage > 1) {
          this.$emit('page-change', this.currentPage - 1);
        }
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.$emit('page-change', this.currentPage + 1);
        }
      }
    }
  }
  </script>
  
  <style>
  /* 추가적인 스타일링이 필요하다면 여기에 작성하세요 */
  </style>
  