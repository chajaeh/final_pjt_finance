<template>
  <div class="container">
    <button @click="this.$router.go(-1)" class="btn">뒤로</button>
    <div class="main-container">
      <div v-if="deposit" class="deposit-container">
        <div class="border-bottom d-flex content-box">
          <div class="border-end category">금융회사명</div>
          <div class="content">{{ deposit.kor_co_nm }}</div>
        </div>
        <div class="border-top border-bottom d-flex content-box">
          <div class="border-end category">상품명</div>
          <div class="content">{{ deposit.fin_prdt_nm }}</div>
        </div>
        <div class="border-top border-bottom d-flex content-box">
          <div class="border-end category">가입방법</div>
          <div class="content">{{ deposit.join_way }}</div>
        </div>
        <div class="border-top border-bottom d-flex">
          <div class="border-end category">우대조건</div>
          <div v-html="formatbr(deposit.spcl_cnd)" class="content"></div>
        </div>
        <div class="border-top border-bottom d-flex">
          <div class="border-end category">이자율</div>
          <div class="content">
            <p v-for="option in deposit.depositoptions_set">
              {{ option.intr_rate_type_nm }} - 저축기간: {{ option.save_trm }} / 금리: {{ option.intr_rate }} /
              최고우대금리: {{ option.intr_rate2 }}
            </p>
          </div>
        </div>
        <button v-if="!isAlreadyJoined" @click="addDeposit" class="btn">가입하기</button>
        <p v-else class="mt-3">이미 가입한 상품입니다!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const deposit = ref(null)
const user = ref(null)
const router = useRouter()
onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.BASE_URL}/api/v1/finance/deposit/${route.params.fin_prdt_cd}`,
    headers: { Authorization: `Token ${store.token}` },
  })
    .then((res) => {
      deposit.value = res.data
    })
    .catch((err) => console.log(err))
  store.getUserDetail()
  user.value = store.userDetail
})

const addDeposit = function () {
  axios({
    method: 'put',
    url: `${store.BASE_URL}/account/add_deposit/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { fin_prdt_cd: deposit.value.fin_prdt_cd },
  }).then((res) => {
    alert('가입 완료')
    router.push({ name: 'user_detail' })
  })
}

const isAlreadyJoined = computed(() => {
  if (user.value && user.value.financial_products) {
    return user.value.financial_products.includes(deposit.value.fin_prdt_cd)
  }
  return false
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
.deposit-container {
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
