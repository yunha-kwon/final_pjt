<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8"> <!-- col-md-6에서 col-md-8로 변경 -->
        <div class="card shadow-sm border-0">
          <div class="card-header bg-info text-white">
            <h2 class="mb-0">로그인</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="logIn">
              <div class="mb-3">
                <label for="username" class="form-label">Username:</label>
                <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="Enter your username">
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" v-model.trim="password" id="password" class="form-control" placeholder="Enter your password">
              </div>
              <button type="submit" class="btn btn-info w-100">Log In</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const username = ref(null);
const password = ref(null);
const store = useCounterStore();

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.container {
  max-width: 800px; /* 폼의 최대 너비를 800px로 설정 */
}

.card-header {
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
}
</style>
