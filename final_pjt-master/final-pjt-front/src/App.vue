<template>
  <PageHeader/> <!-- 헤더 컴포넌트 -->
  <router-view class="do-hyeon-regular"/> <!-- 페이지 이동이 표시될 곳 -->
  <PageFooter/> <!-- 푸터 컴포넌트 -->
  <div id="chatbot-icon" @click="toggleChatbot">
    <v-icon :icon="mdiRobotExcitedOutline"></v-icon>
  </div>
  <ChatBot v-if="showChatbot"/> <!-- 챗봇 컴포넌트, showChatbot이 true일 때만 표시 -->
</template>

<script setup>
import { ref } from 'vue';
import PageHeader from '@/components/Layer/PageHeader.vue';
import PageFooter from '@/components/Layer/PageFooter.vue';
import ChatBot from '@/components/Chat/ChatBot.vue';  // 챗봇 컴포넌트 불러오기
import { provideDarkMode } from '@/composables/useDarkMode';
import { mdiRobotExcitedOutline } from '@mdi/js';

provideDarkMode();

const showChatbot = ref(false);

function toggleChatbot() {
  showChatbot.value = !showChatbot.value;
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Jua&display=swap');

.black-han-sans-regular {
  font-family: "Black Han Sans", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.jua-regular {
  font-family: "Jua", sans-serif;
  font-style: normal;
  font-size: large;
}
.do-hyeon-regular {
  font-family: "Do Hyeon", sans-serif;
  font-style: normal;
}

body {
  background: #faedf0;
}

.dark-mode {
  background-color: #121212;
  color: #e0e0e0;
}

#chatbot-icon {
  position: fixed;
  bottom: 80px;
  right: 20px;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
}
</style>
