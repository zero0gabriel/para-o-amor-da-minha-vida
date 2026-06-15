import os
import random

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(
    page_title="Para a Minha Princesa",
    page_icon="💜",
    layout="centered",
)

if "pagina_abriu_no_topo" not in st.session_state:
    st.session_state.pagina_abriu_no_topo = True
    components.html(
        """
        <script>
        const irParaOTopo = () => {
            try {
                window.parent.history.scrollRestoration = "manual";
                window.parent.scrollTo(0, 0);
                window.parent.document.documentElement.scrollTop = 0;
                window.parent.document.body.scrollTop = 0;
            } catch (e) {}
        };

        irParaOTopo();
        setTimeout(irParaOTopo, 100);
        setTimeout(irParaOTopo, 400);
        setTimeout(irParaOTopo, 900);
        </script>
        """,
        height=0,
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

    .mini-card p {
        margin: 0;
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
    .music-player {
    text-align: center;
    margin: 25px 0;
}

.cd {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    animation: spin 10s linear infinite;
    border: 8px solid rgba(255,255,255,0.08);

    box-shadow:
        0 0 25px rgba(168,85,247,0.4),
        0 0 60px rgba(168,85,247,0.2);
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}
    </style>
    """,
    unsafe_allow_html=True,
)

PASTA = os.path.dirname(os.path.abspath(__file__))

FOTOS = [
    ("amor.png", "jogo aleatorio mais que foi especial"),
    ("amor2.jpg", "eu amava a sua skin de caveira, que combinava com vc"),
    ("amor3.jpg", "SAKJSKJSAJSKAJS"),
]

MOTIVOS = [
    ("seu jeitinho", "vc tem um jeito que acalma tudo ao redor, e isso me pega demais."),
    ("sua companhia", "até as coisas mais simples ficam melhores quando vc tá por perto."),
    ("nossas risadas", "eu amo nossas besteiras, pq só a gente entende e isso é muito nossa cara."),
    ("seu carinho", "vc tem um jeito de cuidar de mim que fica morando na minha cabeça."),
]

LINHA_DO_TEMPO = [
    ("🎮", "o começo", "foi tudo meio simples no início, mas eu guardo isso com muito carinho."),
    ("💜", "as conversas", "do nada vc foi virando uma das melhores partes do meu dia."),
    ("🤍", "hoje", "hoje eu só sei que te amo muito e que eu queria te guardar num lugar seguro do meu coração."),
]

PROMESSAS = [
    ("cuidar", "quero continuar te cuidando do meu jeito, mesmo nas minhas tentativas meio tortas."),
    ("lembrar", "quero guardar nossas memórias, até as pequenas que parecem bobas pra todo mundo."),
    ("escolher", "quero continuar te escolhendo nos dias bons e nos dias difíceis também."),
    ("ficar", "quero viver mais coisas com vc, sem pressa, uma de cada vez."),
]

RECADOS = {
    "Quando estiver com saudade": "lembra que eu também fico pensando em vc do nada.",
    "Quando o dia estiver pesado": "eu to aq ta bom? respira um pouco e deixa eu segurar isso com vc.",
    "Quando quiser sorrir": "lembra das nossas besteiras e solta aquele KAKAKAKAK ou KAJSKAJSKAJKDJ sem medo.",
    "Quando esquecer o quanto é especial": "volta aqui e lê de novo: vc é tudo pra mim, minha princesa.",
}

MENSAGENS_CONFORTO = [
    "ei meu bem, eu to aq ta bom? vai com calma.",
    "vc não precisa aguentar tudo sozinha hoje.",
    "se o dia pesar, descansa um pouquinho, princesa.",
    "eu queria te dar um abraço bem apertado agora.",
    "não fica se cobrando tanto, vc já faz muito.",
    "vc é importante pra mim até nos dias mais chatinhos.",
    "calma, minha princesa. uma coisa de cada vez.",
    "eu gosto de vc até quando vc tá toda bagunçadinha por dentro.",
    "vc não precisa fingir que tá bem comigo.",
    "se bater vontade de chorar, chora. eu continuo aq.",
    "vc merece carinho, não cobrança.",
    "eu tenho muito orgulho de vc, de verdade.",
    "não deixa um dia ruim te fazer esquecer quem vc é.",
    "vc é mais forte do que pensa, mas também merece descanso.",
    "se sua cabeça estiver cheia, respira comigo: devagarzinho.",
    "eu amo seu jeitinho, até quando vc acha que tá impossível.",
    "vc pode ir devagar. devagar também chega.",
    "não precisa ser perfeita pra ser amada.",
    "eu gosto de vc de um jeito muito sincero.",
    "se hoje vc só conseguir descansar, já tá tudo bem.",
    "você não está sozinha nessa, meu bem.",
    "se quiser falar, falar comigo. se quiser silêncio, eu fico aq também.",
    "vc é minha princesa até nos dias difíceis.",
    "não some dentro dos seus pensamentos ruins.",
    "guarda isso: vc é amada, muito amada.",
]


def criar_mensagens(inicios: list[str], finais: list[str]) -> list[str]:
    return [f"{inicio} {final}" for inicio in inicios for final in finais]


MENSAGENS_POR_RECADINHO = {
    "Quando estiver com saudade": criar_mensagens(
        [
            "se a saudade apertar, lembra que eu também sinto a sua falta do nada.",
            "quando bater saudade, lembra das nossas conversas e ri um pouquinho.",
            "se vc sentir minha falta, guarda um pouco desse carinho aí dentro.",
            "quando parecer que eu tô longe, lembra que eu continuo pensando em vc.",
            "se der vontade de me chamar, chama sem medo.",
            "quando a saudade vier forte, deixa ela passar e fica tranquila.",
        ],
        [
            "eu fico feliz só de existir na sua vida.",
            "vc também mora nos meus pensamentos do nada.",
            "eu gosto muito de vc, simples assim.",
            "tem um pedacinho meu torcendo pra vc ficar bem.",
            "nossas memórias não somem só pq a gente tá longe.",
            "eu também sinto falta das nossas besteiras.",
        ],
    ),
    "Quando o dia estiver pesado": criar_mensagens(
        [
            "se o dia tiver pesado, respira devagar.",
            "quando tudo parecer demais, vai com calma.",
            "se sua cabeça estiver cheia, para um pouquinho.",
            "quando vc estiver cansada de tudo, lembra disso.",
            "se hoje estiver difícil, não briga tanto com vc.",
            "quando parecer que vc não aguenta, segura minha mão daqui.",
        ],
        [
            "vc não precisa resolver tudo hoje.",
            "só continuar já é muita coisa.",
            "vc merece descanso sem culpa.",
            "eu to aq, mesmo que seja por mensagem.",
            "um dia ruim não define quem vc é.",
            "vc é forte, mas também merece cuidado.",
        ],
    ),
    "Quando quiser sorrir": criar_mensagens(
        [
            "se vc quiser sorrir, lembra da gente no jogo.",
            "quando quiser rir um pouco, pensa nas nossas fases aleatórias.",
            "se bater vontade de ficar mais leve, lembra das nossas besteiras.",
            "quando o sorriso sumir, tenta lembrar dessas coisas bobas.",
            "se vc quiser uma lembrança boa, pega essa aqui.",
            "quando quiser ficar de boa, lembra do tanto que a gente já riu.",
        ],
        [
            "eu amo nossas piadas sem sentido.",
            "vc rindo é uma das coisas mais lindas pra mim.",
            "nossas besteiras são minhas memórias favoritas.",
            "eu gosto quando a gente vira criança do nada.",
            "só a gente entende metade das coisas, e isso é perfeito.",
            "eu queria tá aí rindo junto com vc.",
        ],
    ),
    "Quando esquecer o quanto é especial": criar_mensagens(
        [
            "se vc esquecer o quanto é especial, lê isso com calma.",
            "quando sua cabeça tentar te diminuir, lembra bem.",
            "se vc se sentir pouca coisa, não acredita nisso.",
            "quando vc duvidar de si mesma, eu te lembro.",
            "se bater insegurança, segura essa verdade aqui.",
            "quando vc achar que não é suficiente, para um segundo.",
        ],
        [
            "vc é tudo pra mim, minha princesa.",
            "vc tem um jeitinho que ninguém copia.",
            "vc faz diferença na minha vida de verdade.",
            "eu gosto de vc exatamente do seu jeito.",
            "vc é mais incrível do que imagina.",
            "eu tenho sorte de ter vc por perto.",
        ],
    ),
}


def voltar() -> None:
    st.session_state.index = (st.session_state.index - 1) % len(FOTOS)


def avancar() -> None:
    st.session_state.index = (st.session_state.index + 1) % len(FOTOS)


def nova_mensagem_conforto() -> None:
    categoria = st.session_state.get("recado_escolhido", "Quando o dia estiver pesado")
    mensagens = MENSAGENS_POR_RECADINHO[categoria]
    anterior = st.session_state.get("mensagem_conforto")
    opcoes = [mensagem for mensagem in mensagens if mensagem != anterior]
    st.session_state.mensagem_conforto = random.choice(opcoes)


def mostrar_cards(items: list[tuple[str, str]]) -> None:
    for inicio in range(0, len(items), 2):
        colunas = st.columns(2)
        for coluna, item in zip(colunas, items[inicio : inicio + 2]):
            titulo, texto = item
            with coluna:
                st.markdown(
                    f'<div class="mini-card"><strong>{titulo}</strong><p>{texto}</p></div>',
                    unsafe_allow_html=True,
                )


def mostrar_timeline(items: list[tuple[str, str, str]]) -> None:
    for icone, titulo, texto in items:
        st.markdown(
            f'<div class="timeline-item"><div class="timeline-dot">{icone}</div><div><strong>{titulo}</strong><p>{texto}</p></div></div>',
            unsafe_allow_html=True,
        )


if "index" not in st.session_state:
    st.session_state.index = 0

st.title("Para a Minha Princesa")
from PIL import Image
import os

caminho_cd = os.path.join(os.path.dirname(__file__), "cd.png")
imagem_cd = Image.open(caminho_cd)

st.image(imagem_cd, width=220)

st.markdown(
    "<p class='texto'>Um cantinho só nosso, feito para guardar memórias, carinho e tudo aquilo que eu nem sempre consigo falar direito.</p>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-note">
        eu fiz isso aqui pensando em vc do jeitinho que vc merece.<br>
        desde 03/09 do ano passado vc virou uma parte enorme de mim, e eu nem sei explicar direito o tamanho disso.<br>
        então eu juntei nossas memórias, nossas fases e um monte de carinho pra deixar tudo com a nossa cara.
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
        <h2>um pedacinho do que eu sinto</h2>
        <p>pq tem coisa que só faz sentido quando vem do coração.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="soft-card letter">
        <p>
         desde que vc entrou na minha vida, tudo ficou mais leve de um jeito que eu nem sei explicar.
         eu gosto das nossas conversas, das nossas risadas, das nossas fases aleatórias e até dos momentos em que a gente só fica existindo junto..
            queria algo que parecesse comigo, com vc, com a nossa história.
        </p>
        <p>
            desde que vc entrou na minha vida, tudo ficou mais leve de um jeito que eu nem sei explicar.
            eu gosto das nossas conversas, das nossas risadas, das nossas fases aleatórias e até dos momentos em que a gente só fica existindo junto.
        </p>
        <p>
            eu amo como a gente se ajuda, como a gente se entende e como o nosso amor é reciproco.
            vc é minha princesa, meu bem, e uma das partes mais lindas da minha vida.
        </p>
        <div class="signature">com carinho, gabriel 💜</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>nossa história</span>
        <h2>algumas partes que eu guardo</h2>
        <p>o mais bonito às vezes tá nas coisas mais simples mesmo.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

mostrar_timeline(LINHA_DO_TEMPO)

st.markdown(
    """
    <div class="section-title">
        <span>motivos</span>
        <h2>coisas que eu amo em vc</h2>
        <p>uns motivos, entre muitos, pra vc nunca duvidar do seu valor pra mim.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

mostrar_cards(MOTIVOS)

st.markdown(
    """
    <div class="soft-card">
        <p class="quote">"vc é a mãe que eu quero pros meus filhos."</p>
        <p class="quote-small">
            eu falo isso sem medo, pq eu sinto de verdade. vc é amor, parceria e paz pra mim.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-title">
        <span>promessas</span>
        <h2>pros próximos capítulos</h2>
        <p>não são promessas enormes. são jeitos simples de continuar te escolhendo todo dia.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

mostrar_cards(PROMESSAS)

st.markdown(
    """
    <div class="section-title">
        <span>recadinhos</span>
        <h2>abre quando precisar</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

recado_escolhido = st.selectbox(
    "Escolha um recadinho",
    list(MENSAGENS_POR_RECADINHO.keys()),
    key="recado_escolhido",
    label_visibility="collapsed",
)

if st.session_state.get("categoria_atual") != recado_escolhido:
    st.session_state.categoria_atual = recado_escolhido
    st.session_state.mensagem_conforto = random.choice(MENSAGENS_POR_RECADINHO[recado_escolhido])

if st.button("💌 Ver outra mensagem"):
    nova_mensagem_conforto()

st.markdown(
    f"""
    <div class="secret">
        {st.session_state.mensagem_conforto}
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
            minha princesa...<br><br>
            eu fiz isso aqui pensando em vc do jeitinho que vc é, com cada detalhe nosso que eu guardo aqui.<br><br>
            eu amo vc do fundo do meu coração, de um jeito que eu não consigo expressar bonito sempre, mas que é real todos os dias.<br><br>
            vc é tudo pra mim. e eu vou continuar te escolhendo, te cuidando e te amando, sempre. 💜
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.success("🤍 ainda vamos criar muitas memórias juntos, minha princesa 💜")

st.markdown(
    """
    <iframe
        style="position:absolute;width:1px;height:1px;opacity:0;pointer-events:none;"
        src="https://www.youtube.com/embed/FsQCwnHJ1so?autoplay=1&loop=1&playlist=FsQCwnHJ1so&controls=0&modestbranding=1"
        title="musica"
        frameborder="0"
        allow="autoplay; encrypted-media">
    </iframe>
    """,
    unsafe_allow_html=True,
)
