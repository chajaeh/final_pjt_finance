<template>
  <div v-if="rate" class="p-5">
    <div class="d-flex justify-content-center">
      <div class="header-container">
        <select name="exchangeRate" id="exchangeRate" v-model="nation" @change="korToFor" class="form-select me-5">
          <option selected :value="rate[0].tts" :key="rate[0].cur_nm">{{ rate[0].cur_nm }}</option>
          <option v-for="item in rate.slice(1)" :key="item.cur_nm" :value="item.tts">
            {{ item.cur_nm }}
          </option>
        </select>
        <div class="form-control" id="won">한국 원</div>
      </div>
      <div class="input-container d-flex flex-wrap">
        <input type="number" v-model="foreign" @input="forToKor" class="form-control" />
        <br />
        <input type="number" v-model="won" @input="korToFor" class="form-control" />
        <br />
      </div>
    </div>
    <p class="text-center m-0">* 엔화 / 인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
  rate: {
    type: Array,
  },
})
const nation = ref(props.rate[0].tts)
const foreign = ref(0)
const won = ref(0)

const korToFor = function () {
  const exchangeRate = nation.value.split(',').join('')
  foreign.value = (won.value / exchangeRate).toFixed(2)
}
const forToKor = function () {
  console.log(nation.value)
  const exchangeRate = nation.value.split(',').join('')
  won.value = Math.round(parseFloat(foreign.value) * exchangeRate)
}
</script>

<style scoped>
.input-container {
  width: 50%;
}
.form-select {
  width: 85%;
  height: 50px;
  margin-bottom: 50px;
  border: 1px solid #3f72af;
}
.form-control {
  height: 50px;
  margin-bottom: 50px;
  width: 100%;
  border: 1px solid #3f72af;
}
#won {
  width: 85%;
  align-content: center;
  border: 1px solid #3f72af;
}
</style>
