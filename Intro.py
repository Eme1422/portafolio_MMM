import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio - Mariana Martínez Maya",
    page_icon="🌿",
    layout="wide"
)

# Estilos CSS personalizados (Paleta rosa pastel + Verde botánico)
st.markdown("""
    <style>
    /* Fondo principal de la aplicación */
    .stApp {
        background-color: #F9ECEF;
        color: #333333;
    }

    /* Reducir márgenes superiores por defecto de Streamlit */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* Encabezado Principal */
    .hero-header {
        text-align: center;
        background: linear-gradient(135deg, #EAC8CE 0%, #F0D4D9 100%);
        padding: 40px 20px;
        border-radius: 20px;
        margin-bottom: 35px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }

    .hero-title {
        color: #5A444A;
        font-size: 2.3rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        color: #7D6167;
        font-size: 1.2rem;
        margin-top: 10px;
        font-weight: 500;
    }

    /* Título de las secciones / Clases */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #4A5D4E;
        margin-top: 25px;
        margin-bottom: 15px;
        border-left: 5px solid #8DA77B;
        padding-left: 12px;
    }

    /* Estilo de la tarjeta del proyecto */
    .project-card {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 22px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #F0DCDD;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 15px;
    }

    .project-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #3B4A3E;
        margin-bottom: 8px;
    }

    .project-desc {
        font-size: 0.92rem;
        color: #666666;
        line-height: 1.45;
        margin-bottom: 18px;
    }

    /* Estilo del Botón Verde */
    .stLinkButton > a {
        background-color: #8DA77B !important;
        color: #FFFFFF !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        display: block !important;
        text-align: center !important;
        box-shadow: 0 2px 6px rgba(141, 167, 123, 0.3);
    }

    .stLinkButton > a:hover {
        background-color: #6C8A59 !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(108, 138, 89, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER PRINCIPAL ---
st.markdown("""
    <div class="hero-header">
        <h1 class="hero-title">Portafolio de Interfaces Multimodales</h1>
        <div class="hero-subtitle">Mariana Martínez Maya</div>
    </div>
""", unsafe_allow_html=True)


# --- CLASE 6 ---
st.markdown('<div class="section-title">Clase 6</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🚀 Mi primera app</div>
                <div class="project-desc">
                    Primer paso en la implementación e integración de interfaces multimodales mediante el desarrollo de nuestra primera aplicación interactiva en Streamlit.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://nehggvugrng8fz7dll6swf.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🔊 Texto a audio</div>
                <div class="project-desc">
                    Conversión de texto a síntesis de voz (TTS). Permite una comunicación accesible y natural, facilitando la inclusión de personas con discapacidad visual e impulsando la creación de asistentes de voz.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://imm1immari.streamlit.app/", use_container_width=True)


# --- CLASE 7 ---
st.markdown('<div class="section-title">Clase 7</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🌐 Traductor</div>
                <div class="project-desc">
                    Herramienta de traducción automática multilingüe para derribar barreras del idioma e integrar procesamiento de lenguaje natural en tiempo real.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://traductor-eoohpvlb8amz4peqgpohpg.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">📄 OCR (Reconocimiento Óptico)</div>
                <div class="project-desc">
                    Extracción y reconocimiento automático de texto impreso o manuscrito desde archivos de imagen para su procesamiento digital.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://ocrememariana.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🎙️ OCR con Audio</div>
                <div class="project-desc">
                    Combinación de visión por computadora y audio: extrae el texto de imágenes mediante OCR y lo convierte de inmediato en voz sintetizada.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://ocr-audio-vjtui8jndebjzh9drz6x2i.streamlit.app/", use_container_width=True)


# --- CLASE 8 ---
st.markdown('<div class="section-title">Clase 8</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">☁️ Wordcloud</div>
                <div class="project-desc">
                    Generación de nubes de palabras interactivas para visualizar la frecuencia y las palabras clave más relevantes de un cuerpo de texto.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://wordcloud-oywdcddcuhkrbyrtcy2vcy.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">😊 Análisis de Sentimientos</div>
                <div class="project-desc">
                    Evaluación de opiniones mediante PLN para detectar emociones (positivas, negativas o neutras) expresadas en textos cortos o comentarios.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://sentimenta-hlvyhhpvao67qkqgafqjox.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">📝 Analizador de Texto</div>
                <div class="project-desc">
                    Procesamiento de datos textuales para extraer métricas clave, estructura, recuento léxico y patrones lingüísticos.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://atextoamariana.streamlit.app/", use_container_width=True)


# --- CLASE 9 ---
st.markdown('<div class="section-title">Clase 9</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🎯 YOLO (You Only Look Once)</div>
                <div class="project-desc">
                    Detección y localización de objetos en tiempo real mediante redes neuronales convolucionales de alta velocidad y precisión.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://yolov5-urfjip3xkha8k742nhfdqj.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🤖 Teachable Machine</div>
                <div class="project-desc">
                    Clasificación de patrones e imágenes utilizando un modelo de Machine Learning entrenado a medida para reconocimiento visual interactivo.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://teacheablemachinemm.streamlit.app/", use_container_width=True)
