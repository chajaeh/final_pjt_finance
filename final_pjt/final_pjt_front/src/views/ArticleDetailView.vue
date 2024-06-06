<template>
  <div class="container">
    <div v-if="article" class="container">
      <ArticleDetailMain :article="article" :fwords="fwords" @updateArticle="reload" />
      <ArticleDetailComment :article="article" :fwords="fwords" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ArticleDetailComment from '@/components/ArticleDetailComment.vue'
import ArticleDetailMain from '@/components/ArticleDetailMain.vue'
const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const fwords = ref(null)
onMounted(() => {
  getFwords()
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => console.log(err))
})
const reload = function () {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => console.log(err))
}
const getFwords = function () {
  axios({
    method: 'GET',
    url: '../src/assets/fword_list.txt',
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
</script>

<style scoped></style>
