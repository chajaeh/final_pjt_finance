<template>
  <div class="container">
    <h1 class="text-center mb-5">대출 상품 추천</h1>
    <h3>신용조회회사와 신용점수를 입력해주세요</h3>
    <form @submit.prevent="recommendLoan" class="mt-4">
      <div class="d-flex mb-3 search-company">
        <label for="creditAgency" class="me-3">신용조회회사:</label>
        <select id="creditAgency" v-model="creditAgency" class="form-select">
          <option value="KCB">KCB</option>
          <option value="NICE">NICE</option>
        </select>
      </div>
      <div class="d-flex input-box mb-3">
        <label for="creditScore" class="form-label me-3">신용점수:</label>
        <input
          type="number"
          id="creditScore"
          v-model="creditScore"
          min="0"
          max="1000"
          required
          class="form-control"
        />
      </div>
      <button type="submit" class="btn mb-3">추천 대출 보기</button>
      <div class="list-container" v-if="standardProduct || subtractionProducts">
        <div v-if="standardProduct" class="list mb-4">
          <h5>기준금리 기준 추천 상품입니다.</h5>

          <p class="mt-3">
            현재 등급의 금리 {{ standardProduct.interest_current_grade }}, 평균
            금리
            {{ standardProduct.interest_average }}
            <span>{{ standardProduct.company_name }}</span
            >의 상품
            <span class="product-name">{{ standardProduct.product_name }}</span
            >은 어떠신가요?
          </p>
        </div>
        <div v-if="subtractionProducts" class="list">
          <h5>가감조정금리 기준 추천 상품입니다.</h5>
          <p class="text-end infoinfo pb-0">
            * 가감조정금리 : 기존에 거래 관계가 있는 고객에게 은행이 금리를
            낮춰주는 것
          </p>
          <ul class="list-group">
            <li v-for="product in subtractionProducts" class="list-group-item">
              <p>
                이미 <span>{{ product.company_name }}</span
                >의 상품을 가지고 계신가요?
              </p>
              <p class="ms-4">
                현재 등급의 금리 {{ product.interest_current_grade }}, 평균 금리
                {{ product.interest_average }}
                {{ product.company_name }}의 상품
                <span class="product-name">{{ product.product_name }}</span
                >을 추천드립니다.
              </p>
            </li>
          </ul>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
const creditAgency = ref("KCB");
const creditScore = ref(0);
const creditGrade = ref("");
const standardProduct = ref(null);
const subtractionProducts = ref(null);
const recommendLoan = function() {
  switch (true) {
    case creditScore.value <= 300:
      creditGrade.value = "crdt_grad_13";
      break;
    case creditScore.value >= 301 && creditScore.value <= 400:
      creditGrade.value = "crdt_grad_12";
      break;
    case creditScore.value >= 401 && creditScore.value <= 500:
      creditGrade.value = "crdt_grad_11";
      break;
    case creditScore.value >= 501 && creditScore.value <= 600:
      creditGrade.value = "crdt_grad_10";
      break;
    case creditScore.value >= 601 && creditScore.value <= 700:
      creditGrade.value = "crdt_grad_6";
      break;
    case creditScore.value >= 701 && creditScore.value <= 800:
      creditGrade.value = "crdt_grad_5";
      break;
    case creditScore.value >= 801 && creditScore.value <= 900:
      creditGrade.value = "crdt_grad_4";
      break;
    case creditScore.value >= 901:
      creditGrade.value = "crdt_grad_1";
      break;
    default:
      creditGrade.value = "unknown";
      break;
  }
  axios({
    method: "post",
    url: `${store.BASE_URL}/account/recommend_loan/`,
    data: {
      creditAgency: creditAgency.value,
      creditGrade: creditGrade.value
    },
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(res => {
      console.log(res);
      standardProduct.value = res.data.standard;
      subtractionProducts.value = res.data.subtraction;
    })
    .catch(err => {
      console.log(err);
      alert("기준에 맞는 대출 상품이 없습니다!");
    });
};
</script>

<style scoped>
.infoinfo {
  font-size: 12px;
  color: grey;
}
.btn {
  color: white;
  background-color: #3f72af;
}
.form-control {
  width: 20%;
  border: 1px solid #3f72af;
}
.input-box {
  align-items: center;
}
.form-select {
  width: 10%;
  border: 1px solid #3f72af;
}
.search-company {
  align-items: center;
}
.list-container {
  background-color: #112d4e;
  padding: 20px;
  border-radius: 20px;
}
.list {
  background-color: white;
  border-radius: 20px;
  padding: 15px;
}
span {
  font-weight: bold;
}
.product-name {
  font-style: italic;
}
</style>
