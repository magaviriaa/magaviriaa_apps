import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Taylor's App Universe 💛", page_icon="✨", layout="wide")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #fff8e7, #ffe89d, #f5d06f);
    color: #3b2f2f;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    color: #c48a00;
    text-shadow: 1px 1px 4px rgba(255, 230, 140, 0.8);
}
img {
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(255, 215, 100, 0.6);
}
a {
    color: #b07a00 !important;
    font-weight: bold;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("🌟 Taylor’s App Universe")
st.markdown("""
Una colección de **17 aplicaciones** reimaginadas como eras del universo de Taylor Swift.  
Cada una explora una faceta distinta: visión, lenguaje, voz, emoción y creatividad 💛  
""")

with st.sidebar:
    st.subheader("✨ Sobre el proyecto")
    st.write("""
    Este portafolio reúne todas las aplicaciones desarrolladas, 
    reimaginadas como si fueran eras del universo de **Taylor Swift**.
    """)
    st.write("Desarrollado por **Migue 💻**, con narrativa by Taylor 🎤")

# --- COMIENZO DEL PORTAFOLIO ---
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    st.header("🎤 1. IntroMigue (Taylor’s Opening Act)")
    st.image("intro.png", width=250)
    st.write("La bienvenida al tour: una introducción a la magia con estilo Taylor ✨")
    st.write("[Abrir App](#)")

    st.header("🗣️ 2. Traductor / Voice to Text")
    st.image("translator.png", width=250)
    st.write("Convierte voz en texto, como si Taylor grabara letras nuevas en tiempo real 🎙️")
    st.write("[Abrir App](#)")

    st.header("🎧 3. OCR Audio")
    st.image("ocr_audio.png", width=250)
    st.write("Deja que escuche, transcriba y te hable con claridad. Una app con ritmo 💬")
    st.write("[Abrir App](#)")

    st.header("🎹 4. Control por voz (Ctrl Voice)")
    st.image("ctrl_voice.png", width=250)
    st.write("Controla el entorno con comandos de voz — la consola de sonido del *Eras Tour* 🎛️")
    st.write("[Abrir App](#)")

    st.header("💡 5. Receptor MQTT")
    st.image("recep_mqtt.png", width=250)
    st.write("Recibe y visualiza señales como si fueran notas musicales conectadas ⚡")
    st.write("[Abrir App](#)")

    st.header("📡 6. Envío MQTT")
    st.image("send_mqtt.png", width=250)
    st.write("Envía datos a sensores o luces, porque hasta las máquinas merecen ritmo 🎶")
    st.write("[Abrir App](#)")

# --- COLUMNA 2 ---
with col2:
    st.header("🧠 7. TF-IDF Migue")
    st.image("tfidf.png", width=250)
    st.write("Un analizador de texto que entiende sentimientos — *The Emotion Era* 💌")
    st.write("[Abrir App](#)")

    st.header("📚 8. Chat PDF (Speak Now Library)")
    st.image("chatpdf.png", width=250)
    st.write("Haz que Taylor’s Read lea tus PDFs y converse contigo sobre ellos 💬📖")
    st.write("[Abrir App](#)")

    st.header("🧩 9. Análisis de Texto")
    st.image("analisis_texto.png", width=250)
    st.write("Analiza frases, emociones y palabras clave como si fueran letras de una canción 🎶")
    st.write("[Abrir App](#)")

    st.header("💬 10. Análisis con TextBlob (TX2)")
    st.image("tx2.png", width=250)
    st.write("Analiza sentimientos en frases y los clasifica: ¿Positiva, neutral o heartbreak? 💔")
    st.write("[Abrir App](#)")

    st.header("🪄 11. Dibujo (Draw Recognizer)")
    st.image("draw_taylor.png", width=250)
    st.write("Convierte dibujos en descripciones, como si Taylor diseñara portadas de álbumes 🎨")
    st.write("[Abrir App](#)")

    st.header("🔢 12. Hand Written (Reconocedor de Dígitos)")
    st.image("hand_digits.png", width=250)
    st.write("Predice dígitos escritos a mano — precisión y arte, como una firma autografiada ✍️")
    st.write("[Abrir App](#)")

# --- COLUMNA 3 ---
with col3:
    st.header("👁️ 13. YOLOv5 Vision")
    st.image("yolov5.png", width=250)
    st.write("Detecta objetos en tiempo real. Taylor Vision Pro te muestra el mundo en vivo 🎥")
    st.write("[Abrir App](#)")

    st.header("🎨 14. IMM1 (Análisis de Imagen con GPT-4o)")
    st.image("imm1.png", width=250)
    st.write("Sube una imagen y deja que te la describa como si fuera una metáfora poética ✨")
    st.write("[Abrir App](#)")

    st.header("🤖 15. TM (Modelo Entrenado)")
    st.image("tm.png", width=250)
    st.write("Reconoce patrones entrenados con tu propio modelo — en su *Midnights Era* 🖤")
    st.write("[Abrir App](#)")

    st.header("🔊 16. Texto a Voz (Text to Speech)")
    st.image("tts.png", width=250)
    st.write("Convierte texto en voz: Taylor leyendo tu diario secreto 💫")
    st.write("[Abrir App](#)")

    st.header("📜 17. OCR (Reconocimiento de Caracteres)")
    st.image("ocr.png", width=250)
    st.write("Captura texto desde una foto: descubre notas ocultas en cartas o letras 🎶")
    st.write("[Abrir App](#)")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("""
🌈 **Taylor’s AI Universe** — un proyecto por *Migue*,  
combinando Inteligencia Artificial, visión, voz y emoción.  
*"Cause darling, I’m a mastermind."* 💛  
""")
