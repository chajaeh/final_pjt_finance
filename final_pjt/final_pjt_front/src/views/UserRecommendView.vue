<template>
  <div class="container">
    <h1 class="text-center mb-3">예금 상품 추천</h1>
    <p class="text-center main-title">"사용자님과 비슷한 다른 사용자들이 선호하는 예금 상품을 추천해드립니다!"</p>
    <div class="list-container">
      <div class="list">
        <div v-for="product in recommends">
          <p class="content" @click="goDetail(product.fin_prdt_cd)">{{ product.fin_prdt_nm }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const recommends = ref([])
const router = useRouter()
const goDetail = function (par) {
  router.push({ name: 'deposit_detail', params: { fin_prdt_cd: par } })
}
onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/account/recommend/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      recommends.value = res.data
    })
    .catch((err) => console.log(err))
})
</script>

<style scoped>
.list {
  background-color: white;
  padding: 20px;
  border-radius: 20px;
}
.list-container {
  background-color: #112d4e;
  padding: 20px;
  border-radius: 20px;
}
.main-title {
  color: #3f72af;
}
.content {
  cursor: pointer;
}
</style>
