<template>
  <div>
    <img src="../assets/align.png" alt="1" v-if="!selected" />
    <img src="../assets/align1.png" alt="2" v-else-if="aord" />
    <img src="../assets/align2.png" alt="3" v-else />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
const props = defineProps({
  id: String,
  choice: String,
  click: Boolean,
})
const selected = ref(false)
const aord = ref(true)
watch(
  () => props.click,
  () => {
    if (props.id === props.choice) {
      console.log(props.choice)
      if (selected.value) {
        aord.value = !aord.value
      } else {
        selected.value = true
      }
    } else {
      selected.value = false
      aord.value = true
    }
  }
)
</script>

<style scoped>
img {
  width: 12px;
  cursor: pointer;
}
</style>
