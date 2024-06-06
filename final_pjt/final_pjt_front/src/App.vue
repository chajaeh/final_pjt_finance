<template>
  <div class="mainBox">
    <Header />
    <ChatBot />
    <RouterView />
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import ChatBot from '@/components/ChatBot.vue'
</script>

<style scoped>
.mainBox {
  background-color: #fdfdfd;
}
</style>
