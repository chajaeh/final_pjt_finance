<template>
  <div class="item-container d-flex">
    <img src="@/assets/home.png" alt="item_img" />
    <div class="p-container">
      <p>ReccoMate는 다양한 금융 서비스를 제공하는 혁신적인 웹사이트입니다.</p>
      <p>예금 및 적금 상품을 쉽게 열람하고, 환율 계산기를 이용해 실시간 환율 정보를 확인할 수 있습니다.</p>
      <p>
        주변 은행 찾기 기능을 통해 가까운 은행을 손쉽게 찾을 수 있으며, 사용자 간의 소통을 위한 게시판도 마련되어
        있습니다.
      </p>
      <p>
        특히, 알고리즘 기반의 개인 맞춤형 예금 상품 추천 기능과 AI 챗봇을 통해 더욱 스마트한 금융 상품 선택을
        지원합니다.
      </p>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.item-container {
  background-color: #f8f8f8;
  height: 300px;
  width: 50%;
  border: 1px solid rgb(178, 178, 178);
  margin: 30px auto;
}
img {
  width: 300px;
  border-right: 1px solid rgb(178, 178, 178);
}
.p-container {
  padding: 10px;
}
p {
  font-size: 14px;
}
</style>
