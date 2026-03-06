<template>
  <nav class="navbar">
    <div class="container">
      <!-- Логотип -->
      <div class="logo">Транскрибатор</div>

      <!-- Навигация -->
      <div class="nav-links">
        <a href="#" class="nav-item active">Главная</a>
        <a href="#" class="nav-item">API</a>
        <a href="#" class="nav-item">Документация</a>
        <a href="#" class="nav-item">Поддержка</a>
        <a href="#" class="nav-item">О разработчике</a>
      </div>

      <!-- Кнопка входа -->
      <button class="login-btn">Войти</button>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  width: 100%;
  height: 70px;
  background-color: #ffffff;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  align-items: center;
  position: fixed; /* Хедер будет закреплен сверху */
  top: 0;
  left: 0;
  z-index: 1000;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.logo {
  font-size: 1.2rem;
  font-weight: 700;
  color: #1a202c;
}

.nav-links {
  display: flex;
  gap: 25px;
}

.nav-item {
  text-decoration: none;
  color: #718096;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-item:hover {
  color: #1a202c;
}

.nav-item.active {
  color: #1a202c;
  font-weight: 600;
}

.login-btn {
  background-color: #0a0a0f; /* Очень темный синий/черный */
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.2s;
}

.login-btn:hover {
  opacity: 0.9;
}
</style>
