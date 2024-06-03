<template>
  <div class="container my-5">
    <h2 class="text-center mb-4">환율 계산</h2>
    <div class="card p-4 mb-4 shadow-sm border-0">
      <div class="card-body">
        <div class="row g-3 align-items-center mb-4">
          <div class="col-12 col-md-4">
            <label for="amount" class="form-label">금액을 입력하세요</label>
            <div class="input-group">
              <span class="input-group-text">
                💵
              </span>
              <input v-model="BeforeChange" class="form-control" id="amount" placeholder="금액을 입력하세요">
            </div>
          </div>
          <div class="col-12 col-md-4">
            <label for="country" class="form-label">국가를 선택해 주세요</label>
            <div class="input-group">
              <span class="input-group-text">
                🌍
              </span>
              <select class="form-select" id="country" v-model="Change">
                <option disabled value="">국가를 선택해 주세요</option>
                <option v-for="(country, index) in Countrys" :value="ChangeInfo[index]" :key="index">
                  {{ country }} ({{ ChangeInfo[index]?.basePrice }})
                </option>
              </select>
            </div>
          </div>
          <div class="col-12 col-md-4">
            <label for="result" class="form-label">환산 금액</label>
            <div class="input-group">
              <span class="input-group-text">💰</span>
              <input class="form-control" id="result" :value="Exchange.toFixed(2)" readonly>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <hr>
    <br>
    <h2 class="text-center mb-4">국가 별 실시간 환율 정보</h2>
    <br>
    <div class="row">
      <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-3" v-for="info in ChangeInfo" :key="info.index">
        <ExchangeRateCard :info="info" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ExchangeRateCard from '@/components/Exchange/ExchangeRateCard.vue';

export default {
  name: 'ExchangeRateView',
  components: {
    ExchangeRateCard,
  },
  data() {
    return {
      Countrys: [
        'USD', 'JPY', 'EUR', 'CNY', 'HKD', 'THB', 'TWD', 'PHP', 'SGD', 'AUD',
        'VND', 'GBP', 'CAD', 'MYR', 'RUB', 'ZAR', 'NOK', 'NZD', 'DKK', 'MXN',
        'MNT', 'BHD', 'BDT', 'BRL', 'BND', 'SAR', 'SEK', 'CHF', 'AED', 'JOD',
        'ILS', 'EGP', 'INR', 'IDR', 'CZK', 'KZT', 'QAR', 'KWD', 'TRY', 'PKR',
        'PLN'
      ],
      ChangeInfo: [],
      Change: null,
      BeforeChange: '',
    };
  },
  computed: {
    Exchange() {
      if (!this.Change) return 0;
      let rlt = this.BeforeChange / this.Change.basePrice * this.Change.currencyUnit;
      if (isNaN(rlt)) return 0;
      return rlt;
    }
  },
  methods: {
    async Getdata() {
      const URL = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW';
      for (const country of this.Countrys) {
        const Get_URL = URL + country;
        const response = await axios.get(Get_URL);
        this.ChangeInfo.push(response.data[0]);
      }
    }
  },
  created() {
    this.Getdata();
  }
};
</script>

<style>
.container {
  max-width: 1200px;
}

.card {
  border-radius: 8px;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
}

.card-body {
  padding: 1.5rem;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #0056b3;
}

.card-text {
  font-size: 1rem;
}

.form-control, .form-select {
  font-size: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  border: 1px solid #ced4da;
}

.form-control:focus, .form-select:focus {
  border-color: #80bdff;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

h2 {
  font-weight: bold;
  color: #0056b3;
}

.row {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 1.5rem;
}

.list-group-item {
  font-size: 0.875rem;
  border: none;
}

.text-muted {
  font-size: 0.75rem;
}

.input-group-text {
  background-color: #007bff;
  color: white;
  border: none;
}
</style>
