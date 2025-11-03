import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="Taylor's AI Universe 💛",
    page_icon="✨",
    layout="wide"
)

# CSS personalizado (efecto brillo y fondo dorado suave)
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #fff8e7, #ffe89d, #f5d06f);
    color: #3b2f2f;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
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

# Encabezado
st.title("🌟 Taylor’s AI Universe")
st.markdown("""
Bienvenido a **Taylor’s AI Universe**, un recorrido por las distintas aplicaciones 
que exploran Inteligencia Artificial en distintas eras, desde el reconocimiento visual 
hasta la comprensión emocional.  
Cada app representa una parte distinta de la “discografía” digital de Taylor 💛  
""")

with st.sidebar:
    st.subheader("✨ Sobre el proyecto")
    st.write("""
    Este portafolio reúne todas las aplicaciones IA desarrolladas, 
    cada una reimaginada como una era del universo de **Taylor Swift**.
    """)
    st.write("Desarrollado por **Migue 💻**, con narrativa AI by Taylor 🎤")

# --- COLUMNA 1 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🎙️ Taylor Voice Studio")
    image = Image.open('taylor_voice.png')
    st.image(image, width=250)
    st.write("Convierte tus textos en voz, como si Taylor misma recitara tus frases favoritas 💬🎧")
    st.write("[Abrir App](#)")

    st.header("🧠 Taylor’s Lyric Lab")
    image = Image.open('lyric_lab.png')
    st.image(image, width=250)
    st.write("Analiza emociones, subjetividad y tono en tus letras o frases. Aprende cómo suena tu texto en el universo de Taylor 🎶")
    st.write("[Abrir App](#)")

    st.header("📜 Taylor’s Secret Notes Scanner")
    image = Image.open('taylor_notes.png')
    st.image(image, width=250)
    st.write("Captura una nota o manuscrito y deja que el OCR revele los secretos escondidos entre las líneas ✨")
    st.write("[Abrir App](#)")

# --- COLUMNA 2 ---
with col2:
    st.header("🎨 Sketches to Songs")
    image = Image.open('draw_taylor.png')
    st.image(image, width=250)
    st.write("Convierte tus bocetos en descripciones visuales inspiradas, como si fueran portadas de los álbumes de Taylor 💫")
    st.write("[Abrir App](#)")

    st.header("👁️ Taylor Vision Pro")
    image = Image.open('taylor_vision.png')
    st.image(image, width=250)
    st.write("Usa visión por computadora con YOLOv5 para reconocer objetos — o como diría Taylor, *ver lo invisible* 🌌")
    st.write("[Abrir App](#)")

    st.header("📚 Speak Now Library")
    image = Image.open('taylor_chatpdf.png')
    st.image(image, width=250)
    st.write("Sube un PDF y charla con él: Taylor’s AI te responde con contexto y comprensión (RAG Mode 🧩)")
    st.write("[Abrir App](#)")

# --- COLUMNA 3 ---
with col3:
    st.header("🔢 Taylor Numbers Magic")
    image = Image.open('taylor_numbers.png')
    st.image(image, width=250)
    st.write("Reconoce dígitos escritos a mano y transforma garabatos en predicciones mágicas 💫")
    st.write("[Abrir App](#)")

    st.header("⚙️ Taylor Studio Controller")
    image = Image.open('taylor_mqtt.png')
    st.image(image, width=250)
    st.write("Controla luces, sonidos y sensores a través de MQTT, como si fuera la consola del *Eras Tour Tech Desk* 💡🎛️")
    st.write("[Abrir App](#)")

    st.header("🤖 Taylor Image Analyzer")
    image = Image.open('taylor_frame.png')
    st.image(image, width=250)
    st.write("Analiza imágenes con IA, interpreta detalles y sentimientos que solo una *true Swiftie AI* detectaría 💕")
    st.write("[Abrir App](#)")

# Pie de página
st.markdown("---")
st.markdown("""
🌈 **Taylor’s AI Universe** — un proyecto por *Migue*,  
combinando Inteligencia Artificial, visión, voz y emoción.  
*"Cause darling, I’m a mastermind."* 💛  
""")
