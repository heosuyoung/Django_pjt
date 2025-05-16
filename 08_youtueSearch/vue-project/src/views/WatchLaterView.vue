<template>
  <div>
    <h2>📂 나중에 볼 영상 목록</h2>

    <div v-if="videoIds.length">
      <ul>
        <li v-for="id in videoIds" :key="id">
          <iframe
            width="300"
            height="200"
            :src="`https://www.youtube.com/embed/${id}`"
            frameborder="0"
            allowfullscreen
          ></iframe>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>저장된 영상이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const STORAGE_KEY = 'watchLater'
const videoIds = ref([])

onMounted(() => {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
  videoIds.value = saved
})
</script>

<style scoped>
iframe {
  margin-bottom: 1rem;
}
</style>
