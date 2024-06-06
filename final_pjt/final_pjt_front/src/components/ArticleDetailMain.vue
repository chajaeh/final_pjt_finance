<template>
  <div v-if="article" class="main-container">
    <div v-if="!update">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>마지막으로 수정한 시각 : {{ formattedDate }}</p>
      <hr />
      <div v-if="article.user.username === store.currentUsername">
        <button @click="update = !update" class="btn">수정</button>
        <button @click="deleteDetail" class="btn" id="delete-button">삭제</button>
      </div>
    </div>
    <form v-else @submit.prevent="updateDetail">
      <label for="newTitle">제목 : </label>
      <input type="text" v-model.trim="newTitle" class="form-control" />
      <br />
      <label for="newTitle">내용 : </label>
      <textarea name="newContent" id="newContent" v-model.trim="newContent" class="form-control"></textarea>
      <hr />
      <button class="btn">수정 확정</button>
      <button @click="update = !update" class="btn">수정 취소</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const update = ref(false)
const props = defineProps({
  article: Object,
  fwords: Array,
})
const newTitle = ref(`${props.article.title}`)
const newContent = ref(`${props.article.content}`)
const emit = defineEmits(['updateArticle'])
const updateArticle = function () {
  emit('updateArticle')
}
const deleteDetail = function () {
  axios({
    method: 'DELETE',
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      router.push({ name: 'article_list' })
    })
    .catch((err) => console.log(err))
}
const updateDetail = async () => {
  let flag = false
  const replaceValue = '**'
  const temTitle = newTitle.value
    .split(' ')
    .map((item) => item.trim())
    .filter((item) => item)
  const temContent = newContent.value
    .split(' ')
    .map((item) => item.trim())
    .filter((item) => item)
  temTitle.forEach((ele, idx) => {
    props.fwords.forEach((e) => {
      if (ele.includes(e)) {
        temTitle[idx] = replaceValue
        flag = true
        return
      }
    })
  })
  temContent.forEach((ele, idx) => {
    props.fwords.forEach((e) => {
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
    await warn()
  }
  axios({
    method: 'PUT',
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { title: finalTitle, content: finalContent },
  })
    .then((res) => {
      updateArticle()
      update.value = !update.value
    })
    .catch((err) => console.log(err))
}
const formattedDate = computed(() => {
  const date = new Date(props.article.updated_at)
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  }).format(date)
})
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
watch(
  () => props.article,
  () => {
    newTitle.value = props.article.title
    newContent.value = props.article.content
  }
)
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
  margin-bottom: 10px;
  margin-right: 10px;
}
.main-container {
  background-color: #f0f0f0;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 15px;
}
#delete-button {
  background-color: rgba(255, 0, 0, 0.661);
}
</style>
