<template>
  <div class="search-container">
    <h2>🔍 관심 종목 영상 검색</h2>
    <div class="search-box">
      <input v-model="query" @keyup.enter="searchVideos" placeholder="검색어를 입력하세요" />
      <button @click="searchVideos">검색</button>
    </div>

    <div v-if="videos.length" class="results">
      <h3>📺 검색 결과</h3>
      <div class="video-grid">
        <div class="video-card" v-for="video in videos" :key="video.id.videoId">
          <iframe
            width="100%"
            height="200"
            :src="`https://www.youtube.com/embed/${video.id.videoId}`"
            frameborder="0"
            allowfullscreen
          ></iframe>
          <p>
            <router-link :to="`/detail/${video.id.videoId}`">
              {{ video.snippet.title }}
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const query = ref('')
const videos = ref([])

const searchVideos = async () => {
  if (!query.value.trim()) return

  const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
  const maxResults = 6
  const endpoint = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=${maxResults}&q=${encodeURIComponent(
    query.value
  )}&key=${API_KEY}`

  try {
    const res = await fetch(endpoint)
    const data = await res.json()
    videos.value = data.items
  } catch (error) {
    console.error('영상 검색 실패:', error)
  }
}
</script>

<style scoped>
.search-container {
  max-width: 960px;
  margin: 0 auto;
  text-align: center;
}

.search-box {
  margin: 2rem 0;
}

input {
  padding: 0.6rem;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 0.4rem;
  font-size: 1rem;
}

button {
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 0.4rem;
  margin-left: 0.5rem;
  cursor: pointer;
}

button:hover {
  background-color: #369f6c;
}

.results {
  margin-top: 2rem;
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.video-card {
  border: 1px solid #eee;
  border-radius: 0.5rem;
  padding: 1rem;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.05);
  background-color: #fafafa;
}

.video-card p {
  margin-top: 0.5rem;
  font-weight: bold;
}
</style>
