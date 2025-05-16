<template>
  <div>
    <h2>{{ video.title }}</h2>
    <iframe
      :src="`https://www.youtube.com/embed/${video.videoId}`"
      width="560"
      height="315"
      frameborder="0"
      allowfullscreen
    ></iframe>

    <div>
      <h3>채널명: {{ video.channelTitle }}</h3>
      <button @click="toggleChannel">
        {{ isSaved ? '⭐ 저장 취소' : '⭐ 채널 저장' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const video = ref({
  videoId: route.params.id,
  title: '임시 제목', // YouTube API 결과에 따라 교체
  channelTitle: '임시 채널', // YouTube API 결과에 따라 교체
})

const isSaved = ref(false)

onMounted(() => {
  const saved = JSON.parse(localStorage.getItem('savedChannels') || '[]')
  isSaved.value = saved.includes(video.value.channelTitle)
})

const toggleChannel = () => {
  let saved = JSON.parse(localStorage.getItem('savedChannels') || '[]')
  if (isSaved.value) {
    saved = saved.filter(c => c !== video.value.channelTitle)
  } else {
    saved.push(video.value.channelTitle)
  }
  localStorage.setItem('savedChannels', JSON.stringify(saved))
  isSaved.value = !isSaved.value
}
</script>
