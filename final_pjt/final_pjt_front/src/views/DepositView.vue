<template>
  <div class="container">
    <h1 class="text-center mb-5">예금 비교</h1>
    <RouterLink to="/deposit" class="link fw-bold">예금</RouterLink> <span class="link"> | </span>
    <RouterLink to="/saving" class="link">적금</RouterLink>
    <RouterView />
    <form @submit.prevent="filterBank" class="d-flex justify-content-center">
      <select class="form-select" aria-label="Default select example" v-model="selectedBankDeposit">
        <option value="">전체</option>
        <option value="우리은행">우리은행</option>
        <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
        <option value="대구은행">대구은행</option>
        <option value="부산은행">부산은행</option>
        <option value="광주은행">광주은행</option>
        <option value="제주은행">제주은행</option>
        <option value="전북은행">전북은행</option>
        <option value="경남은행">경남은행</option>
        <option value="중소기업은행">중소기업은행</option>
        <option value="한국산업은행">한국산업은행</option>
        <option value="국민은행">국민은행</option>
        <option value="신한은행">신한은행</option>
        <option value="농협은행주식회사">농협은행주식회사</option>
        <option value="하나은행">하나은행</option>
        <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
        <option value="수협은행">수협은행</option>
        <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
        <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
      </select>
      <button type="submit" class="btn ms-3">검색</button>
    </form>
    <div class="table-container m-3">
      <table class="table table-hover">
        <thead class="table-head">
          <tr>
            <th scope="col" class="big-th">회사 명</th>
            <th scope="col" class="big-th">상품 명</th>
            <th scope="col" class="big-th">
              <div class="d-flex" @click="setsortKeyDeposit('intr_rate_6'), choose('1')">
                <th>6개월</th>
                <AlignButton id="1" :id="id" :choice="choice" :click="click" />
              </div>
            </th>
            <th scope="col" class="big-th">
              <div class="d-flex" @click="setsortKeyDeposit('intr_rate_12'), choose('2')">
                <th>12개월</th>
                <AlignButton id="2" :id="id" :choice="choice" :click="click" />
              </div>
            </th>
            <th scope="col" class="big-th">
              <div class="d-flex" @click="setsortKeyDeposit('intr_rate_24'), choose('3')">
                <th>24개월</th>
                <AlignButton id="3" :id="id" :choice="choice" :click="click" />
              </div>
            </th>
            <th scope="col" class="big-th" id="finish-th">
              <div class="d-flex" @click="setsortKeyDeposit('intr_rate_36'), choose('4')">
                <th>36개월</th>
                <AlignButton id="4" :id="id" :choice="choice" :click="click" />
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="deposit in store.sortedDeposits" :key="deposit.id" @click="goDepositDetail(deposit.fin_prdt_cd)">
            <td>{{ deposit.kor_co_nm }}</td>
            <td>{{ deposit.fin_prdt_nm }}</td>
            <td>{{ deposit.intr_rate_6 }}</td>
            <td>{{ deposit.intr_rate_12 }}</td>
            <td>{{ deposit.intr_rate_24 }}</td>
            <td>{{ deposit.intr_rate_36 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import AlignButton from '@/components/AlignButton.vue'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useCounterStore()
const selectedBankDeposit = ref('')
const choice = ref('0')
const click = ref(false)
const goDepositDetail = function (fin_prdt_cd) {
  router.push({ name: 'deposit_detail', params: { fin_prdt_cd } })
}
onMounted(() => {
  store.getDepositList()
})
const { setselectedBankDeposit, setsortKeyDeposit } = store
const filterBank = () => {
  setselectedBankDeposit(selectedBankDeposit.value)
}
const choose = function (n) {
  click.value = !click.value
  choice.value = n
}
</script>

<style scoped>
table th {
  cursor: pointer;
}
.btn {
  color: white;
  background-color: #3f72af;
  width: 7%;
}
.form-select {
  width: 70%;
  border: 1px solid #3f72af;
}
.link {
  text-decoration: none;
  color: #112d4e;
  font-size: 20px;
}
.big-th {
  background-color: #f1f6ff;
}
#finish-th {
  border: none;
}
table tr {
  cursor: pointer;
}
</style>
