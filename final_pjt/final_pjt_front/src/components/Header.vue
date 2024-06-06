<template>
  <nav>
    <div class="user-nav d-flex">
      <img src="@/assets/logo.png" alt="logoImage" class="logo" @click="goHome" />
      <div>
        <label v-if="!store.isLogin">
          <RouterLink to="/login" class="router-link">로그인</RouterLink>
          <RouterLink to="/signup" class="router-link">회원가입</RouterLink>
        </label>
        <div v-else>
          <RouterLink to="/user/detail" class="router-link">프로필</RouterLink>
          <label class="router-link" @click="logout"> 로그아웃</label>
        </div>
      </div>
    </div>
    <div class="content-nav">
      <RouterLink to="/exchange" class="router-link-content">환율계산기</RouterLink>
      <RouterLink to="/bankmap" class="router-link-content">은행지도</RouterLink>
      <RouterLink to="/articles" class="router-link-content">게시판</RouterLink>
      <RouterLink to="/deposit" class="router-link-content">예&적금</RouterLink>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
const router = useRouter()
const store = useCounterStore()
const logout = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/accounts/logout/`,
  })
    .then((res) => {
      store.token = null
      store.isLogin = false
      store.currentUsername = null
      router.push({ name: 'home' })
    })
    .catch((err) => {
      console.log(err)
    })
}
const goHome = () => {
  router.push({ name: 'home' })
}
</script>

<style scoped>
.logo {
  width: 12%;
  cursor: pointer;
}
.user-nav {
  justify-content: space-between;
  align-items: center;
  color: #3f72af;
  padding: 5px 20px;
}
.router-link {
  text-decoration: none;
  color: #3f72af;
  cursor: pointer;
  font-size: 20px;
  font-weight: 600;
  margin-right: 20px;
}
.router-link-content {
  text-decoration: none;
  color: #3f72af;
  cursor: pointer;
  font-size: 25px;
  font-weight: 600;
  margin-right: 20px;
}
.content-nav {
  background-color: #dbe2ef;
  text-align: center;
  padding: 25px;
  margin-bottom: 50px;
}
</style>
