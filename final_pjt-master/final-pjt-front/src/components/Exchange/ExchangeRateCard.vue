<template>
  <div class="card mb-4 border-0 shadow-sm">
    <div class="card-header custom-bg text-white">
      <h5 class="card-title mb-0">{{ info.name }}</h5>
    </div>
    <div class="card-body">
      <p class="card-text">
        <strong>시작 가격:</strong> {{ info.openingPrice }}
        <span :style="{ color: RiseFallColor, 'font-weight': 'bold' }">
          {{ info.change === 'RISE' ? '▲' : '▼' }} {{ info.changePrice.toFixed(2) }}
        </span>
      </p>
      <ul class="list-group list-group-flush">
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <strong>현찰 살 때:</strong>
          <span>{{ info.cashBuyingPrice.toFixed(2) }}</span>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <strong>현찰 팔 때:</strong>
          <span>{{ info.cashSellingPrice.toFixed(2) }}</span>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <strong>송금 보낼 때:</strong>
          <span :style="{ color: RiseFallColor, 'font-weight': 'bold' }">{{ info.ttSellingPrice.toFixed(2) }}</span>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <strong>송금 받을 때:</strong>
          <span>{{ info.ttBuyingPrice.toFixed(2) }}</span>
        </li>
        <li class="list-group-item text-end text-muted">
          <small>날짜: {{ currentDate }}</small>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChangeInfoCard',
  props: {
    info: Object,
  },
  computed: {
    RiseFallColor() {
      return this.info.change === 'FALL' ? 'green' : 'red';
    },
    currentDate() {
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0');
      const day = String(today.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 8px;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
}

.card-header {
  border-bottom: 1px solid #e9ecef;
  font-size: 1.25rem;
  font-weight: bold;
  text-align: center;
}

.card-body {
  padding: 1rem 1.25rem;
}

.card-text {
  font-size: 1rem;
  margin-bottom: 1rem;
}

.list-group-item {
  font-size: 0.9rem;
  border: none;
  padding: 0.75rem 1rem;
}

.text-muted {
  font-size: 0.75rem;
}

/* 추가된 스타일 */
.custom-bg {
  /* background: linear-gradient(135deg, #4e73df 0%, #1cc88a 100%); */
  background: rgb(13, 178, 243);
}

.text-white {
  color: #fff; /* 텍스트를 흰색으로 변경 */
}

.card-title {
  margin-bottom: 0; /* 제목과 컨테이너 사이의 간격 제거 */
}

.card-title::after {
  content: ''; /* 추가적인 스타일링을 위한 가상 요소 */
  display: block;
  width: 40px;
  height: 2px;
  background-color: #fff;
  margin: 8px auto; /* 수직 가운데 정렬 */
}

.list-group-item {
  border-bottom: 1px solid #e9ecef; /* 각 리스트 아이템에 구분선 추가 */
}

.list-group-item:last-child {
  border-bottom: none; /* 마지막 아이템의 구분선 삭제 */
}

.list-group-item span {
  font-weight: bold;
  color: #333;
}
</style>
