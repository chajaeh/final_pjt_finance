<template>
  <div class="container">
    <h1 class="text-center mb-5">가까운 은행 찾기</h1>
    <div class="map-container d-flex justify-content-between">
      <BankMapNavBar @set-location="setLocation" class="nav" />

      <BankMapMain :location="location" :brand="brand" class="map" />
    </div>
  </div>
</template>

<script setup>
import BankMapMain from '@/components/BankMapMain.vue'
import BankMapNavBar from '@/components/BankMapNavBar.vue'
import { ref } from 'vue'
const location = ref(null)
const brand = ref(null)
const setLocation = function (lo, b) {
  location.value = lo
  brand.value = b
}
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 700px;
  background-color: #dbe2ef;
  padding: 30px;
  margin-bottom: 20px;
}
</style>
