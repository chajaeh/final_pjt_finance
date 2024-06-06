<template>
  <div class="container">
    <button @click="router.push({ name: 'saving' })" class="btn">뒤로</button>
    <div class="main-container">
      <div v-if="saving" class="saving-container">
        <div class="border-bottom d-flex content-box">
          <div class="border-end category">금융회사명</div>
          <div class="content">{{ saving.kor_co_nm }}</div>
        </div>
        <div class="border-top border-bottom d-flex content-box">
          <div class="border-end category">상품명</div>
          <div class="content">{{ saving.fin_prdt_nm }}</div>
        </div>
        <div class="border-top border-bottom d-flex content-box">
          <div class="border-end category">가입방법</div>
          <div class="content">{{ saving.join_way }}</div>
        </div>
        <div class="border-top border-bottom d-flex">
          <div class="border-end category">우대조건</div>
          <div v-html="formatbr(saving.spcl_cnd)" class="content"></div>
        </div>
        <div class="border-top border-bottom d-flex">
          <div class="border-end category">이자율</div>
          <div class="content">
            <p v-for="option in saving.savingoptions_set">
              {{ option.intr_rate_type_nm }}({{ option.rsrv_type_nm }}) - 저축기간: {{ option.save_trm }} / 금리:
              {{ option.intr_rate }} / 최고우대금리: {{ option.intr_rate2 }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const saving = ref(null)

onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/finance/saving/${route.params.fin_prdt_cd}`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      saving.value = res.data
    })
    .catch((err) => console.log(err))
})
const formatbr = function (text) {
  return text.replace(/\n/g, '<br>')
}
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
  margin: 10px;
}
.category {
  width: 20%;
  align-content: center;
  padding: 10px;
}
.content {
  align-content: center;
  padding: 10px;
  width: 70%;
}
.saving-container {
  background-color: white;
  border-radius: 20px;
  padding: 10px;
}
.main-container {
  background-color: #112d4e;
  padding: 20px;
  border-radius: 20px;
}
</style>
