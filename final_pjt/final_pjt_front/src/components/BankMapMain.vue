<template>
  <div class="map">
    <div id="map"></div>
    <button @click="changeOption()" v-if="mapMove" class="comeback-button">돌아가기</button>
    <button @click="reSearch()" v-if="mapMove" class="current-button">
      <img src="@/assets/refresh.png" alt="refresh" class="refresh-img" /> 현 지도에서 검색
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  location: Object,
  brand: String,
})

const mapMove = ref(false)
const clevel = ref(null)
const lat = ref(null)
const lng = ref(null)
let map = null
let ps = null
let markers = [] // 현재 지도에 표시된 마커를 추적하기 위한 배열
let currentInfowindow = null // 현재 열려 있는 인포윈도우를 추적하기 위한 변수

const loadKakaoMapScript = () => {
  return new Promise((resolve, reject) => {
    if (typeof kakao !== 'undefined') {
      resolve()
      return
    }

    const script = document.createElement('script')
    script.src = '//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_APP_KEY&libraries=services'
    script.onload = resolve
    script.onerror = reject
    document.head.appendChild(script)
  })
}

const initializeMap = () => {
  const mapContainer = document.getElementById('map')
  const mapOption = {
    center: new kakao.maps.LatLng(37.4998496, 127.0366601),
    level: 4,
  }

  map = new kakao.maps.Map(mapContainer, mapOption)
  ps = new kakao.maps.services.Places(map)
}

const clearOverlays = () => {
  markers.forEach((marker) => marker.setMap(null))
  markers = []
  if (currentInfowindow) {
    currentInfowindow.close()
    currentInfowindow = null
  }
}

onMounted(async () => {
  await loadKakaoMapScript()
  initializeMap()
})

const changeOption = () => {
  mapMove.value = false

  if (map && props.location) {
    const mapOption = {
      center: new kakao.maps.LatLng(props.location.x, props.location.y),
      level: props.location.level,
    }

    map.setCenter(mapOption.center)
    map.setLevel(mapOption.level)

    clearOverlays()
    ps.keywordSearch(props.brand, placesSearchCB, { useMapBounds: true })

    kakao.maps.event.addListener(map, 'center_changed', () => {
      mapMove.value = true
      clevel.value = map.getLevel()
      const latlng = map.getCenter()
      lat.value = latlng.getLat()
      lng.value = latlng.getLng()
    })
  }
}

const reSearch = () => {
  mapMove.value = false

  if (map && lat.value && lng.value) {
    const mapOption = {
      center: new kakao.maps.LatLng(lat.value, lng.value),
      level: clevel.value,
    }

    map.setCenter(mapOption.center)
    map.setLevel(mapOption.level)

    clearOverlays()
    ps.keywordSearch(props.brand, placesSearchCB, { useMapBounds: true })

    kakao.maps.event.addListener(map, 'center_changed', () => {
      mapMove.value = true
      clevel.value = map.getLevel()
      const latlng = map.getCenter()
      lat.value = latlng.getLat()
      lng.value = latlng.getLng()
    })
  }
}

const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    clearOverlays()

    for (let i = 0; i < data.length; i++) {
      displayMarker(data[i])
    }
  }
}

const displayMarker = (place) => {
  const isBank =
    !place.place_name.includes('365') && place.category_group_code === 'BK9' && !place.place_name.includes('ATM')
  const isPostOffice =
    props.brand === '우체국' && !place.place_name.includes('주차장') && !place.place_name.includes('우편취급국')
  const isCreditUnion =
    props.brand === '신협' &&
    !place.place_name.includes('ATM') &&
    !place.place_name.includes('365') &&
    !place.place_name.includes('주차장') &&
    place.category_group_code !== 'CS2'

  if (isBank || isPostOffice || isCreditUnion) {
    const marker = new kakao.maps.Marker({
      map,
      position: new kakao.maps.LatLng(place.y, place.x),
    })

    markers.push(marker)

    const infowindow = new kakao.maps.InfoWindow({
      content: '<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>',
    })

    kakao.maps.event.addListener(marker, 'click', () => {
      if (currentInfowindow) {
        currentInfowindow.close()
      }
      infowindow.open(map, marker)
      currentInfowindow = infowindow
    })
  }
}

watch(
  () => props.location,
  () => {
    changeOption()
  }
)

watch(
  () => props.brand,
  () => {
    changeOption()
  }
)
</script>

<style scoped>
#map {
  width: 100%;
  height: 100%;
  border: 1px solid #3f72af;
  position: relative;
}
.map {
  width: 80%;
  position: relative;
}
.btn {
  color: white;
  background-color: #3f72af;
}
.current-button {
  position: absolute;
  top: 2%;
  left: 50%;
  z-index: 5;
  background-color: white;
  border-radius: 7px;
  border: 0.5px solid #3f72af;
  font-size: 13px;
}
.refresh-img {
  width: 15px;
  z-index: 10;
}
.comeback-button {
  position: absolute;
  top: 2%;
  left: 37%;
  z-index: 5;
  background-color: white;
  border-radius: 7px;
  border: 0.5px solid #3f72af;
  font-size: 13px;
}
</style>
