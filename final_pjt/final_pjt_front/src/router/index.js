import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CreateView from '@/views/CreateView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'
import UserDetailView from '@/views/UserDetailView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import BankMapView from '@/views/BankMapView.vue'
import UserRecommendView from '@/views/UserRecommendView.vue'
import UserLoanView from '@/views/UserLoanView.vue'
import { useCounterStore } from '@/stores/counter'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/create',
      name: 'create',
      component: CreateView,
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
    {
      path: '/articles/:id',
      name: 'article_detail',
      component: ArticleDetailView,
    },
    {
      path: '/articles',
      name: 'article_list',
      component: ArticlesView,
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView,
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView,
    },
    {
      path: '/deposit/:fin_prdt_cd',
      name: 'deposit_detail',
      component: DepositDetailView,
    },
    {
      path: '/saving/:fin_prdt_cd',
      name: 'saving_detail',
      component: SavingDetailView,
    },
    {
      path: '/user/detail',
      name: 'user_detail',
      component: UserDetailView,
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView,
    },
    {
      path: '/bankmap',
      name: 'bankmap',
      component: BankMapView,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: UserRecommendView,
    },
    {
      path: '/loan',
      name : 'loan',
      component : UserLoanView,
    },
  ],
})
router.beforeEach((to, from, next) => {
  const store = useCounterStore()
  const publicPages = ['login', 'signup', 'home'] // 공개 페이지 리스트
  const authRequired = !publicPages.includes(to.name)

  if (authRequired && !store.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    return next({ name: 'login' })
  }

  next()
})

export default router
