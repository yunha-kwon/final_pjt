<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-lg-8 col-md-10">
        <div class="card shadow-lg border-0">
          <div class="card-header bg-info text-white text-center">
            <h2 class="mb-0">회원가입 페이지</h2>
          </div>
          <div class="card-body p-4">
            <form @submit.prevent="signUp" class="needs-validation" novalidate>
              <div class="mb-3 input-group">
                <span class="input-group-text"><v-icon :icon="mdiAccount" size="24"></v-icon></span>
                <input type="text" class="form-control" v-model.trim="username" id="username" placeholder="Username" :class="{ 'is-invalid': !isUsernameValid }" required>
                <div class="invalid-feedback">Username을 입력하세요.</div>
              </div>
              <div class="mb-3 input-group">
                <span class="input-group-text"><v-icon :icon="mdiCalendar" size="24"></v-icon></span>
                <input type="date" class="form-control" v-model.trim="birth" id="birth" @keydown="handleBirthInput" placeholder="YYYY-MM-DD" :class="{ 'is-invalid': !isBirthValid }" required>
                <div class="invalid-feedback">생년월일을 입력하세요.</div>
              </div>
              <div class="mb-3 input-group">
                <span class="input-group-text"><v-icon :icon="mdiEmail" size="24"></v-icon></span>
                <input type="email" class="form-control" v-model.trim="email" id="email" placeholder="Email" :class="{ 'is-invalid': !isEmailValid }" required>
                <div class="invalid-feedback">올바른 이메일 주소를 입력하세요.</div>
              </div>
              <div class="mb-3 input-group">
                <span class="input-group-text"><v-icon :icon="mdiLock" size="24"></v-icon></span>
                <input type="password" class="form-control" v-model.trim="password1" id="password1" placeholder="Password" :class="{ 'is-invalid': !isPassword1Valid }" required>
                <div class="invalid-feedback">Password를 입력하세요.</div>
              </div>
              <div class="mb-3 input-group">
                <span class="input-group-text"><v-icon :icon="mdiLockCheck" size="24"></v-icon></span>
                <input type="password" class="form-control" v-model.trim="password2" id="password2" placeholder="Confirm Password" :class="{ 'is-invalid': !isPassword2Valid }" required>
                <div class="invalid-feedback">Password가 일치하지 않습니다.</div>
              </div>
              <div class="mt-3 text-center">
                <button type="submit" class="btn btn-success btn-lg w-100">회원 가입</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { mdiAccount, mdiCalendar, mdiEmail, mdiLock, mdiLockCheck } from '@mdi/js';
import { VIcon } from 'vuetify/components';

const username = ref('');
const birth = ref('');
const email = ref('');
const password1 = ref('');
const password2 = ref('');
const store = useCounterStore();

const signUp = () => {
  const payload = {
    username: username.value,
    birth: birth.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};

const handleBirthInput = (event) => {
  const allowedKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'];
  if (!allowedKeys.includes(event.key) && !/^\d{0,4}-?\d{0,2}-?\d{0,2}$/.test(event.target.value + event.key)) {
    event.preventDefault();
  }
};

const isUsernameValid = computed(() => username.value.trim() !== '');
const isBirthValid = computed(() => /^\d{4}-\d{2}-\d{2}$/.test(birth.value));
const isEmailValid = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value));
const isPassword1Valid = computed(() => password1.value.trim() !== '');
const isPassword2Valid = computed(() => password2.value.trim() !== '' && password2.value === password1.value);
</script>



<style scoped>
.container {
  max-width: 800px;
}

.card {
  border-radius: 15px;
  border: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
  padding: 1.25rem;
  border-bottom: none;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.card-header h2 {
  margin: 0;
}

.card-body {
  padding: 2rem;
}

.form-label {
  font-weight: 600;
  color: #333;
  font-size: 1.1rem;
}

.input-group-text {
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px 0 0 10px;
}

.form-control {
  border-radius: 0 10px 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
  font-size: 1.1rem;
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
  color: white;
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 1.1rem;
  font-weight: 600;
}

.btn-success:hover {
  background-color: #218838;
  border-color: #218838;
}

.is-invalid {
  border-color: #dc3545;
}

.invalid-feedback {
  color: #dc3545;
  font-size: 0.875rem;
}

.input-group {
  display: flex;
  align-items: center;
  margin-bottom: 1.2rem;
}

.input-group span {
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-group .form-control {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
</style>
