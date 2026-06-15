import os

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Para a Minha Princesa",
    page_icon="💜",
    layout="centered",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;700&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 50% -10%, rgba(196, 181, 253, 0.34), transparent 34rem),
            linear-gradient(145deg, #130a2f 0%, #090615 48%, #1f123f 100%);
        color: #f5f3ff;
        font-family: 'Inter', sans-serif;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            radial-gradient(rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(rgba(196,181,253,0.65) 1px, transparent 1px);
        background-size: 58px 58px, 94px 94px;
        background-position: 0 0, 28px 34px;
        opacity: 0.16;
        animation: moveStars 80s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    .stApp::after {
        content: "";
        position: fixed;
        inset: 0;
        background: linear-gradient(180deg, transparent 0%, rgba(9, 6, 21, 0.7) 100%);
        pointer-events: none;
        z-index: 0;
    }

    @keyframes moveStars {
        from { transform: translateY(0); }
        to { transform: translateY(-700px); }
    }

    .block-container {
        position: relative;
        z-index: 1;
        max-width: 780px;
        padding-top: 44px;
        padding-bottom: 46px;
    }

    h1, h2, h3 {
        text-align: center;
        letter-spacing: 0;
    }

    h1 {
        color: #f5f3ff;
        font-family: 'Playfair Display', serif;
        font-size: 48px;
        line-height: 1.06;
        margin-bottom: 8px;
        text-shadow: 0 12px 34px rgba(0, 0, 0, 0.48);
    }

    .texto {
        text-align: center;
        color: #d8b4fe;
        font-size: 18px;
        margin: 0 auto 30px;
        max-width: 560px;
        line-height: 1.65;
    }

    .card {
        background:
            linear-gradient(180deg, rgba(46, 16, 101, 0.82), rgba(23, 18, 58, 0.88));
        padding: 18px;
        border-radius: 24px;
        box-shadow:
            0 24px 60px rgba(0, 0, 0, 0.46),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
        margin-bottom: 24px;
        border: 1px solid rgba(221, 214, 254, 0.20);
        backdrop-filter: blur(12px);
    }

    .card img {
        border-radius: 18px;
        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.35);
    }

    .card h3 {
        margin: 20px 12px 6px;
        color: #eee7ff;
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        line-height: 1.35;
        font-weight: 600;
    }

    .photo-counter {
        text-align: center;
        color: #c4b5fd;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .secret {
        background:
            linear-gradient(135deg, rgba(109, 40, 217, 0.44), rgba(30, 27, 75, 0.94));
        padding: 22px;
        border-radius: 20px;
        text-align: center;
        color: #f5f3ff;
        margin-top: 12px;
        font-size: 18px;
        line-height: 1.6;
        border: 1px solid rgba(221, 214, 254, 0.22);
        box-shadow: 0 18px 44px rgba(0, 0, 0, 0.28);
    }

    .final-text {
        text-align: center;
        color: #ddd6fe;
        font-size: 18px;
        line-height: 1.7;
        margin: 0;
    }

    .stButton > button {
        width: 100%;
        min-height: 44px;
        background: rgba(109, 40, 217, 0.88);
        color: white;
        border-radius: 999px;
        padding: 10px 18px;
        border: 1px solid rgba(221, 214, 254, 0.22);
        box-shadow: 0 12px 28px rgba(76, 29, 149, 0.28);
        transition: 0.18s ease-in-out;
        font-weight: 700;
    }

    .stButton > button:hover {
        background: #8b5cf6;
        color: white;
        transform: translateY(-1px);
        border-color: rgba(255, 255, 255, 0.34);
        box-shadow: 0 16px 34px rgba(124, 58, 237, 0.34);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(221, 214, 254, 0.32), transparent);
        margin: 28px 0;
    }

    div[data-testid="stAlert"] {
        background: rgba(30, 27, 75, 0.78);
        color: #ddd6fe;
        border-color: rgba(196, 181, 253, 0.25);
        border-radius: 16px;
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 30px;
            padding-left: 18px;
            padding-right: 18px;
        }

        h1 {
            font-size: 38px;
        }

        .card {
            padding: 14px;
            border-radius: 20px;
        }

        .card h3 {
            font-size: 20px;
            margin-left: 6px;
            margin-right: 6px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

PASTA = os.path.dirname(os.path.abspath(__file__))

FOTOS = [
    ("amor.png", "🎮 O começo de tudo... aquele primeiro momento no jogo 💜"),
    ("amor2.jpg", "💀 Sua skin de caveira, que eu amava quando combinava com você 🤍"),
    ("amor3.jpg", "😂 A lendária fase careca kkkkk momentos que eu nunca esqueço 💜"),
]


def voltar() -> None:
    st.session_state.index = (st.session_state.index - 1) % len(FOTOS)


def avancar() -> None:
    st.session_state.index = (st.session_state.index + 1) % len(FOTOS)


if "index" not in st.session_state:
    st.session_state.index = 0

st.title("Para a Minha Princesa")
st.markdown(
    "<p class='texto'>Memórias simples, bonitas e guardadas com todo carinho.</p>",
    unsafe_allow_html=True,
)

arquivo, legenda = FOTOS[st.session_state.index]
caminho = os.path.join(PASTA, arquivo)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(
    f"<div class='photo-counter'>Memória {st.session_state.index + 1} de {len(FOTOS)}</div>",
    unsafe_allow_html=True,
)

if os.path.exists(caminho):
    imagem = Image.open(caminho)
    st.image(imagem, use_container_width=True)
else:
    st.warning(f"Coloque a imagem {arquivo} na mesma pasta do app.")

st.markdown(f"<h3>{legenda}</h3>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 0.25, 1])

with col1:
    st.button("← Voltar", on_click=voltar)

with col3:
    st.button("Avançar →", on_click=avancar)

st.markdown("---")

if st.button("💜 Abrir surpresa"):
    st.balloons()
    st.markdown(
        """
        <div class='secret'>
            você é uma das melhores partes da minha vida 🤍<br>
            obrigado por tudo 💜
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.success("🤍 ainda vamos criar muitas memórias juntos 💜")

st.markdown(
    """
    <div class='card'>
        <h2>🌙 Final secreto</h2>
        <p class='final-text'>
            existem coisas que não cabem em palavras...<br>
            mas cabem direitinho no coração.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <iframe width="0" height="0"
    src="https://www.youtube.com/embed/FsQCwnHJ1so?autoplay=1&loop=1&playlist=FsQCwnHJ1so"
    frameborder="0"
    allow="autoplay">
    </iframe>
    """,
    unsafe_allow_html=True,
)
