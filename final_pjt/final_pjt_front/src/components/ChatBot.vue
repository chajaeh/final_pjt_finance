<template>
  <div class="information" v-if="hover || clicked">
    레꼬에게 예금 상품들에 대한 질문을 해보세요! 예를 들어 모든 예금 상품들 중 금리가 가장 높은 상품을 추천해 줘 라고
    물어보면 레꼬가 친절하게 대답해 줄거에요!
  </div>
  <section class="container" v-show="select">
    <div class="d-flex button-container">
      <b-button
        id="button-1"
        class="tooltip-button"
        variant="outline-primary"
        @mouseover="over"
        @mouseout="over"
        @click="clickclick"
        >!</b-button
      >
      <b-button id="button-2" class="tooltip-button" variant="outline-primary" @click="cancel">x</b-button>
    </div>

    <!-- 프로필 영역 -->
    <div class="top-area">
      <div class="profile-area">
        <span>우리들의 친구 레꼬🐱</span>
      </div>
    </div>
    <!-- 채팅 영역 -->
    <div class="chat-area">
      <div v-for="(chat, index) in chats" :key="index" :class="chat.class">
        {{ chat.message }}
      </div>
      <div ref="bottomOfChat" />
    </div>

    <!-- 채팅창 하단 영역 -->
    <form class="bottom-area" @submit.prevent="chatbotCommand">
      <input class="chat-input" type="text" placeholder="레꼬에게 말을 건네보세요!" v-model="command" />
    </form>
  </section>
  <img src="@/assets/chatbotchar.png" alt="cat" class="cat-image" @click="selected" />
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { onMounted, ref, nextTick } from 'vue' // nextTick 추가

const store = useCounterStore()
const command = ref('')
const chats = ref([])
const select = ref(false)
const hover = ref(false)
const clicked = ref(false)

const cancel = function () {
  select.value = false
  clicked.value = false
}

const selected = function () {
  if (select.value == true && clicked.value == true) {
    select.value = false
    clicked.value = false
  } else {
    select.value = !select.value
  }
}

const over = function () {
  hover.value = !hover.value
}

const clickclick = function () {
  clicked.value = !clicked.value
}

const addChat = (message, type) => {
  const chatClass = type === 'send' ? 'send-chat' : 'receive-chat'
  chats.value.push({ message, class: `chat ${chatClass}` })
  scrollToBottom() // 메시지 추가 후 스크롤 조정
}

const chatbotCommand = () => {
  if (!command.value.trim()) return

  // Add user chat to the chat area
  addChat(command.value, 'send')
  const temp = command.value
  command.value = ''
  axios({
    method: 'POST',
    url: `${store.BASE_URL}/api/v1/finance/chatbot/usercommand/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { command: temp },
  })
    .then((res) => {
      // Add bot response to the chat area
      addChat(res.data.response, 'receive')
    })
    .catch((err) => alert('오류발생!'))
}

// ref 추가
const bottomOfChat = ref(null)

// scrollToBottom 함수 추가
const scrollToBottom = () => {
  nextTick(() => {
    bottomOfChat.value?.scrollIntoView({ behavior: 'smooth' })
  })
}

// 챗봇을 켰을 때 context를 초기화하기 위한 코드
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/finance/chatbot/`,
    headers: { Authorization: `Token ${store.token}` },
  }).catch((err) => console.log(err))
})
</script>

<style scoped>
#button-1 {
  margin-right: 7px;
}
.button-container {
  align-self: flex-end;
}
.tooltip-button {
  align-self: flex-end;
  font-size: 10px;
  font-weight: bold;
  padding: 0 5px;
  border-radius: 100%;
  margin-top: 6px;
  margin-right: 12px;
  position: relative;
}
.information {
  position: fixed;
  right: 2%;
  top: 9%;
  background-color: white;
  padding: 5px;
  border: 1px solid rgb(191, 191, 191);
  border-radius: 10px;
  z-index: 2000;
  font-size: 10px;
}
.cat-image {
  position: fixed;
  z-index: 5;
  width: 110px;
  bottom: 5%;
  right: 2%;
  cursor: pointer;
}

.chat-area {
  width: 100%;
  display: flex;
  flex: 1;
  padding: 10px;
  box-sizing: border-box;
  flex-direction: column;
  overflow-y: scroll;
}

.top-area {
  margin-top: 5px;
  width: 100%;
  height: 35px;
}
.chat {
  border-radius: 30px;
  padding: 5px 15px;
  box-sizing: border-box;
  color: var(--color-white);
  width: fit-content;
  max-width: 70%;
  height: fit-content;
  word-break: break-all;
  margin: 5px 0;
}

.send-chat {
  align-self: flex-end;
  background-color: #d1e7dd;
}
.receive-chat {
  background-color: #f8d7da;
}

.chat-input {
  width: 100%;
  border: none;
  font-size: 16px;
  border-radius: 15px;
  background-color: white;
}

.chat-input:focus {
  outline: none;
}

.container {
  width: 30%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 30px;
  box-shadow: 0px 1px 3px rgba(0, 0, 0);
  position: fixed;
  bottom: 17%;
  right: 5%;
  background-color: #eef2fa;
  z-index: 1500;
}

.profile-area {
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
  background-color: white;
  border-radius: 15px;
  height: 100%;
}

.profile-area > span {
  font-size: 20px;
  font-weight: semi-bold;
  text-align: center;
}

.bottom-area {
  width: 100%;
  height: 13%;
  display: flex;
  padding: 10px 20px;
  box-sizing: border-box;
}

.tool-area {
  display: flex;
  align-items: center;
}
</style>
