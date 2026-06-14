import streamlit as st
from PIL import Image
import os

st.title("💖 Meu álbum de fotos com você meu bem")

st.header("Nosso álbum de momentos especiais")

pasta = os.path.dirname(__file__)

# 1
if st.button("💘 Ver o primeiro momento"):
    img1 = Image.open(os.path.join(pasta, "amor.png"))
    st.image(img1, caption="o dia que te conheci 💘")

st.markdown("---")

# 2
if st.button("💫 Ver segundo momento"):
    img2 = Image.open(os.path.join(pasta, "amor2.jpg"))
    st.image(img2, caption="eu amava vc de esqueleto bb")

st.markdown("---")

# 3
if st.button("😂 Ver momento engraçado"):
    img3 = Image.open(os.path.join(pasta, "amor3.jpg"))
    st.image(img3, caption="KASKASJKSJKSAJ")

st.markdown("---")

st.success("Fim do nosso álbum 💕")
