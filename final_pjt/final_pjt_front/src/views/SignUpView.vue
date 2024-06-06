<template>
  <div class="container">
    <h1 class="mb-3">회원가입 페이지</h1>
    <form @submit.prevent="signUp">
      <label class="form-label"> 이름</label>
      <input type="text" v-model="username" class="form-control" />
      <br />
      <label class="form-label">비밀번호</label>
      <input type="password" v-model="password1" class="form-control" />
      <br />
      <label class="form-label">비밀번호 확인</label>
      <input type="password" v-model="password2" class="form-control" />
      <br />
      <button class="btn">가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()
const router = useRouter()
const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
}
</style>
