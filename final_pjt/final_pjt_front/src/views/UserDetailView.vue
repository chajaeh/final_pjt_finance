<template>
  <div class="container">
    <div>
      <table class="border">
        <tr class="border-bottom">
          <td class="m-0 text-center table-title" colspan="2">상품 추천</td>
        </tr>
        <tr>
          <td class="border-end table-content" @click="goRecom">예금</td>
          <td class="table-content" @click="goLoan">대출</td>
        </tr>
      </table>
    </div>
    <div class="border-bottom attr">
      <p class="m-1">ID : {{ store.userDetail.username }}</p>
    </div>
    <div class="attr border-bottom">
      <form @submit.prevent="changeAge">
        <label for="age">나이 : </label>
        <input v-model="age" type="number" class="form-control d-inline ms-3 me-2" />
        <button class="btn">변경</button>
      </form>
    </div>
    <div class="attr border-bottom">
      <form @submit.prevent="changeAsset">
        <label for="asset">자산 :</label>
        <input v-model="asset" type="number" class="form-control d-inline ms-3 me-2" />
        <button class="btn">변경</button>
      </form>
    </div>
    <div class="attr border-bottom">
      <form @submit.prevent="changeSalary">
        <label for="salary">연봉 : </label>
        <input v-model="salary" type="number" class="form-control d-inline ms-3 me-2" />
        <button class="btn">변경</button>
      </form>
    </div>
    <div class="attr border-bottom">
      <div v-if="store.financialProducts.length > 0 && store.financialProducts[0] !== ''" class="attr">
        <p>가입한 상품 목록</p>
        <div class="border-bottom mb-3">
          <div v-for="product in store.products" :key="product.id" id="attritem">
            <p>{{ product.fin_prdt_nm }} - {{ product.kor_co_nm }}</p>
          </div>
        </div>
        <h4 class="text-center mb-3">사용자 분석 차트</h4>
        <UserDetailChart v-if="isCompleteFetch" />
      </div>
      <div v-else>
        <p>아직 가입한 상품이 없습니다</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import UserDetailChart from '@/components/UserDetailChart.vue'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink, RouterView, onBeforeRouteLeave, useRouter } from 'vue-router'
import axios from 'axios'

const store = useCounterStore()
const age = ref(null)
const asset = ref(null)
const salary = ref(null)
const router = useRouter()
const isCompleteFetch = ref(false)
onMounted(async () => {
  await store.getUserDetail() // getUserDetail 함수가 완료될 때까지 기다림
  age.value = store.userDetail.age
  asset.value = store.userDetail.asset
  salary.value = store.userDetail.salary
  await store.fetchProductDetails()
  isCompleteFetch.value = true
})

const goRecom = function () {
  router.push({ name: 'recommend' })
}
const goLoan = function () {
  router.push({ name: 'loan' })
}

const changeAge = () => {
  axios({
    method: 'PUT',
    url: `${store.BASE_URL}/account/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { age: age.value },
  })
    .then((res) => {
      store.getUserDetail()
      alert('변경완료')
    })
    .catch((err) => console.log(err))
}

const changeAsset = () => {
  axios({
    method: 'PUT',
    url: `${store.BASE_URL}/account/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { asset: asset.value },
  })
    .then((res) => {
      store.getUserDetail()
      alert('변경완료')
    })
    .catch((err) => console.log(err))
}

const changeSalary = () => {
  axios({
    method: 'PUT',
    url: `${store.BASE_URL}/account/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { salary: salary.value },
  })
    .then((res) => {
      store.getUserDetail()
      alert('변경완료')
    })
    .catch((err) => console.log(err))
}
onBeforeRouteLeave((to, from) => {
  if (
    (to.name === 'recommend' || to.name === 'loan') &&
    (!store.userDetail.age || !store.userDetail.asset || !store.userDetail.salary)
  ) {
    alert('나이와 자산, 연봉을 입력해주세요.')
    return false
  }
})
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
}
.form-control {
  width: 50%;
  border: 1px solid #3f72af;
}
.attr {
  padding: 10px 0px 10px 0px;
}
td {
  width: 50%;
  text-align: center;
}
table {
  width: 22%;
  margin: 0 auto;
}
.table-title {
  font-size: 30px;
}
.table-content {
  font-size: 20px;
  cursor: pointer;
}
</style>
