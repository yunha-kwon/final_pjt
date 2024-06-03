<template>
  <v-container class="container-custom">
    <v-card class="shadow-sm" width="100%" >
      <v-toolbar color="primary" dark>
        <v-toolbar-title v-if="article"><h1>{{ article.title }}</h1></v-toolbar-title>        
        <v-btn text :to="{ name: 'ArticleView'}">[BACK]</v-btn>
      </v-toolbar>
      <v-card-text>
        <v-container v-if="article">
          <h1>{{ article.content }}</h1>
          <br><br><br>         
        </v-container>
        <div class="mt-4 d-flex justify-space-between align-center">
          <div>
            <v-btn class="mr-4" color="primary" @click="editArticle">게시글 수정</v-btn>
            <v-btn color="error" @click="confirmDeleteArticle">게시글 삭제</v-btn>
          </div>
        </div>
        <hr>
        <div>
          <h2>댓글</h2>
          <v-list>
            <v-list-item v-for="comment in comments" :key="comment.id">
              <h3>{{ comment.content }} - <strong>{{ comment.username }}</strong></h3>
              <v-list-item-action>
                <v-btn text color="error" @click="confirmDeleteComment(comment.id)">삭제</v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </div>
        <div v-if="isLogin" class="mt-4">
          <form @submit.prevent="submitComment" class="d-flex">
            <v-text-field v-model="newComment" placeholder="댓글을 입력하세요" class="me-2"></v-text-field>
            <v-btn type="submit" color="primary">작성</v-btn>
          </form>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'
import Swal from 'sweetalert2'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const comments = ref([])
const newComment = ref('')
const isLogin = store.isLogin
const router = useRouter()
const currentUser = store.currentUser
const articleUser = ref('')

// 게시글 가져오기
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      article.value = response.data
      articleUser.value = response.data.username
    })
    .catch((error) => {
      console.log(error)
    })

  // 댓글 가져오기
  store.getComments(route.params.id)

  // store.comments가 갱신될 때 comments에 반영
  watch(() => store.comments, (newComments) => {
    comments.value = Array.isArray(newComments) ? newComments : []
  }, { immediate: true })
})

// 게시글 삭제 확인
const confirmDeleteArticle = () => {
  Swal.fire({
    title: "진짠교?",
    text: "Real로 삭제하겠는교?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "하모예!"
  }).then((result) => {
    if (result.isConfirmed) {
      deleteArticle()
    } else {
      Swal.fire(
        '일단은 살려 드릴게',
        '이제 마 안전하오',
        'error'
      )
    }
  })
}

// 게시글 삭제하기
const deleteArticle = () => {
  if(articleUser.value === currentUser) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      }
    })
    .then(() => {
      Swal.fire({
        title: "고마 가뿟다!",
        text: "완즈히 없애뿟다!",
        icon: "success"
      })
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
  } else {
    Swal.fire({
      title: "권한이 없습니다.",
      text: "본인의 게시글만 삭제할 수 있습니다.",
      icon: "error",
      confirmButtonText: "확인"
    });
  }
}

// 게시글 수정 기능 구현
const editArticle = () => {
  // SweetAlert2를 사용하여 수정할 수 있는 모달 창 띄우기
  Swal.fire({
    title: '게시글 수정',
    html:
      `<input id="swal-input1" class="swal2-input" placeholder="제목" value="${article.value.title}">` +
      `<textarea id="swal-input2" class="swal2-textarea" placeholder="내용">${article.value.content}</textarea>`,
    focusConfirm: false,
    showCancelButton: true,
    preConfirm: () => {
      const title = document.getElementById('swal-input1').value;
      const content = document.getElementById('swal-input2').value;
      
      // 현재 사용자가 작성한 게시글인지 확인
      if (article.value.username === currentUser) {
        // 서버로 수정된 게시글 데이터 전송
        axios({
          method: 'put',
          url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
          headers: {
            Authorization: `Token ${store.token}`,
          },
          data: {
            title: title,
            content: content
          }
        })
          .then((response) => {
            Swal.fire({
              title: '게시글이 수정되었습니다.',
              icon: 'success'
            });
            // 수정된 게시글 데이터 업데이트
            article.value.title = title;
            article.value.content = content;
          })
          .catch((error) => {
            console.log(error);
            Swal.fire({
              title: '게시글 수정에 실패하였습니다.',
              icon: 'error'
            });
          });
      } else {
        Swal.fire({
          title: '수정 권한이 없습니다.',
          icon: 'error'
        });
      }
    }
  });
}

// 댓글 작성하기
const submitComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      content: newComment.value
    }
  })
    .then((response) => {
      comments.value.push(response.data);
      newComment.value = '';
    })
    .catch((error) => {
      console.log(error)
    })
  }

// 댓글 수정하기
const editComment = (commentId) => {
  // comments.value가 정의되어 있는지 확인
  if (comments.value) {
    Swal.fire({
      title: '댓글 수정',
      html:
        `<input id="swal-input1" class="swal2-input" placeholder="댓글을 수정하세요" value="${comments.value.find(comment => comment.id === commentId)?.content || ''}">`, // comments.value가 정의되어 있지 않으면 빈 문자열을 출력
      focusConfirm: false,
      showCancelButton: true,
      preConfirm: () => {
        const content = document.getElementById('swal-input1').value;
        
        // 서버로 수정된 댓글 데이터 전송
        axios({
          method: 'put',
          url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/${commentId}/`,
          headers: {
            Authorization: `Token ${store.token}`,
          },
          data: {
            content: content
          }
        })
          .then((response) => {
            Swal.fire({
              title: '댓글이 수정되었습니다.',
              icon: 'success'
            });
            // 수정된 댓글 데이터 업데이트
            const editedCommentIndex = comments.value.findIndex(comment => comment.id === commentId);
            if (editedCommentIndex !== -1) {
              comments.value[editedCommentIndex].content = content;
            }
          })
          .catch((error) => {
            console.log(error);
            Swal.fire({
              title: '댓글 수정에 실패하였습니다.',
              icon: 'error'
            });
          });
      }
    });
  }
}


// 댓글 삭제 확인
const confirmDeleteComment= (commentId) => {
  Swal.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!"
  }).then((result) => {
    if (result.isConfirmed) {
      deleteComment(commentId)
    } else {
      Swal.fire(
        'Cancelled',
        'Your file is safe :)',
        'error'
      )
    }
  })

}

// 댓글 삭제하기
const deleteComment = (commentId) => {  
  const commentToDelete = comments.value.find(comment => comment.id === commentId);

  if (commentToDelete && commentToDelete.username === currentUser) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      }
    })
      .then((response) => {
        Swal.fire({
        title: "Deleted!",
        text: "Your file has been deleted.",
        icon: "success"
      })
        // 삭제 성공 시 해당 댓글을 화면에서도 제거
        comments.value = comments.value.filter(comment => comment.id !== commentId);
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    Swal.fire({
      title: "권한이 없습니다.",
      text: "본인의 댓글만 삭제할 수 있습니다.",
      icon: "error",
      confirmButtonText: "확인"
    });
  }
}
</script>

<style scoped>
.container-custom {
  max-width: 1200px;
  margin: 0 auto;
}
.v-btn {
  font-weight: 500;
}

.v-btn--text {
  text-transform: none;
}

.v-toolbar__title {
  font-size: 24px;
}


</style>