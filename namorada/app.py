import streamlit as st
from PIL import Image
import os

# 🌙 CONFIGURAÇÃO
st.set_page_config(
    page_title="Para a Minha Princesa 🤍",
    page_icon="💜",
    layout="centered"
)

# 💜 CSS MELHORADO (mesmo fundo + mais polimento)
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #2e1065, #0b061a);
}

/* ✨ estrelas */
.stApp:before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.15;
    animation: moveStars 60s linear infinite;
    z-index: 0;
}

@keyframes moveStars {
    from {transform: translateY(0px);}
    to {transform: translateY(-1000px);}
}

/* 🧠 textos */
h1, h2, h3 {
    text-align: center;
    color: #c4b5fd;
}

/* 💜 card melhorado */
.card {
    background: rgba(30, 27, 75, 0.88);
    padding: 22px;
    border-radius: 28px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.6);
    margin-bottom: 25px;
    transition: 0.3s ease-in-out;
    position: relative;
    z-index: 1;
}

.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 15px 40px rgba(168, 85, 247, 0.35);
}

/* 💬 texto bonito */
.texto {
    text-align: center;
    color: #ddd6fe;
    font-size: 20px;
    margin-top: -10px;
}

/* 🎁 surpresa */
.secret {
    background: #1e1b4b;
    padding: 18px;
    border-radius: 20px;
    text-align: center;
    color: #c4b5fd;
    margin-top: 10px;
    font-size: 16px;
}

/* 🎮 botões mais bonitos */
.stButton>button {
    background: #6d28d9;
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    border: none;
    transition: 0.2s ease-in-out;
    font-weight: bold;
}

.stButton>button:hover {
    background: #9333ea;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# 📁 pasta
pasta = os.path.dirname(__file__)

# 💜 título
st.title("🤍 Para a Minha Princesa")
st.markdown("<p class='texto'>memórias que eu guardo com carinho 💜</p>", unsafe_allow_html=True)

# 📸 fotos (NÃO ALTERADAS)
fotos = [
    ("amor.png", "🎮 O começo de tudo… aquele primeiro momento no jogo 💜"),
    ("amor2.jpg", "💀 Sua skin de caveira (eu amava quando combinava com você 🤍)"),
    ("amor3.jpg", "😂 A lendária fase careca kkkkk momentos que eu nunca esqueço 💜")
]

# 🧠 controle de estado
if "index" not in st.session_state:
    st.session_state.index = 0

arquivo, legenda = fotos[st.session_state.index]
caminho = os.path.join(pasta, arquivo)

# 💜 CARD PRINCIPAL
st.markdown("<div class='card'>", unsafe_allow_html=True)

if os.path.exists(caminho):
    img = Image.open(caminho)
    st.image(img, use_container_width=True)

st.markdown(
    f"<h3>{legenda}</h3>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# 🔁 navegação
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Voltar"):
        st.session_state.index = (st.session_state.index - 1) % len(fotos)

with col3:
    if st.button("Avançar ➡️"):
        st.session_state.index = (st.session_state.index + 1) % len(fotos)

# 🎁 surpresa
st.markdown("---")

if st.button("💜 clique aqui (surpresa)"):
    st.balloons()
    st.markdown("""
    <div class='secret'>
        você é uma das melhores partes da minha vida 🤍<br>
        obrigado por tudo 💜
    </div>
    """, unsafe_allow_html=True)

# 💌 final
st.markdown("---")
st.success("🤍 ainda vamos criar muitas memórias juntos 💜")

st.markdown("""
<div class='card'>
<h2>🌙 Final secreto</h2>
<p style='text-align:center;color:#ddd6fe'>
existem coisas que não cabem em palavras…
</p>
</div>
""", unsafe_allow_html=True)

# 🎧 música (NÃO ALTERADA)
st.markdown("""
<iframe width="0" height="0"
src="https://www.youtube.com/embed/FsQCwnHJ1so?autoplay=1&loop=1&playlist=FsQCwnHJ1so"
frameborder="0"
allow="autoplay">
</iframe>
""", unsafe_allow_html=True)