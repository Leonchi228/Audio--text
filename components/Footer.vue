<template>
  <footer class="site-footer">
    <div class="footer-content">
      <p>&copy; 2024 WhisperText — Транскрибация аудио</p>
      <div class="footer-links">
        <a href="PrivacyPolicy.vue" class="footer-link">Политика конфиденциальности</a>
        <span class="divider">|</span>
        <a href="mailto:uchihahiro228@gmail.com" class="footer-link">Поддержка</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  margin-top: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-top: 1px solid #eee;
  text-align: center;
  font-family: sans-serif;
}
.footer-content p {
  margin: 0;
  color: #666;
  font-size: 14px;
}
.footer-links {
  margin-top: 10px;
}
.footer-link {
  color: #42b983;
  text-decoration: none;
  font-size: 14px;
}
.footer-link:hover {
  text-decoration: underline;
}
.divider {
  margin: 0 10px;
  color: #ccc;
}
</style>