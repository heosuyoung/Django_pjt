<template>
  <div>
    <header>
      <h1>📺 관심 종목 영상 검색 서비스</h1>
      <nav>
        <router-link to="/">🏠 홈</router-link> |
        <router-link to="/search">🔍 검색</router-link> |
        <router-link to="/watch-later">⭐ 나중에 볼 영상</router-link>
        <RouterLink to="/channels">⭐ 좋아하는 채널</RouterLink>

      </nav>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
header {
  padding: 1rem;
  background-color: #42b983;
  color: white;
  text-align: center;
}

nav {
  margin-top: 0.5rem;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

main {
  padding: 2rem;
}
</style>
