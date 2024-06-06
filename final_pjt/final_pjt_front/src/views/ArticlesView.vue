<template>
  <div class="container">
    <h1 class="text-center mb-5">게시판</h1>
    <button class="mb-4 btn" @click="goCreate">글쓰기</button>
    <ArticleList :article-list="store.articles" v-if="store.articles.length" />
    <h3 v-else>아직 작성된 글이 없습니다! 첫번째 글을 작성해 보는건 어떨까요?</h3>
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
const store = useCounterStore()
const router = useRouter()
onMounted(() => {
  store.getArticleList()
})
const goCreate = function () {
  if (!store.isLogin) {
    alert('로그인 하세요!!')
    router.push({ name: 'login' })
  } else {
    router.push({ name: 'create' })
  }
}
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
}
</style>
