<template>
  <div>
    <HomeCarousel />
    <HomeItem />
  </div>
</template>

<script setup>
import HomeCarousel from '@/components/HomeCarousel.vue'
import HomeItem from '@/components/HomeItem.vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>

<style scoped></style>
