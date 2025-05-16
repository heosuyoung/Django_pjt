<template>
  <div class="home">
    <h2>📺 관심 종목 영상 검색 서비스에 오신 걸 환영합니다!</h2>
    <p>유튜브에서 관심 있는 키워드를 검색하고<br />나중에 보고 싶은 영상은 따로 저장해두세요.</p>
    <router-link to="/search" class="btn">🔍 지금 검색하러 가기</router-link>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 3rem 1rem;
  background: #f7fcfb;
  border-radius: 1rem;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.home h2 {
  margin-bottom: 1rem;
}

.home p {
  font-size: 1.1rem;
  color: #555;
  line-height: 1.6;
}

.btn {
  margin-top: 2rem;
  display: inline-block;
  background: #42b983;
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 0.5rem;
  text-decoration: none;
  font-size: 1.1rem;
}

.btn:hover {
  background: #369f6c;
}
</style>
