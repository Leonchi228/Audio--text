<template>
  <div class="privacy-page">
    <header class="header">
      <router-link to="/" class="back-btn">← На главную</router-link>
      <h1>Политика конфиденциальности</h1>
    </header>

    <div class="policy-body">
      <section>
        <h2>1. Обработка аудиофайлов</h2>
        <p>Наш сервис использует нейросеть Whisper для преобразования аудио в текст. Все загруженные файлы обрабатываются «на лету» и <strong>удаляются немедленно</strong> после завершения транскрибации. Мы не храним ваши аудиозаписи на наших серверах.</p>
      </section>

      <section>
        <h2>2. Персональные данные</h2>
        <p>Мы не требуем регистрации и не собираем ваши личные данные: имена, адреса или номера телефонов. Информация из ваших аудиофайлов не передается третьим лицам.</p>
      </section>

      <section>
        <h2>3. Рекламные блоки</h2>
        <p>На сайте могут отображаться объявления Рекламной сети Яндекса. Эти сети могут использовать файлы cookie и анонимные данные для показа наиболее подходящей вам рекламы.</p>
      </section>
    </div>
  </div>
</template>

<style scoped>
.privacy-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
  line-height: 1.6;
  color: #333;
}
.header {
  margin-bottom: 30px;
  border-bottom: 2px solid #42b983;
  padding-bottom: 15px;
}
.back-btn {
  color: #42b983;
  text-decoration: none;
  font-weight: bold;
}
h1 { margin-top: 10px; color: #2c3e50; }
h2 { margin-top: 25px; color: #34495e; font-size: 20px; }
p { margin-bottom: 15px; }
</style>
