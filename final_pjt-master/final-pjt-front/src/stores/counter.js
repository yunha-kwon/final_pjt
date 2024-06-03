import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const comments = ref([])
  const products = ref([])
  const options = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  const currentUser = ref(null)
  const currentEmail = ref(null)
  const currentBirth = ref(null)
  const saveproducts = ref([])
  const saveoptions= ref([])
  const storedProduct = ref([])

  const updateStoredProduct = (product) => {
    console.log(storedProduct)
    storedProduct.value.push(product)
  }

  const clear = () => {
    token.value = ''
  }

  const isLogin = computed(() => !!token.value)

  const getArticles = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.error(error)
      })
  }

  const getComments = (articleId) => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${articleId}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        comments.value = response.data
           
      })
      .catch(error => {
        console.error(error)
      })
  }

  // 예금 상품
  const getDepositProduct = () => {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/deposit-products/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        products.value = response.data
        
      })
      .catch(error => {
        console.error(error)
      })
  }

  const getDepositProductOption = (fin_prdt_cd) => {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/deposit-product-options/${fin_prdt_cd}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        options.value = response.data
      })
      .catch(error => {
        console.error(error)
      })
  }

  const getSaveProduct = () => {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/save-products/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        saveproducts.value = response.data
        
      })
      .catch(error => {
        console.error(error)
      })
  }
  // 적금 상품
  const getSaveProductOption = (fin_prdt_cd) => {
    axios({
      method: 'get',
      url: `${API_URL}/finlife/save-product-options/${fin_prdt_cd}/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then(response => {
        saveoptions.value = response.data
      })
      .catch(error => {
        console.error(error)
      })
  }
  const signUp = (payload) => {
    const { username, birth, email, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        birth,
        email,
        password1,
        password2,
      },
    })
      .then((res) => {
        const password = password1
        logIn({ username,  password })
        
      })
      .catch((err) => {
        console.error(err)
      })
  }

  const logIn = (payload) => {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      },
    })
      .then((res) => {
        token.value = res.data.key
        currentUser.value = res.data.user.username
        currentBirth.value = res.data.user.birth
        currentEmail.value = res.data.user.email
        router.push({ name: 'HomeView' })
        console.log('로그인이 완료되었습니다'
        )
        Swal.fire({
          position: "center",
          icon: "success",
          title: `환영합니다 ${currentUser.value}님!`,
          showConfirmButton: false,
          timer: 1500
        });
      })
      .catch((err) => {
        console.error(err)
      })
  }

  return {
    articles,
    API_URL,
    getArticles,
    getComments,
    getDepositProduct,
    signUp,
    logIn,
    token,
    isLogin,
    clear,
    comments,
    products,
    getDepositProductOption,
    options,
    currentUser,
    currentEmail,
    currentBirth,
    getSaveProduct,
    getSaveProductOption,
    saveproducts,
    saveoptions,
    storedProduct,
    updateStoredProduct

  }
}, { persist: true })
