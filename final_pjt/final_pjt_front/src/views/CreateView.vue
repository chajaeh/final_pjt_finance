<template>
  <div class="container px-5">
    <h1 class="text-center mb-5">게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목:</label>
      <input type="text" v-model="title" class="form-control" />
      <br />
      <label for="content">내용:</label>
      <textarea name="content" v-model="content" class="form-control"></textarea>
      <br />
      <button class="btn">작성</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()
const fwords = ref(null)
const createArticle = function () {
  let flag = false
  const replaceValue = '**'
  const temTitle = title.value
    .split(' ')
    .map((item) => item.trim())
    .filter((item) => item)
  const temContent = content.value
    .split(' ')
    .map((item) => item.trim())
    .filter((item) => item)
  temTitle.forEach((ele, idx) => {
    fwords.value.forEach((e) => {
      if (ele.includes(e)) {
        temTitle[idx] = replaceValue
        flag = true
        return
      }
    })
  })
  temContent.forEach((ele, idx) => {
    fwords.value.forEach((e) => {
      if (ele.includes(e)) {
        temContent[idx] = replaceValue
        flag = true
        return
      }
    })
  })
  const finalTitle = temTitle.join(' ')
  const finalContent = temContent.join(' ')
  if (flag == true) {
    warn()
  }
  axios({
    method: 'POST',
    url: `${store.BASE_URL}/api/v1/articles/`,
    data: {
      title: finalTitle,
      content: finalContent,
    },
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      router.push({ name: 'article_list' })
    })
    .catch((err) => {
      console.log(err)
    })
}
onMounted(() => {
  getFwords()
})
const getFwords = function () {
  axios({
    method: 'GET',
    url: 'src/assets/fword_list.txt',
  })
    .then((res) => {
      const dataArray = res.data
        .split('\n')
        .map((item) => item.trim())
        .filter((item) => item)
      fwords.value = dataArray
    })
    .catch((err) => {
      console.log(err)
    })
}
const warn = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/account/warn/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      if (res.data.warn >= 3) {
        alert(`욕설 누적 ${res.data.warn}회 누적으로 이용이 제한됩니다.`)
        warnSignout()
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
      } else {
        alert(`현재 욕설 누적 ${res.data.warn}회입니다.\n3회 누적될 경우 이용이 제한될 수 있습니다.`)
      }
    })
    .catch((err) => {
      console.log(err)
    })
}
const warnSignout = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/account/warn_signout/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
}
</style>
