<template>
  <div>
    <ArticleDetailCommentItemElement
      v-for="comment in comments"
      :keys="comment.id"
      :comment="comment"
      :fwords="fwords"
      @deleteCom="deleteCom"
      @updateCom="updateCom"
    />
  </div>
</template>

<script setup>
import ArticleDetailCommentItemElement from '@/components/ArticleDetailCommentItemElement.vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
const route = useRoute()
defineProps({
  comments: Array,
  fwords: Array,
})
const emit = defineEmits(['deleteCom, updateCom'])
const deleteCom = function (commentId) {
  emit('deleteCom', commentId)
}
const updateCom = function (commentId, newCom) {
  emit('updateCom', commentId, newCom)
}
</script>

<style scoped></style>
