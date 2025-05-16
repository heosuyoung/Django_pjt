<template>
  <div>
    <h2>⭐ 저장한 채널 목록</h2>
    <ul>
      <li v-for="channel in channels" :key="channel">
        {{ channel }}
      </li>
    </ul>
    <p v-if="channels.length === 0">저장된 채널이 없습니다.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const channels = ref([])

onMounted(() => {
  channels.value = JSON.parse(localStorage.getItem('savedChannels') || '[]')
})
</script>
