<template>
  <ul class="list-group">
    <li class="list-group-item d-flex justify-content-between">
      <div v-if="!update" class="comment-part d-flex">
        <div class="username-part">{{ comment.user.username }}</div>
        <div class="content-part">{{ comment.content }}</div>
        <div class="update-time">{{ formattedDate(comment.created_at) }}</div>
        <div
          v-if="comment.user.username === store.currentUsername"
          class="button-box"
        >
          <button @click="update = !update" class="btn">수정</button>
          <button
            @click="deleteComment(comment.id)"
            class="btn"
            id="delete-button"
          >
            삭제
          </button>
        </div>
      </div>
      <form
        v-if="update"
        @submit.prevent="updateComment(comment.id)"
        class="comment-part d-flex justify-content-between"
      >
        <input type="text" v-model.trim="newComment" class="form-control" />
        <button class="btn me-4">댓글 수정</button>
      </form>
    </li>
  </ul>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();
const route = useRoute();
const update = ref(false);
const router = useRouter();

const props = defineProps({
  comment: Object,
  fwords: Array
});
const newComment = ref(`${props.comment.content}`);
const emit = defineEmits(["deleteCom, updateCom"]);
const deleteComment = function(commentId) {
  axios({
    method: "DELETE",
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}/comments/${commentId}/`,
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(res => {
      emit("deleteCom", commentId);
    })
    .catch(err => console.log(err));
};
const updateComment = function(commentId) {
  let flag = false;
  const replaceValue = "**";
  const temContent = newComment.value
    .split(" ")
    .map(item => item.trim())
    .filter(item => item);

  temContent.forEach((ele, idx) => {
    props.fwords.forEach(e => {
      if (ele.includes(e)) {
        temContent[idx] = replaceValue;
        flag = true;
        return;
      }
    });
  });
  const finalContent = temContent.join(" ");
  if (flag == true) {
    warn();
  }
  axios({
    method: "PUT",
    url: `${store.BASE_URL}/api/v1/articles/${route.params.id}/comments/${commentId}/`,
    headers: { Authorization: `Token ${store.token}` },
    data: { content: finalContent }
  })
    .then(res => {
      const newCom = finalContent;
      emit("updateCom", commentId, newCom);
      update.value = !update.value;
      newComment.value = newCom;
    })
    .catch(err => console.log(err));
};
const warn = function() {
  axios({
    method: "post",
    url: `${store.BASE_URL}/account/warn/`,
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(res => {
      if (res.data.warn >= 3) {
        alert(`욕설 누적 ${res.data.warn}회 누적으로 이용이 제한됩니다.`);
        warnSignout();
        axios({
          method: "post",
          url: `${store.BASE_URL}/accounts/logout/`
        })
          .then(res => {
            store.token = null;
            store.isLogin = false;
            store.currentUsername = null;
            router.push({ name: "home" });
          })
          .catch(err => {
            console.log(err);
          });
      } else {
        alert(
          `현재 욕설 누적 ${res.data.warn}회입니다.\n3회 누적될 경우 이용이 제한될 수 있습니다.`
        );
      }
    })
    .catch(err => {
      console.log(err);
    });
};
const warnSignout = function() {
  axios({
    method: "post",
    url: `${store.BASE_URL}/account/warn_signout/`,
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(res => {
      console.log(res);
    })
    .catch(err => {
      console.log(err);
    });
};
const formattedDate = dat => {
  const date = new Date(dat);
  return new Intl.DateTimeFormat("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false
  }).format(date);
};
</script>

<style scoped>
.btn {
  color: white;
  background-color: #3f72af;
  margin-right: 10px;
}
#delete-button {
  background-color: rgba(255, 0, 0, 0.661);
}
.comment-part {
  width: 100%;
  align-items: center;
  height: 30px;
}
.input-box {
  justify-content: space-between;
  width: 60%;
}
.form-control {
  width: 70%;
}
.username-part {
  width: 15%;
}
.content-part {
  width: 40%;
}
.update-time {
  width: 20%;
  font-size: 13px;
}
.button-box {
  margin-left: auto;
}
</style>
