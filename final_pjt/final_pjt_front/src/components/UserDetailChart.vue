<template>
  <div>
    <div class="chart-container">
      <canvas ref="MyChart" v-show="isCompleted" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const store = useCounterStore()
const MyChart = ref(null)
const isCompleted = ref(false)

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: '평균 금리',
      data: [],
      backgroundColor: 'rgba(54, 162, 235, 0.5)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
    },
    {
      label: '최고 우대 금리',
      data: [],
      backgroundColor: 'rgba(255, 206, 86, 0.5)',
      borderColor: 'rgba(255, 206, 86, 1)',
      borderWidth: 1,
    },
  ],
})

const chartOptions = {
  scales: {
    y: {
      beginAtZero: true,
    },
  },
}

const createChart = () => {
  if (MyChart.value) {
    new Chart(MyChart.value, {
      type: 'bar',
      data: chartData.value,
      options: chartOptions,
    })
  }
}

onMounted(async () => {
  await store.getChartAttr()
  chartData.value.labels = store.chartLabel
  chartData.value.datasets[0].data = store.averageInterest
  chartData.value.datasets[1].data = store.highestInterest
  createChart()
  isCompleted.value = true

  // Update chart data with values from store
})
</script>

<style scoped>
.chart-container {
  width: 60%;
  margin: 5px auto;
}
</style>
