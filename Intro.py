import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio - Mariana Martínez Maya",
    page_icon="🌿",
    layout="wide"
)

# Estilos CSS personalizados (Fondo rosado claro y botones verdes)
st.markdown("""
    <style>
    /* Fondo principal de la aplicación */
    .stApp {
        background-color: #F8ECEE; /* Tono rosado claro de la paleta */
        color: #4A4A4A;
    }

    /* Estilo del título principal */
    .main-title {
        text-align: center;
        font-family: 'Playfair Display', serif, sans-serif;
        color: #615055;
        background-color: #EAC8CE; /* Rosado más acentuado */
        padding: 35px 20px;
        border-radius: 18px;
        margin-bottom: 30px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }

    /* Contenedor tipo tarjeta por cada clase */
    .class-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        border: 1px solid #F0DCDD;
    }

    .class-title {
        font-size: 22px;
        font-weight: 600;
        color: #4A5D4E;
        margin-bottom: 15px;
        border-bottom: 2px solid #EAC8CE;
        padding-bottom: 8px;
    }

    /* Estilo del botón enlace en verde */
    .stLinkButton > a {
        background-color: #8DA77B !important; /* Verde pastel de la paleta */
        color: #FFFFFF !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 500 !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        display: inline-block !important;
        width: 100% !important;
        text-align: center !important;
    }

    .stLinkButton > a:hover {
        background-color: #6C8A59 !important; /* Verde un poco más oscuro al pasar el cursor */
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Título Principal
st.markdown("""
    <div class="main-title">
        <h1 style="margin:0; font-size: 2.3rem;">Portafolio de interfaces multimodales</h1>
        <h3 style="margin-top:10px; font-weight: 400; color: #7A6167;">Mariana Martínez Maya</h3>
    </div>
""", unsafe_allow_html=True)

# --- CLASE 6 ---
with st.container():
    st.markdown('<div class="class-card">', unsafe_allow_html=True)
    st.markdown('<div class="class-title">Clase 6</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🚀 Mi primera app", "https://nehggvugrng8fz7dll6swf.streamlit.app/", use_container_width=True)
    with col2:
        st.link_button("🔊 Texto a audio", "https://imm1immari.streamlit.app/", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CLASE 7 ---
with st.container():
    st.markdown('<div class="class-card">', unsafe_allow_html=True)
    st.markdown('<div class="class-title">Clase 7</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("🌐 Traductor", "https://traductor-eoohpvlb8amz4peqgpohpg.streamlit.app/", use_container_width=True)
    with col2:
        st.link_button("📄 OCR", "https://ocrememariana.streamlit.app/", use_container_width=True)
    with col3:
        st.link_button("🎙️ OCR audio", "https://ocr-audio-vjtui8jndebjzh9drz6x2i.streamlit.app/", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CLASE 8 ---
with st.container():
    st.markdown('<div class="class-card">', unsafe_allow_html=True)
    st.markdown('<div class="class-title">Clase 8</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("☁️ Wordcloud", "https://wordcloud-oywdcddcuhkrbyrtcy2vcy.streamlit.app/", use_container_width=True)
    with col2:
        st.link_button("😊 Análisis de sentimientos", "https://sentimenta-hlvyhhpvao67qkqgafqjox.streamlit.app/", use_container_width=True)
    with col3:
        st.link_button("📝 Análisis de texto", "https://atextoamariana.streamlit.app/", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CLASE 9 ---
with st.container():
    st.markdown('<div class="class-card">', unsafe_allow_html=True)
    st.markdown('<div class="class-title">Clase 9</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🎯 Yolo", "https://yolov5-urfjip3xkha8k742nhfdqj.streamlit.app/", use_container_width=True)
    with col2:
        st.link_button("🤖 Teachable Machine", "https://teacheablemachinemm.streamlit.app/", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
