<template>
  <div id="chat-container" ref="chatContainer">
    <div id="chat-header">
      Y&S CHAT-BOT
      <button @click="closeChat" id="close-button">X</button>
    </div>
    <div id="chat-messages">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender === `${store.currentUser}` ? 'user-message' : 'bot-message']">
        <span class="sender">{{ message.sender }}:</span> {{ message.text }}
      </div>
    </div>
    <div id="user-input">
      <input
        type="text"
        v-model="userMessage"
        @keydown.enter="sendMessage"
        placeholder="메시지를 입력하세요..."
      />
      <v-icon :icon="mdiSend" @click="sendMessage"></v-icon>
    </div>
  </div>
</template>

<script setup>
import {useCounterStore} from '@/stores/counter';
import { ref } from 'vue';
import { mdiRobotExcitedOutline, mdiSend } from '@mdi/js';

const store = useCounterStore()
const chatContainer = ref(null);
const messages = ref([]);
const userMessage = ref('');
const apiKey = 'sk-proj-uEQIVAg5nDU5FGFMbS9OT3BlbkFJp5diLnjZ7R4q3Co6gVVT'; // 여기에 실제 API 키를 입력하세요.
const apiEndpoint = 'https://api.openai.com/v1/chat/completions';

// 미리 지정된 키워드와 답변
const predefinedAnswers = {
  '안녕' : `안녕하세요 ${store.currentUser}님! 무엇을 도와드릴까요?`,
  '날씨': '오늘 날씨는 맑고 화창합니다!',
  '이름': '저는 YS로보입니다. 만나서 반가워요!',
  '10' : "10대를 위한 상품으로는 '대구은행의 영플러스적금, 토스뱅크의 아이적금, 다올저축은행의 퍼스트유정기적금'이 존재합니다!",
  '20' : "20대를 위한 상품으로는 '광주은행의 스마트모아 Dream정기예금, 제주은행의 스마일드림 정기예금, DB저축은행의 M-DreamBig 정기예금'등이 존재합니다!",
  '30' : "30대를 위한 상품으로는 '카카오뱅크의 정기예금, 제주은행의 MZ플랜적금 , 에큐온저축은행의 직장인우대적금'등이 존재합니다!",
  '40' : "40대를 위한 상품으로는 '다올저축은행의 직장인yes정기적금, 농협은행의 NH직장인월복리적금, IBK은행의 중기근로자우대적금'등이 존재합니다!",
  '50' : "50대를 위한 상품으로는 '대구은행의 DGB행복파트너예금, 농협은행의 고향사랑 기부예금, IBK은행의 IBK평생한가족통장(실세금리정기예금)'등이 존재합니다!",
  '60' : "60대를 위한 상품으로는 '수협은행의 Sh평생주거래우대예금, 오에스비저축은행의 정기예금, 오에스비저축은행의 OSB 회전식 정기예금 '등이 존재합니다!",
  '70' : "70대를 위한 상품으로는 '수협은행의 Sh평생주거래우대예금, 오에스비저축은행의 정기예금, 오에스비저축은행의 OSB 회전식 정기예금 '등이 존재합니다!",
  '80' : "80대를 위한 상품으로는 '수협은행의 Sh평생주거래우대예금, 오에스비저축은행의 정기예금, 오에스비저축은행의 OSB 회전식 정기예금 '등이 존재합니다!",
  '90' : "90대를 위한 상품으로는 '수협은행의 Sh평생주거래우대예금, 오에스비저축은행의 정기예금, 오에스비저축은행의 OSB 회전식 정기예금 '등이 존재합니다!",
  '최초' : "은행에서 첫 상품을 가입하시려는 분들께 추천드리는 상품으로는 '광주은행의 굿스타트예금, 수협은행의 Sh첫만남우대예금, 대구은행의 DGB주거래우대예금(첫만남고객형)'등이 존재합니다!",
  '첫' : "은행에서 첫 상품을 가입하시려는 분들께 추천드리는 상품으로는 '광주은행의 굿스타트예금, 수협은행의 Sh첫만남우대예금, 대구은행의 DGB주거래우대예금(첫만남고객형)'등이 존재합니다!",
  '도움': "저는 여기서 여러 금융 관련 정보를 제공해드릴 수 있어요. 어떤 것이 궁금하신가요?",
  '환율': "현재 환율 정보를 원하시면, 구체적으로 어떤 통화에 대한 정보를 원하시는지 말씀해 주세요.",
  '금리': "현재 금리 정보를 원하시면, 예금 또는 대출 금리에 대해 말씀해 주세요.",
  '적금': "적금 상품을 찾으시나요? 특정 연령대나 조건이 있으면 말씀해 주세요.",
  '대출': "대출 상품을 찾으시나요? 대출 목적이나 조건이 있다면 말씀해 주세요.",
  '투자': "투자 상품에 대해 궁금하시군요. 어떤 종류의 투자를 생각하고 계신가요?",
  '주식': "주식 관련 정보를 찾으시나요? 특정 종목이나 시장에 대해 알고 싶으신가요?",
  '보험': "보험 상품에 대해 궁금하시다면, 생명보험, 건강보험, 자동차보험 등 구체적으로 어떤 보험인지 말씀해 주세요.",
  '연락처': "저희 은행의 고객센터 전화번호는 123-456-7890입니다. 운영 시간은 평일 오전 9시부터 오후 6시까지입니다.",
  '지점': "가까운 지점을 찾고 계신가요? 현재 위치를 알려주시면 가장 가까운 지점을 안내해 드리겠습니다.",
  '상담': "상담 예약을 원하시면, 원하시는 날짜와 시간을 말씀해 주세요. 담당자가 연락드릴 수 있도록 하겠습니다.",
  '고객센터': "고객센터 운영 시간은 평일 오전 9시부터 오후 6시까지입니다. 전화번호는 123-456-7890입니다.",
  '계좌 개설': "계좌 개설을 원하시면, 신분증과 함께 가까운 지점을 방문해 주세요. 또는 온라인으로도 개설할 수 있습니다.",
  '인터넷 뱅킹': "인터넷 뱅킹에 대한 도움을 원하시면, 인터넷 뱅킹 가이드를 참고하시거나 고객센터로 연락해 주세요.",
  '모바일 뱅킹': "모바일 뱅킹 앱을 다운로드하여 다양한 금융 서비스를 이용하실 수 있습니다. 자세한 안내는 홈페이지를 참고해 주세요.",
  '수수료': "각 서비스별 수수료는 당행 홈페이지의 수수료 안내 페이지에서 확인하실 수 있습니다.",
  '이체 한도': "이체 한도는 계좌 종류와 이용하시는 서비스에 따라 다릅니다. 자세한 내용은 고객센터에 문의해 주세요.",
  '카드 발급': "카드 발급을 원하시면, 신분증과 함께 가까운 지점을 방문해 주세요. 또는 온라인으로 신청하실 수 있습니다.",
  '분실 신고': "카드 분실 시 고객센터로 즉시 연락해 주세요. 전화번호는 123-456-7890입니다.",
  '재발급': "카드 재발급을 원하시면, 신분증을 지참하여 가까운 지점을 방문해 주세요. 재발급에는 일정 수수료가 발생할 수 있습니다.",
  '한도 상향': "카드 한도 상향을 원하시면, 신분증과 함께 가까운 지점을 방문해 주세요. 또는 고객센터로 문의해 주세요.",
  '이자율': "현재 이자율에 대한 정보는 당행 홈페이지나 고객센터에서 확인하실 수 있습니다.",
  '잔액 조회': "잔액 조회는 모바일 뱅킹 앱, 인터넷 뱅킹, ATM 또는 지점 방문을 통해 가능합니다.",
  '거래 내역': "거래 내역은 모바일 뱅킹 앱, 인터넷 뱅킹, ATM 또는 지점 방문을 통해 조회하실 수 있습니다.",
  '입출금': "입출금 서비스는 모바일 뱅킹, 인터넷 뱅킹, ATM 및 지점을 통해 이용하실 수 있습니다.",
  '정기예금': "정기예금 상품에 대해 궁금하시다면, 특정 조건이나 기간을 말씀해 주세요.",
  '연금': "연금 상품에 대해 궁금하시다면, 퇴직연금, 개인연금 등 구체적으로 어떤 연금인지 말씀해 주세요.",
  '청약': "청약 통장에 대해 궁금하시다면, 주택청약종합저축에 대해 안내해 드릴 수 있습니다.",
  '외환': "외환 거래에 대해 궁금하시다면, 환전, 해외 송금 등 구체적으로 어떤 정보를 원하시는지 말씀해 주세요.",
  '부동산': "부동산 관련 대출 상품이나 투자 정보를 원하시면 말씀해 주세요.",
  '가상화폐': "가상화폐 거래에 대한 정보는 저희 은행에서 제공하지 않습니다. 관련 거래소를 참고해 주세요."
};

function addMessage(sender, text) {
  messages.value.unshift({ sender, text });
}

function getPredefinedAnswer(message) {
  for (const keyword in predefinedAnswers) {
    if (message.includes(keyword)) {
      return predefinedAnswers[keyword];
    }
  }
  return null;
}

async function fetchAIResponse(prompt) {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.8,
      max_tokens: 1024,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0.5,
      stop: ['Human'],
    }),
  };
  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    return data.choices[0].message.content;
  } catch (error) {
    console.error('OpenAI API 호출 중 오류 발생:', error);
    return 'OpenAI API 호출 중 오류 발생';
  }
}

async function sendMessage() {
  const message = userMessage.value.trim();
  if (message.length === 0) return;
  addMessage(`${store.currentUser}`, message);
  userMessage.value = '';

  // 미리 지정된 답변이 있는지 확인
  const predefinedAnswer = getPredefinedAnswer(message);
  if (predefinedAnswer) {
    setTimeout(() => {
      addMessage('YS로보', predefinedAnswer);
    }, 1000); // 1초 지연
  } else {
    const aiResponse = await fetchAIResponse(message);
    setTimeout(() => {
      addMessage('YS로보', aiResponse);
    }, 1000); // 1초 지연
  }
}

function closeChat() {
  if (chatContainer.value) {
    chatContainer.value.style.display = 'none'; // 채팅 창을 숨김
  }
}
</script>
  
  <style scoped>
  #chat-container {
    width: 400px;
    height: 600px;
    display: flex;
    flex-direction: column;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  #chat-header {
  padding: 10px;
  background-color: #f5f5f5;
  border-radius: 10px 10px 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  }
  
  #chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column-reverse;
  }
  
  .message {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    max-width: 80%;
  }
  
  .user-message {
    background-color: rgb(255, 234, 253);
    color: black;
    align-self: flex-end;
  }
  
  .bot-message {
    background-color: #fcfcec;
    color: #333;
    align-self: flex-start;
  }
  
  .sender {
    font-weight: bold;
    margin-right: 5px;
  }
  
  #user-input {
    display: flex;
    padding: 15px;
    background-color: #f5f5f5;
    border-radius: 0 0 10px 10px;
    align-items: center;
  }
  
  #user-input input {
    flex: 1;
    padding: 10px;
    border: none;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
    margin-right: 10px;
    outline: none;
  }
  #user-input v-icon {
  margin-top: 10px; /* 아이콘을 약간 아래로 이동 */
  padding-top : 10px;
  }

  #user-input input:focus {
    border-color: #1e88e5;
  }
  
  #user-input button {
    border: none;
    background-color: #1e88e5;
    color: white;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  #user-input button:hover {
    background-color: #1565c0;
  }
  </style>
  