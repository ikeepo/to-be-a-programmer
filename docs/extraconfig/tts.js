// docs/extra_config/tts.js
console.log("TTS script loaded!"); // 添加这一行来确认加载

function speakFrench(text) {
  const url = `https://dict.youdao.com/dictvoice?le=fr&audio=${encodeURIComponent(text)}`;
  const audio = new Audio(url);
  audio.play();
}

// 在你的 tts.js 中添加
function speakChinese(text) {
  if ("speechSynthesis" in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "zh-CN"; // 设置为中文
    utterance.rate = 0.9; // 语速稍微调慢一点点，方便听清
    window.speechSynthesis.speak(utterance);
  } else {
    console.error("您的浏览器不支持语音合成。");
  }
}
