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
            radial-gradient(circle at 0% 30%, rgba(236, 72, 153, 0.16), transparent 24rem),
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
        background: linear-gradient(180deg, transparent 0%, rgba(9, 6, 21, 0.72) 100%);
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
        max-width: 860px;
        padding-top: 44px;
        padding-bottom: 54px;
    }

    h1, h2, h3 {
        text-align: center;
        letter-spacing: 0;
    }

    h1 {
        color: #f5f3ff;
        font-family: 'Playfair Display', serif;
        font-size: 54px;
        line-height: 1.05;
        margin-bottom: 8px;
        text-shadow: 0 12px 34px rgba(0, 0, 0, 0.48);
    }

    h2 {
        color: #f5f3ff;
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        margin: 0 0 10px;
    }

    .texto {
        text-align: center;
        color: #ddd6fe;
        font-size: 18px;
        margin: 0 auto 30px;
        max-width: 620px;
        line-height: 1.7;
    }

    .hero-note {
        background:
            linear-gradient(135deg, rgba(255, 255, 255, 0.10), rgba(109, 40, 217, 0.16));
        border: 1px solid rgba(221, 214, 254, 0.20);
        border-radius: 24px;
        color: #eee7ff;
        font-size: 18px;
        line-height: 1.75;
        margin: 0 0 28px;
        padding: 22px 24px;
        text-align: center;
        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.24);
        backdrop-filter: blur(12px);
    }

    .card, .soft-card {
        background:
            linear-gradient(180deg, rgba(46, 16, 101, 0.82), rgba(23, 18, 58, 0.90));
        border: 1px solid rgba(221, 214, 254, 0.20);
        border-radius: 24px;
        box-shadow:
            0 24px 60px rgba(0, 0, 0, 0.46),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
        margin-bottom: 24px;
        padding: 20px;
        backdrop-filter: blur(12px);
    }

    .card img {
        border-radius: 18px;
        box-shadow: 0 18px 42px rgba(0, 0, 0, 0.35);
    }

    .card h3 {
        margin: 20px 12px 8px;
        color: #eee7ff;
        font-family: 'Playfair Display', serif;
        font-size: 25px;
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

    .section-title {
        margin: 34px auto 18px;
        text-align: center;
    }

    .section-title span {
        color: #c4b5fd;
        display: block;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
        text-transform: uppercase;
    }

    .section-title p {
        color: #ddd6fe;
        font-size: 16px;
        line-height: 1.65;
        margin: 0 auto;
        max-width: 620px;
    }

    .letter {
        color: #eee7ff;
        font-size: 18px;
        line-height: 1.85;
    }

    .letter p {
        margin: 0 0 16px;
    }

    .letter .signature {
        color: #d8b4fe;
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        margin-top: 18px;
        text-align: right;
    }

    .timeline {
        display: grid;
        gap: 14px;
    }

    .timeline-item {
        display: grid;
        grid-template-columns: 42px 1fr;
        gap: 14px;
        align-items: start;
        background: rgba(255, 255, 255, 0.055);
        border: 1px solid rgba(221, 214, 254, 0.14);
        border-radius: 18px;
        padding: 16px;
    }

    .timeline-dot {
        align-items: center;
        background: rgba(168, 85, 247, 0.22);
        border: 1px solid rgba(221, 214, 254, 0.20);
        border-radius: 999px;
        color: #f5f3ff;
        display: flex;
        font-size: 18px;
        height: 42px;
        justify-content: center;
        width: 42px;
    }

    .timeline-item strong {
        color: #f5f3ff;
        display: block;
        font-size: 17px;
        margin-bottom: 5px;
    }

    .timeline-item p {
        color: #ddd6fe;
        line-height: 1.6;
        margin: 0;
    }

    .mini-grid {
        display: grid;
        gap: 14px;
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .mini-card {
        background: rgba(255, 255, 255, 0.065);
        border: 1px solid rgba(221, 214, 254, 0.14);
        border-radius: 18px;
        color: #ddd6fe;
        line-height: 1.6;
        min-height: 128px;
        padding: 18px;
    }

    .mini-card strong {
        color: #f5f3ff;
        display: block;
        font-size: 18px;
        margin-bottom: 8px;
    }

    .quote {
        color: #f5f3ff;
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        line-height: 1.45;
        margin: 0;
        text-align: center;
    }

    .quote-small {
        color: #c4b5fd;
        font-size: 15px;
        line-height: 1.7;
        margin: 14px auto 0;
        max-width: 560px;
        text-align: center;
    }

    .secret {
        background:
            linear-gradient(135deg, rgba(109, 40, 217, 0.48), rgba(30, 27, 75, 0.94));
        border: 1px solid rgba(221, 214, 254, 0.22);
        border-radius: 22px;
        box-shadow: 0 18px 44px rgba(0, 0, 0, 0.28);
        color: #f5f3ff;
        font-size: 18px;
        line-height: 1.7;
        margin-top: 12px;
        padding: 24px;
        text-align: center;
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

    div[data-baseweb="select"] > div {
        background: rgba(30, 27, 75, 0.88);
        border-color: rgba(221, 214, 254, 0.22);
        border-radius: 16px;
        color: #f5f3ff;
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(221, 214, 254, 0.32), transparent);
        margin: 30px 0;
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
            font-size: 40px;
        }

        h2 {
            font-size: 27px;
        }

        .card, .soft-card {
            padding: 15px;
            border-radius: 20px;
        }

        .card h3 {
            font-size: 21px;
            margin-left: 6px;
            margin-right: 6px;
        }

        .mini-grid {
            grid-template-columns: 1fr;
        }

        .timeline-item {
            grid-template-columns: 36px 1fr;
            padding: 14px;
        }

        .timeline-dot {
            height: 36px;
            width: 36px;
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

MOTIVOS = [
    ("Seu jeitinho", "Tem uma coisa em você que deixa qualquer dia mais leve, mesmo quando tudo parece bagunçado."),
    ("Sua companhia", "Até as coisas simples ficam melhores quando eu lembro que você faz parte da minha vida."),
    ("Nossas risadas", "Eu guardo cada momento bobo como se fosse uma foto que não precisa de câmera."),
    ("Seu carinho", "Você tem um jeito de ficar no pensamento sem fazer esforço nenhum."),
]

LINHA_DO_TEMPO = [
    ("🎮", "O primeiro momento", "Tudo começou de um jeito simples, mas virou uma memória que eu gosto de lembrar."),
    ("💜", "As conversas", "Aos poucos, cada mensagem foi virando parte boa do meu dia."),
    ("😂", "As fases aleatórias", "Teve jogo, skin, risada, fase careca e um monte de coisa que só a gente entende."),
    ("🤍", "O agora", "Hoje eu só queria deixar registrado que você é muito especial para mim."),
]

PROMESSAS = [
    ("Cuidar", "Prometo tentar ser abrigo nos dias difíceis e paz nos dias cansativos."),
    ("Lembrar", "Prometo guardar nossas memórias com carinho, até as mais bobinhas."),
    ("Escolher", "Prometo escolher você nos detalhes, nas conversas e nos pequenos gestos."),
    ("Ficar", "Prometo querer construir mais momentos bonitos, um de cada vez."),
]

RECADOS = {
    "Quando estiver com saudade": "fecha os olhos e lembra que tem alguém aqui que sorri só de pensar em você.",
    "Quando o dia estiver pesado": "respira com calma, minha princesa. Você não precisa carregar tudo sozinha.",
    "Quando quiser sorrir": "lembra das nossas besteiras, das fases aleatórias e de tudo que só a gente entende.",
    "Quando esquecer o quanto é especial": "volta aqui e lê de novo: você é uma das melhores partes da minha vida.",
}


def voltar() -> None:
    st.session_state.index = (st.session_state.index - 1) % len(FOTOS)


def avancar() -> None:
    st.session_state.index = (st.session_state.index + 1) % len(FOTOS)


def montar_cards(items: list[tuple[str, str]]) -> str:
    cards = "".join(
        f"""
        <div class="mini-card">
            <strong>{titulo}</strong>
            {texto}
        </div>
        """
        for titulo, texto in items
    )
    return f'<div class="mini-grid">{cards}</div>'


def montar_timeline(items: list[tuple[str, str, str]]) -> str:
    partes = "".join(
        f"""
        <div class="timeline-item">
            <div class="timeline-dot">{icone}</div>
            <div>
                <strong>{titulo}</strong>
                <p>{texto}</p>
            </div>
        </div>
        """
        for icone, titulo, texto in items
    )
    return f'<div class="timeline">{partes}</div>'


if "index" not in st.session_state:
    st.session_state.index = 0

st.title("Para a Minha Princesa")
st.markdown(
    "<p class='texto'>Um cantinho só nosso, feito para guardar memórias, carinho e tudo aquilo que eu nem sempre consigo falar direito.</p>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-note">
        Talvez isso aqui seja só uma página, mas cada pedacinho dela foi pensado para lembrar uma coisa:
        você importa muito para mim, e eu sou grato por cada memória que a gente já criou.
    </div>
    """,
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

st.markdown(
    """
    <div class="section-title">
        <span>cartinha</span>
        <h2>Um pedacinho do que eu sinto</h2>
        <p>Porque algumas coisas merecem ser guardadas com mais calma.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="soft-card letter">
        <p>
            Eu queria fazer algo simples, mas bonito, para mostrar que você não passa pela minha vida como qualquer pessoa.
            Você ficou nos detalhes: nas conversas, nas risadas, nos momentos aleatórios e até nas lembranças pequenas
            que parecem bobas, mas que para mim têm um valor enorme.
        </p>
        <p>
            Gosto de lembrar do começo, das nossas fases, das brincadeiras e de tudo que foi virando parte da nossa história.
            E mesmo quando eu não encontro as palavras perfeitas, eu espero que esse cantinho consiga dizer um pouco:
            você é especial de verdade.
        </p>
        <p>
            Obrigado por existir na minha vida, por deixar meus dias melhores e por ser essa pessoa que eu gosto tanto de cuidar,
            admirar e chamar de minha princesa.
        </p>
        <div class="signature">com carinho, de alguém que te ama muito 💜</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>nossa história</span>
        <h2>Algumas partes que eu guardo</h2>
        <p>Não precisa ser perfeito para ser inesquecível. Às vezes, o mais bonito mora no simples.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='soft-card'>{montar_timeline(LINHA_DO_TEMPO)}</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>motivos</span>
        <h2>Coisas que eu amo em você</h2>
        <p>Alguns motivos, entre muitos, para você nunca duvidar do quanto é importante.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='soft-card'>{montar_cards(MOTIVOS)}</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="soft-card">
        <p class="quote">"Você é aquele tipo de memória que dá vontade de viver de novo."</p>
        <p class="quote-small">
            E eu espero que a gente ainda crie muitas outras, daquelas que fazem a gente sorrir sem perceber.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>promessas</span>
        <h2>Para os próximos capítulos</h2>
        <p>Não são promessas enormes. São pequenas escolhas que eu quero continuar fazendo por você.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='soft-card'>{montar_cards(PROMESSAS)}</div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>recadinhos</span>
        <h2>Abra quando precisar</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

recado_escolhido = st.selectbox(
    "Escolha um recadinho",
    list(RECADOS.keys()),
    label_visibility="collapsed",
)

st.markdown(
    f"""
    <div class="secret">
        {RECADOS[recado_escolhido]}
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

if st.button("💜 Abrir surpresa final"):
    st.balloons()
    st.markdown(
        """
        <div class="secret">
            você é uma das melhores partes da minha vida 🤍<br>
            obrigado por tudo, por cada risada, por cada conversa e por cada memória que virou carinho em mim 💜
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.success("🤍 ainda vamos criar muitas memórias juntos 💜")

st.markdown(
    """
    <div class="card">
        <h2>🌙 Final secreto</h2>
        <p class="final-text">
            existem coisas que não cabem em palavras...<br>
            mas cabem direitinho no coração.<br><br>
            e você, minha princesa, mora em um dos lugares mais bonitos do meu.
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
