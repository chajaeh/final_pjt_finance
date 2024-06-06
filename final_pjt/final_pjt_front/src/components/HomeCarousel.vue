<template>
  <div>
    <div id="carouselExampleCaptions" class="carousel slide">
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="@/assets/deposit.jpg"
            class="d-block w-100"
            alt="deposit_image"
            style="width: 100%; height: 700px"
          />
          <div class="carousel-caption d-none d-md-block" @click="goDeposit">
            <h1 class="function-title">예적금 비교</h1>
            <p class="function-description">다양한 예적금 상품을 비교하여 최적의 선택을 도와드립니다.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/exchange.jpg"
            class="d-block w-100"
            alt="exchange_image"
            style="width: 100%; height: 700px"
          />
          <div class="carousel-caption d-none d-md-block" @click="goExchange">
            <h1 class="function-title">환율 계산기</h1>
            <p class="function-description">실시간 환율 정보를 바탕으로 간편하게 환율을 계산해보세요.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/bank.jpg" class="d-block w-100" alt="bank_image" style="width: 100%; height: 700px" />
          <div class="carousel-caption d-none d-md-block" @click="goMap">
            <h1 class="function-title">은행 지도</h1>
            <p class="function-description">가장 가까운 은행 지점을 찾아주는 편리한 은행 지도 서비스입니다.</p>
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goDeposit = function () {
  router.push({ name: 'deposit' })
}
const goExchange = function () {
  router.push({ name: 'exchange' })
}
const goMap = function () {
  router.push({ name: 'bankmap' })
}
</script>

<style scoped>
.function-title {
  font-size: 50px;
  margin-bottom: 15px;
}
.function-description {
  font-size: 20px;
}
.carousel-caption {
  background-color: rgb(0, 0, 0, 0.2);
  height: 300px;
  align-content: center;
  margin-bottom: 180px;
  cursor: pointer;
}
</style>
