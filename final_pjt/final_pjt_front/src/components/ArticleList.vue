<template>
  <div v-if="articleList">
    <div class="d-flex ms-2 mb-2 pb-1 barbar">
      <div class="idid">번호</div>
      <div class="title">제목</div>
      <div class="profile">작성자</div>
      <div class="up-date">작성한 시각</div>
    </div>
    <ul class="list-group">
      <li v-for="article in articleList" :keys="article.id" class="list-group-item p-3">
        <div class="m-0 d-flex article-box" @click="goDetail(article.id)">
          <div class="idid">{{ article.id }}</div>
          <div class="title d-flex justify-content-between">
            <div>{{ article.title }}</div>
            <div v-if="article.created_at != article.updated_at" class="modify me-5">*수정됨</div>
          </div>
          <div class="profile">{{ article.user.username }}</div>
          <div class="up-date" style="font-size: 14px">
            {{ formattedDate(article.updated_at) }}
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
defineProps({
  articleList: Array,
})
const router = useRouter()

const goDetail = function (articleId) {
  router.push({ name: 'article_detail', params: { id: articleId } })
}
const formattedDate = (dat) => {
  const date = new Date(dat)
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  }).format(date)
}
</script>

<style scoped>
.idid {
  width: 10%;
}
.title {
  width: 50%;
}
.profile {
  width: 20%;
}
.up-date {
  width: 20%;
}
.barbar {
  border-bottom: 1px solid rgb(123, 123, 123);
}
.article-box {
  cursor: pointer;
}
.modify {
  font-size: 12px;
  color: grey;
}
</style>
