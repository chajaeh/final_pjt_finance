<template>
  <div class="comment-container">
    <p>댓글 목록</p>
    <form @submit.prevent="createComment" class="d-flex mb-4">
      <input type="text" v-model.trim="comment" class="create-com form-control" />
      <button class="create-button btn ms-3">댓글 작성</button>
    </form>
    <div v-if="comments">
      <ArticleDetailCommentItem
        :comments="comments"
        :fwords="fwords"
        @delete-com="deleteComment"
        @update-com="updateComment"
      />
    </div>
  </div>
</template>

<script setup>
import ArticleDetailCommentItem from '@/components/ArticleDetailCommentItem.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const comments = ref(null)
const comment = ref('')
const router = useRouter()
const props = defineProps({
  article: Object,
  fwords: Array,
})
onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/articles/${props.article.id}/comments/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      comments.value = res.data
    })
    .catch((err) => console.log(err))
})
const createComment = function () {
  let flag = false
  const replaceValue = '**'
  const temContent = comment.value
    .split(' ')
    .map((item) => item.trim())
    .filter((item) => item)

  temContent.forEach((ele, idx) => {
    props.fwords.forEach((e) => {
      if (ele.includes(e)) {
        temContent[idx] = replaceValue
        flag = true
        return
      }
    })
  })
  const finalContent = temContent.join(' ')
  if (flag == true) {
    warn()
  }
  axios({
    method: 'POST',
    url: `${store.BASE_URL}/api/v1/articles/${props.article.id}/comments/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { content: finalContent },
  })
    .then((res) => {
      comment.value = ''
      axios({
        method: 'GET',
        url: `${store.BASE_URL}/api/v1/articles/${props.article.id}/comments/`,
        headers: { Authorization: `Token ${store.token}` },
      })
        .then((res) => {
          comments.value = res.data
        })
        .catch((err) => console.log(err))
    })
    .catch((err) => console.log(err))
}
const deleteComment = function (commentId) {
  const idx = comments.value.findIndex((e) => e.id === commentId)
  comments.value.splice(idx, 1)
}
const updateComment = function (commentId, newCom) {
  const idx = comments.value.findIndex((e) => e.id === commentId)
  comments.value[idx].content = newCom
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
.comment-container {
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 15px;
}
.btn {
  color: white;
  background-color: #3f72af;
  margin-right: 10px;
}
.create-com {
  width: 80%;
}
.form-control {
  border: 1px solid #3f72af;
}
</style>
