// docs/extra_config/tts.js
console.log("TTS script loaded!"); // 添加这一行来确认加载

function speakFrench(text) {
  const url = `https://dict.youdao.com/dictvoice?le=fr&audio=${encodeURIComponent(text)}`;
  const audio = new Audio(url);
  audio.play();
}
