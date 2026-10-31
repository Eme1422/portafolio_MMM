import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio - Mariana Martínez Maya",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados (Paleta rosa pastel + Verde botánico + Estilo de Sidebar)
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

    /* Estilo del Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F0DCDD;
        border-right: 1px solid #EAC8CE;
    }
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #5A444A !important;
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

    /* Título de la Parte General del Portafolio */
    .part-title {
        font-size: 2rem;
        font-weight: 800;
        color: #5A444A;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #EAC8CE;
        padding-bottom: 8px;
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

# ==============================================================================
# --- PANEL LATERAL (SIDEBAR) - MENÚ DE APLICACIONES ---
# ==============================================================================
with st.sidebar:
    st.subheader("🌿 Menú de Aplicaciones")
    st.markdown("Acceso rápido a todos los proyectos del portafolio.")
    
    st.markdown("---")
    st.markdown("### 📌 Primera Parte")
    st.markdown("""
    - **Clase 6**
      - [🚀 Mi primera app](https://nehggvugrng8fz7dll6swf.streamlit.app/)
      - [🔊 Texto a audio](https://imm1immari.streamlit.app/)
    - **Clase 7**
      - [🌐 Traductor](https://traductor-eoohpvlb8amz4peqgpohpg.streamlit.app/)
      - [📄 OCR](https://ocrememariana.streamlit.app/)
      - [🎙️ OCR con Audio](https://ocr-audio-vjtui8jndebjzh9drz6x2i.streamlit.app/)
    - **Clase 8**
      - [☁️ Wordcloud](https://wordcloud-oywdcddcuhkrbyrtcy2vcy.streamlit.app/)
      - [😊 Sentimientos](https://sentimenta-hlvyhhpvao67qkqgafqjox.streamlit.app/)
      - [📝 Analizador Texto](https://atextoamariana.streamlit.app/)
    - **Clase 9**
      - [🎯 YOLO](https://yolov5-urfjip3xkha8k742nhfdqj.streamlit.app/)
      - [🤖 Teachable Machine](https://teacheablemachinemm.streamlit.app/)
    """)
    
    st.markdown("---")
    st.markdown("### 📌 Segunda Parte")
    st.markdown("""
    - **Clase 11: LLMs**
      - [💬 Chatpdf](https://chatpdf-hsbuepw2uzpandxsqbuq6u.streamlit.app/)
      - [👁️ Ver Imágenes](https://visionapp-jj23pqhr8ae6rnw92asp2c.streamlit.app/)
    - **Clase 12: Táctiles**
      - [🎨 Tablero](https://mnistpred-fgeyb6ktndmub94ymjvafe.streamlit.app/)
      - [🔍 Visión de Modelos](https://drawrecog-n29rrxhetpuywevwjuoc5e.streamlit.app/)
      - [📝 Ejercicio Clase](https://histinf-lkftauvtd9irebs3gmfnzo.streamlit.app/)
    - **Clase 13: IoT**
      - [📡 Lector MQTT](https://recepmqtt-ahdpcjtcnabiosgll3nvtc.streamlit.app/)
      - [🎛️ MQTT Control](https://sendcmqtt-c7f4qvrgpiccbrr2mg4kma.streamlit.app/)
      - [🎙️ Control Voz](https://ctrlvoice-jxkj9xjuu9qnhqusobz3po.streamlit.app/)
    """)


# --- BANNER PRINCIPAL ---
st.markdown("""
    <div class="hero-header">
        <h1 class="hero-title">Portafolio de Interfaces Multimodales</h1>
        <div class="hero-subtitle">Mariana Martínez Maya</div>
    </div>
""", unsafe_allow_html=True)


# ==============================================================================
# --- PRIMERA PARTE DEL PORTAFOLIO ---
# ==============================================================================
st.markdown('<div class="part-title">Primera Parte del Portafolio</div>', unsafe_allow_html=True)

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


# ==============================================================================
# --- SEGUNDA PARTE DEL PORTAFOLIO ---
# ==============================================================================
st.markdown('<div class="part-title">Segunda Parte del Portafolio</div>', unsafe_allow_html=True)

# --- CLASE 11 ---
st.markdown('<div class="section-title">Clase 11: Aplicaciones LLMS</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">💬 Chatpdf</div>
                <div class="project-desc">
                    Aplicación interactiva basada en Modelos de Lenguaje Grande para chatear, extraer información y consultar el contenido directamente de archivos PDF.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://chatpdf-hsbuepw2uzpandxsqbuq6u.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">👁️ Interpretación de imágenes</div>
                <div class="project-desc">
                    Herramienta de visión artificial asistida por LLM para analizar, describir y responder preguntas detalladas sobre los elementos visuales de una imagen.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://visionapp-jj23pqhr8ae6rnw92asp2c.streamlit.app/", use_container_width=True)


# --- CLASE 12 ---
st.markdown('<div class="section-title">Clase 12: Interacción con interfaces táctiles</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🎨 Tablero</div>
                <div class="project-desc">
                    Lienzo interactivo de dibujo libre optimizado para el reconocimiento en tiempo real de trazos y dígitos escritos a mano.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://mnistpred-fgeyb6ktndmub94ymjvafe.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🔍 Reconocimiento usando modelos de visión</div>
                <div class="project-desc">
                    Aplicación capaz de procesar bocetos y dibujos interactivos empleando arquitecturas de redes neuronales orientadas a la visión artificial.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://drawrecog-n29rrxhetpuywevwjuoc5e.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">📝 Ejercicio de clase</div>
                <div class="project-desc">
                    Práctica integradora enfocada en la manipulación y respuesta de interfaces multimodales interactivas desarrolladas en clase.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://histinf-lkftauvtd9irebs3gmfnzo.streamlit.app/", use_container_width=True)


# --- CLASE 13 ---
st.markdown('<div class="section-title">Clase 13: Sistemas con Internet de las Cosas</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">📡 Lector sensor Mqtt</div>
                <div class="project-desc">
                    Interfaz de monitoreo para la recepción y visualización de datos telemétricos enviados por sensores IoT mediante el protocolo MQTT.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://recepmqtt-ahdpcjtcnabiosgll3nvtc.streamlit.app/", use_container_width=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🎛️ Mqtt control</div>
                <div class="project-desc">
                    Panel de control remoto digital y analógico conectado a un broker MQTT para la actuación directa sobre dispositivos de hardware.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://sendcmqtt-c7f4qvrgpiccbrr2mg4kma.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("""
        <div class="project-card">
            <div>
                <div class="project-title">🎙️ Controlador de voz</div>
                <div class="project-desc">
                    Sistema multimodal de comandos por voz integrado con MQTT para operar y gobernar dispositivos inteligentes de manera inalámbrica.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Ir a la App ➔", "https://ctrlvoice-jxkj9xjuu9qnhqusobz3po.streamlit.app/", use_container_width=True)
