import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore(
  'counter',
  () => {
    const router = useRouter()
    const articles = ref([])
    const deposits = ref([])
    const savings = ref([])
    const BASE_URL = 'http://127.0.0.1:8000'
    const token = ref('')
    const currentUsername = ref(null)
    const isLogin = ref(false)
    const userDetail = ref([])
    const sortKeyDeposit = ref('')
    const sortOrderDeposit = ref(1)
    const selectedBankDeposit = ref('')
    const sortKeySaving = ref('')
    const sortOrderSaving = ref(1)
    const selectedBankSaving = ref('')

    const getArticleList = function () {
      axios({
        method: 'GET',
        url: `${BASE_URL}/api/v1/articles/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          articles.value = res.data
        })
        .catch((err) => console.log(err))
    }

    const getDepositList = function () {
      axios({
        method: 'get',
        url: `${BASE_URL}/api/v1/finance/get_deposit_list/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          deposits.value = res.data.map((deposit) => {
            const updatedDeposit = { ...deposit }
            ;[6, 12, 24, 36].forEach((month) => {
              const option = deposit.depositoptions_set.find((option) => option.save_trm === month)
              if (option) {
                if (option.intr_rate) {
                  updatedDeposit[`intr_rate_${month}`] = option.intr_rate
                } else {
                  updatedDeposit[`intr_rate_${month}`] = option.intr_rate2
                }
              } else {
                updatedDeposit[`intr_rate_${month}`] = '-'
              }
            })
            return updatedDeposit
          })
        })
        .catch((err) => console.log(err))
    }

    const getSavingList = function () {
      axios({
        method: 'get',
        url: `${BASE_URL}/api/v1/finance/get_saving_list/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          savings.value = res.data.map((saving) => {
            const updatedSaving = { ...saving }
            ;[6, 12, 24, 36].forEach((month) => {
              const option = saving.savingoptions_set.find((option) => option.save_trm === month)
              if (option) {
                if (option.intr_rate) {
                  updatedSaving[`intr_rate_${month}`] = option.intr_rate
                } else {
                  updatedSaving[`intr_rate_${month}`] = option.intr_rate2
                }
              } else {
                updatedSaving[`intr_rate_${month}`] = '-'
              }
            })
            return updatedSaving
          })
        })
        .catch((err) => console.log(err))
    }

    const login = function (payload) {
      const { username, password } = payload
      axios({
        method: 'POST',
        url: `${BASE_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key
          isLogin.value = true
          currentUsername.value = username
          getUserDetail()
          router.push({ name: 'home' })
        })
        .catch((err) => alert('아이디와 비밀번호를 확인하세요.'))
    }

    const signUp = function (payload) {
      const { username, password1, password2 } = payload
      axios({
        method: 'POST',
        url: `${BASE_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          const password = password1
          login({ username, password })
        })
        .catch((err) => alert('아이디와 비밀번호를 확인하세요.'))
    }

    const sortedDeposits = computed(() => {
      let filteredDeposits = deposits.value
      if (selectedBankDeposit.value) {
        filteredDeposits = filteredDeposits.filter((deposit) => deposit.kor_co_nm === selectedBankDeposit.value)
      }
      if (!sortKeyDeposit.value) return filteredDeposits
      return filteredDeposits.slice().sort((a, b) => {
        let aValue = a[sortKeyDeposit.value]
        let bValue = b[sortKeyDeposit.value]
        if (aValue === '-') aValue = Number.NEGATIVE_INFINITY
        if (bValue === '-') bValue = Number.NEGATIVE_INFINITY
        aValue = parseFloat(aValue)
        bValue = parseFloat(bValue)
        let result = 0
        if (aValue < bValue) result = -1
        if (aValue > bValue) result = 1
        return result * sortOrderDeposit.value
      })
    })

    const setsortKeyDeposit = (key) => {
      if (sortKeyDeposit.value === key) {
        sortOrderDeposit.value *= -1
      } else {
        sortKeyDeposit.value = key
        sortOrderDeposit.value = 1
      }
    }

    const sortedSavings = computed(() => {
      let filteredSavings = savings.value
      if (selectedBankSaving.value) {
        filteredSavings = filteredSavings.filter((saving) => saving.kor_co_nm === selectedBankSaving.value)
      }
      if (!sortKeySaving.value) return filteredSavings
      return filteredSavings.slice().sort((a, b) => {
        let aValue = a[sortKeySaving.value]
        let bValue = b[sortKeySaving.value]
        if (aValue === '-') aValue = Number.NEGATIVE_INFINITY
        if (bValue === '-') bValue = Number.NEGATIVE_INFINITY
        aValue = parseFloat(aValue)
        bValue = parseFloat(bValue)
        let result = 0
        if (aValue < bValue) result = -1
        if (aValue > bValue) result = 1
        return result * sortOrderSaving.value
      })
    })

    const setsortKeySaving = (key) => {
      if (sortKeySaving.value === key) {
        sortOrderSaving.value *= -1
      } else {
        sortKeySaving.value = key
        sortOrderSaving.value = 1
      }
    }

    const getUserDetail = async () => {
      try {
        const response = await axios({
          method: 'get',
          url: `${BASE_URL}/accounts/user`,
          headers: { Authorization: `Token ${token.value}` },
        })
        userDetail.value = response.data
      } catch (error) {
        console.error('Error fetching user details:', error)
      }
    }
    const financialProducts = computed(() => {
      if (!userDetail.value.financial_products) return []
      return userDetail.value.financial_products.split(',').map((product) => product.trim())
    })
    const products = ref([])
    const fetchProductDetails = async () => {
      products.value = [] // Reset products array
      for (const product of financialProducts.value) {
        try {
          const response = await axios.get(`${BASE_URL}/api/v1/finance/deposit/${product}`, {
            headers: { Authorization: `Token ${token.value}` },
          })
          products.value.push(response.data)
        } catch (error) {
          console.error(`Failed to fetch details for product ${product}:`, error)
        }
      }
    }
    const chartLabel = ref([])
    const averageInterest = ref([])
    const highestInterest = ref([])
    const getChartAttr = async () => {
      chartLabel.value = []
      averageInterest.value = []
      highestInterest.value = []
      products.value.forEach((prod) => {
        chartLabel.value.push(prod.fin_prdt_nm)
        let aver = 0
        let high = 0
        prod.depositoptions_set.forEach((opt) => {
          if (high < opt.intr_rate2) {
            high = opt.intr_rate2
          }
          aver += opt.intr_rate
        })
        aver = aver / prod.depositoptions_set.length
        highestInterest.value.push(high)
        averageInterest.value.push(aver)
      })
      chartLabel.value.push('전체 평균')
      highestInterest.value.push(calAverage(highestInterest.value))
      averageInterest.value.push(calAverage(averageInterest.value))
    }
    function calAverage(array) {
      var sum = 0
      for (var i = 0; i < array.length; i++) sum += array[i]
      return sum / array.length
    }

    return {
      articles,
      getArticleList,
      token,
      BASE_URL,
      login,
      signUp,
      isLogin,
      currentUsername,
      getDepositList,
      getSavingList,
      deposits,
      savings,
      sortedDeposits,
      sortKeyDeposit,
      sortOrderDeposit,
      sortedSavings,
      sortKeySaving,
      sortOrderSaving,
      setsortKeyDeposit,
      setsortKeySaving,
      getUserDetail,
      selectedBankDeposit,
      selectedBankSaving,
      userDetail,
      setselectedBankDeposit: (bank) => {
        selectedBankDeposit.value = bank
      },
      setselectedBankSaving: (bank) => {
        selectedBankSaving.value = bank
      },
      financialProducts,
      fetchProductDetails,
      products,
      getChartAttr,
      chartLabel,
      averageInterest,
      highestInterest,
    }
  },
  { persist: true }
)
