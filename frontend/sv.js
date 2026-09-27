// ---------------- DOM ----------------
const chatBox = document.getElementById("chat-box");
const downArrow = document.getElementById("centerDownArrow");
const inputBox = document.getElementById("user-input");
const languageSelect = document.getElementById("languageSelect");
const ttsPlayer = document.getElementById("ttsPlayer");

let isUserScrolling = false;
let lastBotReply = "";
let isSpeaking = false;
let currentAudio = null; // 🔥 IMPORTANT: store audio reference

// ---------------- AUTO GROW TEXTAREA ----------------
inputBox.addEventListener("input", () => {
  inputBox.style.height = "auto";
  const maxHeight = 90;
  inputBox.style.height =
    inputBox.scrollHeight <= maxHeight
      ? inputBox.scrollHeight + "px"
      : maxHeight + "px";
});

// ENTER = SEND
inputBox.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// ---------------- SCROLL HANDLING ----------------
chatBox.addEventListener("scroll", () => {
  const atBottom =
    chatBox.scrollHeight - chatBox.scrollTop - chatBox.clientHeight < 30;

  if (!atBottom) {
    isUserScrolling = true;
    downArrow.classList.add("show");
  } else {
    isUserScrolling = false;
    downArrow.classList.remove("show");
  }
});

downArrow.addEventListener("click", () => {
  chatBox.scrollTo({ top: chatBox.scrollHeight, behavior: "smooth" });
  isUserScrolling = false;
  downArrow.classList.remove("show");
});

// ---------------- TYPEWRITER EFFECT ----------------
function typeText(element, text, speed) {
  let i = 0;
  element.innerHTML = "";

  const interval = setInterval(() => {
    element.innerHTML += text.charAt(i);
    i++;

    if (!isUserScrolling) {
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    if (i >= text.length) clearInterval(interval);
  }, speed);
}

// ---------------- PLAY VOICE USING BACKEND (/tts) ----------------
async function speakText(text, language) {
  try {
    if (!text) {
      alert("No text to read");
      return;
    }

    // 🔴 If already speaking → stop first
    stopVoice();

    isSpeaking = true;
    ttsPlayer.innerText = "⏳ Loading...";

    const res = await fetch("https://dhanushlonely143-chatbot.hf.space/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        text: text,
        language: language || "en"
      })
    });

    if (!res.ok) throw new Error("TTS API failed");

    // IMPORTANT: Read as BLOB
    const audioBlob = await res.blob();
    const audioUrl = URL.createObjectURL(audioBlob);

    // 🔥 STORE AUDIO OBJECT
    currentAudio = new Audio(audioUrl);
    currentAudio.play();

    ttsPlayer.innerText = "⏸ Stop Voice";

    currentAudio.onended = () => {
      stopVoice();
    };

  } catch (err) {
    console.error("TTS error:", err);
    alert("Voice playback failed");
    stopVoice();
  }
}

// ---------------- STOP VOICE ----------------
function stopVoice() {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.currentTime = 0;
    currentAudio = null;
  }
  isSpeaking = false;
  ttsPlayer.innerText = "▶ Play Voice";
}

// ---------------- PLAY / STOP BUTTON ----------------
ttsPlayer.addEventListener("click", () => {
  if (!lastBotReply) {
    alert("No text to read");
    return;
  }

  if (!isSpeaking) {
    const lang = languageSelect ? languageSelect.value : "en";
    speakText(lastBotReply, lang);
  } else {
    // 🔥 ACTUALLY STOP AUDIO
    stopVoice();
  }
});

// ---------------- SEND MESSAGE ----------------
async function sendMessage() {
  const message = inputBox.value.trim();
  const language = languageSelect.value;

  if (!message) return;

  // User bubble
  chatBox.innerHTML += `<div class="user">${message}</div>`;
  chatBox.classList.add("active");

  inputBox.value = "";
  inputBox.style.height = "42px";

  try {
    const res = await fetch("https://dhanushlonely143-chatbot.hf.space/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, language })
    });

    if (!res.ok) throw new Error("Chat API error");

    const data = await res.json();

    const botDiv = document.createElement("div");
    botDiv.className = "bot";
    chatBox.appendChild(botDiv);

    lastBotReply = data.reply;

    // Typewriter output
    typeText(botDiv, data.reply, 18);

  } catch (e) {
    console.error(e);
    chatBox.innerHTML += `<div class="bot">Server error</div>`;
  }
}
