<template>
  <div class="page-content">
    <!-- 여기에 페이지의 콘텐츠를 넣으세요 -->
  </div>
  <footer :class="{ 'dark-mode': isDarkMode }">
    <div class="container">
      <p>&copy; 2024 Y& S Financial Service. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup>
import { useDarkMode } from '@/composables/useDarkMode';

const { isDarkMode } = useDarkMode();
</script>

<style scoped>
.page-content {
  margin-bottom: 80px; /* 푸터의 높이만큼 여백 추가 */
}

footer {
  background-color: #f8f9fa; /* Light mode background */
  color: #2c3e50; /* Light mode text color */
  padding: 1rem 0;
  text-align: center;
  width: 100%; /* 푸터가 페이지 너비를 차지하도록 설정 */
  position: fixed; /* 푸터를 고정 위치로 설정 */
  bottom: 0; /* 푸터를 하단에 배치 */
  box-sizing: border-box; /* 푸터의 높이가 포함된 박스 크기 설정 */
}

footer.dark-mode {
  background-color: #121212; /* Dark mode background */
  color: #e0e0e0; /* Dark mode text color */
}

.footer-link {
  margin: 0 1rem;
  color: #2c3e50; /* Light mode link color */
  text-decoration: none;
}

.footer-link.dark-mode {
  color: #e0e0e0; /* Dark mode link color */
}

.footer-link:hover {
  text-decoration: underline;
}

.dark-mode .footer-link:hover {
  color: #ffffff; /* Dark mode link hover color */
}
</style>
