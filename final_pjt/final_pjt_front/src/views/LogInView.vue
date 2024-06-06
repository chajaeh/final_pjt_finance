<template>
  <div class="container">
    <h1 class="mb-3">로그인 페이지</h1>
    <form @submit.prevent="login">
      <label for="id" class="form-label">id</label>
      <input type="text" v-model="username" class="form-control" />
      <br />
      <label for="password" class="form-label">비밀번호</label>
      <input type="password" v-model="password" class="form-control" />
      <br />
      <button class="mb-2 btn">로그인</button>
      <p>아이디가 없으신가요? <button class="ms-2 btn" @click="goSignUp">회원가입</button></p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const username = ref(null)
const password = ref(null)
const store = useCounterStore()
const router = useRouter()
const login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.login(payload)
}
const goSignUp = function () {
  router.push({ name: 'signup' })
}
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
}
</style>
