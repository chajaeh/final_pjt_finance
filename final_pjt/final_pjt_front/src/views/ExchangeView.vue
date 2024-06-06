<template>
  <div>
    <h1 class="text-center mb-5">환율 계산기</h1>
    <div v-if="rate" class="container mb-4">
      <ExchangeItem :rate="rate" />
    </div>
    <div v-else class="loading container"></div>
  </div>
</template>

<script setup>
import ExchangeItem from '@/components/ExchangeItem.vue'
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const rate = ref(null)
onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/finance/exchange/`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      rate.value = res.data
      const idx = rate.value.findIndex((e) => e.cur_nm === '한국 원')
      rate.value.splice(idx, 1)
      rate.value.reverse()
    })
    .catch((err) => console.log(err))
})
</script>

<style scoped>
.container {
  width: 100%;
  height: 300px;
  background-color: #dbe2ef;
}
</style>
