<template>
  <div class="container">
    <h2>정보 입력</h2>
    <table class="table">
      <tr>
        <th class="category">성별</th>
        <td>
          <label><input type="radio" value="male" v-model="gender">남자</label>
          <label><input type="radio" value="female" v-model="gender">여자</label>
        </td>
      </tr>
      <tr>
        <th class="category">나이</th>
        <td>
          <label><input type="radio" value="age_one" v-model="ages">20세 미만</label>
          <label><input type="radio" value="age_two" v-model="ages">20세 ~ 29세</label>
          <label><input type="radio" value="age_thr" v-model="ages">30세 ~ 39세</label>
          <label><input type="radio" value="age_fou" v-model="ages">40세 ~ 49세</label>
          <label><input type="radio" value="age_fiv" v-model="ages">50세 ~ 59세</label>
          <label><input type="radio" value="age_six" v-model="ages">60세 이상</label>
        </td>
      </tr>
      <tr>
        <th class="category">연봉</th>
        <td>
          <label><input type="radio" value="sal_one" v-model="sal">2000만원 미만</label>
          <label><input type="radio" value="sal_two" v-model="sal">2000만원 ~ 4000만원</label>
          <label><input type="radio" value="sal_thr" v-model="sal">4000만원 ~ 6000만원</label>
          <label><input type="radio" value="sal_fou" v-model="sal">6000만원 ~ 8000만원</label>
          <label><input type="radio" value="sal_fiv" v-model="sal">8000만원 ~ 1억원</label>
          <label><input type="radio" value="sal_six" v-model="sal">1억원 이상</label>
        </td>
      </tr>
      <tr>
        <th class="category">자산</th>
        <td>
          <label><input type="radio" value="whl_one" v-model="whls">2000만원 미만</label>
          <label><input type="radio" value="whl_two" v-model="whls">2000만원 ~ 6000만원</label>
          <label><input type="radio" value="whl_thr" v-model="whls">6000만원 ~ 1억원</label>
          <label><input type="radio" value="whl_fou" v-model="whls">1억원 ~ 2억원</label>
          <label><input type="radio" value="whl_five" v-model="whls">2억원 ~ 4억원</label>
          <label><input type="radio" value="whl_six" v-model="whls">4억원 이상</label>
        </td>
      </tr>
      <tr>
        <th class="category">저축성향</th>
        <td>
          <label><input type="radio" value="ten_one" v-model="tendc">단기</label>
          <label><input type="radio" value="ten_two" v-model="tendc">중기</label>
          <label><input type="radio" value="ten_thr" v-model="tendc">장기</label>
        </td>
      </tr>
    </table>
    <button @click="updateInfo" class="btn btn-primary">추천 상품 조회</button>
    <br>
    <br>
    <div v-if="isLoading" class="text-center">Loading...</div>
    <div v-else>
      <div class="row">
        <div class="col-md-6">
          <h3>예금 상품</h3>
          <ul class="list-group">
            <router-link 
              v-for="product in depositProducts"
              :key="product.id"
              :to="{ name: 'ProductDetailView', params : { fin_prdt_cd : product.fin_prdt_cd }}"
              class="list-group-item"
            >
              {{ product.fin_prdt_nm }}
            </router-link>
          </ul>
        </div>
        <div class="col-md-6">
          <h3>저축 상품</h3>
          <ul class="list-group">
            <router-link 
              v-for="product in saveProducts"
              :key="product.id"
              :to="{ name: 'ProductSaveDetailView', params : { fin_prdt_cd : product.fin_prdt_cd } }"
              class="list-group-item"
            >
              {{ product.fin_prdt_nm }}
            </router-link>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import age_fivxios from 'axios';
import { RouterLink } from 'vue-router';
import { ref, watch } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2'

const info = ref({
  gen_one: false,
  gen_two: false,
  age_one: false,
  age_two: false,
  age_thr: false,
  age_fou: false,
  age_fiv: false,
  age_six: false,
  sal_one: false,
  sal_two: false,
  sal_thr: false,
  sal_fou: false,
  sal_fiv: false,
  sal_six: false,
  whl_one: false,
  whl_two: false,
  whl_thr: false,
  whl_fou: false,
  whl_five: false,
  whl_six: false,
  ten_one: false,
  ten_two: false,
  ten_thr: false
})
const gender = ref("");
const sal = ref("");
const ages = ref("");
const whls = ref("")
const tendc = ref("");

watch(gender, (newVal) => {
  if(newVal === "male") {
    info.value.gen_one = true;
    info.value.gen_two = false;
  } else {
    info.value.gen_one = false;
    info.value.gen_two = true;
  }
});

watch(ages, (newVal) => {
    const ages = ['age_one', 'age_two','age_thr','age_fou','age_fiv','age_six'];
    ages.forEach(element => {
      info.value[element] = false;
    });
    info.value[newVal] = true;
});

watch(sal, (newVal) => {
    const sals = ['sal_one', 'sal_two','sal_thr','sal_fou','sal_fiv','sal_six'];
    sals.forEach(element => {
      info.value[element] = false;
    });
    info.value[newVal] = true;
});

watch(whls, (newVal) => {
    const whls = ['whl_one', 'whl_two','whl_thr','whl_fou','whl_five','whl_six'];
    whls.forEach(element => {
      info.value[element] = false;
    });
    info.value[newVal] = true;
});
watch(tendc, (newVal) => {
    const tendc = ['ten_one', 'ten_two','ten_thr'];
    tendc.forEach(element => {
      info.value[element] = false;
    });
    info.value[newVal] = true;
});


const isLoading = ref(false);
const depositProducts = ref([]);
const saveProducts = ref([]);

const updateInfo = () => {
  if (!gender.value || !ages.value || !sal.value || !whls.value || !tendc.value) {
    Swal.fire({
      title: "경고",
      text: "모든 필드를 선택해주세요.",
      icon: "warning"
    });
    return;
  }

  isLoading.value = true;
  // "잠시만 기다려주세요" 메시지와 로딩 표시
  Swal.fire({
  title: "나에게 맞는 상품을 찾고 있습니다!",
  didOpen: () => {
    const title = Swal.getPopup().querySelector(".swal2-title");
    title.style.fontSize = "1.7em"; // 글꼴 크기를 조정할 수 있음
    Swal.showLoading();
  },
  allowOutsideClick: false,
  allowEscapeKey: false,
  allowEnterKey: false
});

  const requestData = {
    info: info.value
  };

  // 2초 후에 요청을 보내도록 함
  setTimeout(() => {
    axios.post(`http://127.0.0.1:8000/finlife/update/`, requestData)
      .then(response => {
        const matchingId = response.data.matching_id;
        if (matchingId) {
          fetchRecommendedProducts(matchingId);
        } else {
          Swal.fire({
            title: "알림",
            text: "일치하는 ID를 찾을 수 없습니다.",
            icon: "info"
          });
        }
      })
      .catch(error => {
        console.error(error);
        Swal.fire({
          title: "오류",
          text: "정보를 업데이트하는 중 오류가 발생했습니다.",
          icon: "error"
        });
      })
      .finally(() => {
        isLoading.value = false;
        Swal.close(); // 로딩 창 닫기
      });
  }, 2000); // 2초 지연
};


const fetchRecommendedProducts = (userId) => {
  isLoading.value = true;
  axios.get(`http://127.0.0.1:8000/finlife/recommend/${userId}`)
    .then(response => {
      depositProducts.value = response.data.deposit_products;
      saveProducts.value = response.data.save_products;
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
    })
    .finally(() => {
      isLoading.value = false;
    });
};
</script>
<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f7f7f7;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  max-width: 1200px;
  width: 100%;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 10px;
}

th {
  background-color: #f2f2f2;
  border-bottom: 2px solid #ddd;
}

td {
  border-bottom: 1px solid #ddd;
}

td input[type="checkbox"] {
  margin-right: 10px;
}

.category {
  font-weight: bold;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

button:hover {
  background-color: #0056b3;
}
</style>