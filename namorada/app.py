import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Nosso Álbum 💖",
    page_icon="💖",
    layout="centered"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ffd6e7, #fff0f6);
}

h1 {
    text-align: center;
    color: #ff2f6d;
}

h2 {
    text-align: center;
    color: #d6336c;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}

.texto {
    text-align:center;
    color:#ff4d88;
    font-size:20px;
}

</style>
""", unsafe_allow_html=True)


st.title("💖 Nosso Álbum")
st.header("Momentos especiais com você 🫶")

st.markdown(
    "<p class='texto'>Cada foto guarda uma memória nossa ✨</p>",
    unsafe_allow_html=True
)


pasta = os.path.dirname(__file__)


fotos = [
    ("amor.png", "💘 O dia que te conheci"),
    ("amor2.jpg", "💫 Um momento que eu amo"),
    ("amor3.jpg", "😂 Nosso momento engraçado")
]


for arquivo, legenda in fotos:

    caminho = os.path.join(pasta, arquivo)

    if os.path.exists(caminho):

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        img = Image.open(caminho)

        st.image(
            img,
            use_container_width=True
        )

        st.markdown(
            f"<h3 style='text-align:center;color:#ff2f6d'>{legenda}</h3>",
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)


st.success("💗 Fim do nosso álbum. Ainda vamos criar muitas memórias 💗")
