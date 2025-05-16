<template>
  <div>
    <h2>🎬 영상 상세 정보</h2>
    <iframe
      width="560"
      height="315"
      :src="`https://www.youtube.com/embed/${videoId}`"
      frameborder="0"
      allowfullscreen
    ></iframe>

    <div style="margin-top: 1rem;">
      <button @click="toggleSave">
        {{ isSaved ? '❌ 저장 취소' : '💾 나중에 보기 저장' }}
      </button>
    </div>

    <div style="margin-top: 1rem;">
      <h3>채널명: {{ channelTitle }}</h3>
      <button @click="toggleChannel">
        {{ isChannelSaved ? '⭐ 저장 취소' : '⭐ 채널 저장' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'

const route = useRoute()
const videoId = route.params.id
const channelTitle = route.query.channel || '알 수 없음'

const isSaved = ref(false)
const isChannelSaved = ref(false)

const STORAGE_KEY = 'watchLater'
const CHANNEL_KEY = 'savedChannels'

const checkSaved = () => {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
  isSaved.value = saved.includes(videoId)
}

const toggleSave = () => {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
  if (isSaved.value) {
    const updated = saved.filter(id => id !== videoId)
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updated))
    isSaved.value = false
  } else {
    saved.push(videoId)
    localStorage.setItem(STORAGE_KEY, JSON.stringify(saved))
    isSaved.value = true
  }
}

const toggleChannel = () => {
  let saved = JSON.parse(localStorage.getItem(CHANNEL_KEY) || '[]')
  if (isChannelSaved.value) {
    saved = saved.filter(c => c !== channelTitle)
  } else {
    saved.push(channelTitle)
  }
  localStorage.setItem(CHANNEL_KEY, JSON.stringify(saved))
  isChannelSaved.value = !isChannelSaved.value
}

onMounted(() => {
  checkSaved()
  const savedChannels = JSON.parse(localStorage.getItem(CHANNEL_KEY) || '[]')
  isChannelSaved.value = savedChannels.includes(channelTitle)
})
</script>
