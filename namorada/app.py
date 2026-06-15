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
    ("Seu jeitinho", "Não sei explicar direito, mas você tem um jeito que deixa tudo menos pesado."),
    ("Sua companhia", "Mesmo nas coisas mais aleatórias, com você parece que fica melhor."),
    ("Nossas risadas", "Eu gosto muito das nossas besteiras, porque são coisas que só a gente entende."),
    ("Seu carinho", "Você tem um jeito de ficar no meu pensamento sem nem tentar."),
]

LINHA_DO_TEMPO = [
    ("🎮", "O começo", "Começou de um jeito simples, mas eu lembro com um carinho absurdo."),
    ("💜", "As conversas", "Do nada você foi virando uma das melhores partes do meu dia."),
    ("😂", "As fases aleatórias", "Teve jogo, skin, risada, fase careca e umas coisas que só a gente sabe kkkkk."),
    ("🤍", "Hoje", "Hoje eu só queria deixar isso aqui guardado, porque você é muito especial para mim."),
]

PROMESSAS = [
    ("Cuidar", "Quero tentar cuidar de você do meu jeito, mesmo que às vezes eu seja meio bobo."),
    ("Lembrar", "Vou guardar nossas memórias, até aquelas pequenas que parecem nada."),
    ("Escolher", "Quero continuar te escolhendo nas conversas, nos detalhes e nos dias comuns."),
    ("Ficar", "Quero viver mais coisas com você, sem pressa, uma de cada vez."),
]

RECADOS = {
    "Quando estiver com saudade": "lembra que eu também fico bobo pensando em vc do nada.",
    "Quando o dia estiver pesado": "respira um pouco, meu amor. vc não precisa aguentar tudo quietinha.",
    "Quando quiser sorrir": "lembra das nossas besteiras e dessas fases aleatórias que só a gente entende.",
    "Quando esquecer o quanto é especial": "volta aqui e lê de novo: vc é muito importante pra mim, de verdade.",
}

MENSAGENS_CONFORTO = [
    "Respira um pouquinho, meu amor. Vai com calma.",
    "Você não precisa resolver a vida inteira hoje.",
    "Se o dia foi pesado, descansa. Você merece.",
    "Eu queria te dar um abraço bem apertado agora.",
    "Não fica se cobrando tanto, tá? Você já tenta muito.",
    "Você é importante para mim até nos dias que você não se sente importante.",
    "Calma, princesa. Uma coisa de cada vez.",
    "Eu estou aqui, mesmo que seja por essas palavrinhas.",
    "Você não precisa fingir que está bem comigo.",
    "Tem dias que só continuar já é muita coisa.",
    "Eu gosto de você até quando você está toda bagunçadinha por dentro.",
    "Seu valor não some só porque hoje foi difícil.",
    "Não deixa um dia ruim te convencer de coisas ruins sobre você.",
    "Você merece carinho, não cobrança.",
    "Se sua cabeça estiver cheia, tenta respirar e soltar um pouquinho.",
    "Eu tenho muito orgulho de você, mesmo quando você acha que não merece.",
    "Você não é fraca por cansar.",
    "Queria guardar seu coração num lugar bem calminho.",
    "Você é mais forte do que pensa, mas também pode descansar.",
    "Eu gosto de cuidar de você, até de longe.",
    "Nada em você é demais para mim.",
    "Se bater vontade de chorar, chora. Não tem problema.",
    "Eu queria que você se visse com o carinho que eu te vejo.",
    "Você não precisa carregar tudo sozinha.",
    "Hoje pode estar confuso, mas não vai ser assim para sempre.",
    "Eu fico aqui com você, tá?",
    "Você é minha princesa até nos dias difíceis.",
    "Não precisa ser perfeita para ser amada.",
    "Eu amo seu jeitinho, inclusive quando você acha que está impossível.",
    "Você merece uma pausa sem culpa.",
    "A vida às vezes pesa, mas você não precisa virar pedra por causa disso.",
    "Seu coração é bonito, mesmo quando está cansado.",
    "Se tudo parecer grande demais, começa pelo próximo minuto.",
    "Eu acredito em você de verdade.",
    "Você já passou por tanta coisa e ainda está aqui. Isso importa.",
    "Não esquece de beber água e respirar, meu bem.",
    "Eu queria transformar sua ansiedade em paz agora.",
    "Você pode ir devagar. Devagar também chega.",
    "Eu não vou te achar menos incrível por você ter dias ruins.",
    "Você é muito mais do que esse momento ruim.",
    "Se hoje você só conseguir descansar, já está tudo bem.",
    "Eu queria colocar sua cabecinha no meu peito e deixar o mundo quieto.",
    "Você não está sozinha nessa.",
    "Eu amo quando você existe perto de mim, mesmo de longe.",
    "Seu sorriso faz falta, mas você não precisa forçar ele.",
    "Pode ficar quietinha se quiser. Eu continuo gostando de você igual.",
    "Você não precisa explicar tudo para merecer cuidado.",
    "Eu gosto da sua presença de um jeito muito sincero.",
    "Respira comigo: devagarzinho, sem pressa.",
    "Você merece coisas leves.",
    "Se sua mente estiver brigando com você, lembra que ela não manda na verdade toda.",
    "Você é linda por dentro também, mesmo quando esquece disso.",
    "Eu queria estar aí só para te lembrar que vai ficar tudo bem.",
    "Um dia ruim não apaga a pessoa incrível que você é.",
    "Não deixa o medo falar mais alto que o carinho que existe por você.",
    "Você merece ser tratada com calma.",
    "Eu gosto de você de um jeito que dá vontade de cuidar.",
    "Se doer, fala comigo. Não guarda tudo aí dentro.",
    "Você não precisa vencer tudo hoje.",
    "Eu te escolheria até nos dias complicados.",
    "Você é uma das minhas partes favoritas da vida.",
    "Eu sei que às vezes pesa, mas eu tenho orgulho de você.",
    "Não se compara com ninguém, meu amor. Você tem seu tempo.",
    "Você não é um problema. Você é uma pessoa que eu amo.",
    "Se ninguém te disse hoje: eu estou feliz por você existir.",
    "Eu gosto até das suas manias bobinhas.",
    "Você merece um carinho bem demorado.",
    "Eu queria mandar paz direto para seu coração.",
    "Você pode descansar sem achar que está falhando.",
    "Seu jeito me faz bem de verdade.",
    "Não precisa se diminuir para caber em lugar nenhum.",
    "Você é suficiente, mesmo quando sua cabeça diz que não.",
    "Eu gosto de você sem precisar de motivo novo todo dia.",
    "Quando tudo apertar, lembra que eu me importo muito com você.",
    "Você tem um lugar muito bonito no meu coração.",
    "Eu amo sua forma de ser, até quando você duvida dela.",
    "Não some dentro dos seus pensamentos ruins.",
    "Você merece ser lembrada com amor.",
    "Eu queria te proteger de tudo que te machuca.",
    "Se hoje foi um dia daqueles, amanhã a gente tenta de novo.",
    "Você não precisa dar conta de tudo para merecer orgulho.",
    "Eu vejo muita coisa boa em você.",
    "Você é mais querida do que imagina.",
    "Até seu silêncio tem importância para mim.",
    "Eu fico feliz só de saber que você existe.",
    "Não deixa a tristeza te convencer que você está sozinha.",
    "Você pode ser sensível. Isso também é bonito.",
    "Eu queria que essa mensagem fosse um abraço.",
    "Você é muito especial, sério mesmo.",
    "Se estiver cansada, fecha os olhos um pouco. O mundo espera.",
    "Eu gosto de você nos detalhes pequenos.",
    "Você não precisa esconder quando estiver mal.",
    "Eu não vou embora só porque o dia ficou difícil.",
    "Você merece alguém que fique com paciência. Eu quero ser esse alguém.",
    "Seu coração merece descanso.",
    "Eu te amo mais do que eu consigo escrever bonito.",
    "Não precisa ter vergonha de precisar de carinho.",
    "Você é minha pessoa preferida para lembrar do nada.",
    "Se hoje a vida parece pesada, divide um pouquinho comigo.",
    "Guarda isso: você é amada.",
]


def criar_mensagens(inicios: list[str], finais: list[str]) -> list[str]:
    return [f"{inicio} {final}" for inicio in inicios for final in finais]


MENSAGENS_POR_RECADINHO = {
    "Quando estiver com saudade": criar_mensagens(
        [
            "Se a saudade apertar, lembra que eu penso em vc também.",
            "Quando bater saudade, fecha os olhos um pouquinho.",
            "Se vc sentir minha falta, guarda isso no coração.",
            "Quando parecer que eu estou longe demais, lembra disso.",
            "Se der vontade de me chamar, pode chamar sem medo.",
            "Quando a saudade chegar do nada, respira e lembra de nós.",
            "Se o coração ficar meio quietinho de saudade, calma.",
            "Quando vc sentir falta das nossas conversas, lembra bem.",
            "Se a saudade vier forte, deixa ela passar com carinho.",
            "Quando der aquele aperto por lembrar de mim, fica tranquila.",
        ],
        [
            "eu fico feliz só de existir na sua vida.",
            "vc também mora nos meus pensamentos do nada.",
            "eu gosto muito de vc, simples assim.",
            "tem um pedacinho meu torcendo pra vc ficar bem.",
            "nossas memórias não somem só pq a gente está longe.",
            "eu também sinto falta das nossas besteiras.",
            "vc é uma das pessoas que eu mais gosto de lembrar.",
            "eu queria estar aí só pra te dar um abraço.",
            "eu guardo vc com muito carinho aqui dentro.",
            "logo a saudade fica menor, e o carinho continua enorme.",
        ],
    ),
    "Quando o dia estiver pesado": criar_mensagens(
        [
            "Se o dia estiver pesado, respira devagar.",
            "Quando tudo parecer demais, vai com calma.",
            "Se sua cabeça estiver cheia, para um pouquinho.",
            "Quando vc estiver cansada de tudo, lembra disso.",
            "Se hoje estiver difícil, não briga tanto com vc.",
            "Quando parecer que vc não aguenta, segura minha mão daqui.",
            "Se o mundo estiver barulhento demais, fica um pouco quietinha.",
            "Quando o peito apertar, tenta respirar comigo.",
            "Se o dia não foi gentil, eu queria ser gentil com vc.",
            "Quando a vida pesar, não tenta carregar tudo sozinha.",
        ],
        [
            "vc não precisa resolver tudo hoje.",
            "só continuar já é muita coisa.",
            "vc merece descanso sem culpa.",
            "eu estou aqui, mesmo que seja por mensagem.",
            "um dia ruim não define quem vc é.",
            "vc é forte, mas também merece cuidado.",
            "eu tenho orgulho de vc por tentar.",
            "vai passar, nem que seja aos pouquinhos.",
            "vc merece paz no coração.",
            "eu queria tirar um pouco desse peso de vc.",
        ],
    ),
    "Quando quiser sorrir": criar_mensagens(
        [
            "Se vc quiser sorrir, lembra da gente no jogo.",
            "Quando quiser rir um pouco, pensa nas nossas fases aleatórias.",
            "Se bater vontade de ficar mais leve, lembra das nossas besteiras.",
            "Quando o sorriso sumir, tenta lembrar dessas coisas bobas.",
            "Se vc quiser uma lembrança boa, pega essa aqui.",
            "Quando quiser ficar de boa, lembra do tanto que a gente já riu.",
            "Se o dia estiver sem graça, pensa em alguma coisa nossa.",
            "Quando quiser sorrir do nada, lembra da fase careca kkkkk.",
            "Se vc precisar de um motivo bobo pra rir, lembra disso.",
            "Quando tudo estiver sério demais, pensa na gente sendo besta.",
        ],
        [
            "eu amo nossas piadas sem sentido.",
            "vc rindo é uma das coisas mais lindas pra mim.",
            "nossas besteiras são minhas memórias favoritas.",
            "eu gosto quando a gente vira criança do nada.",
            "só a gente entende metade das coisas, e isso é perfeito.",
            "eu queria estar aí rindo junto com vc.",
            "vc deixa até as coisas bobas especiais.",
            "eu sorrio só de lembrar de algumas conversas nossas.",
            "a gente é meio doido, mas é isso que eu gosto.",
            "guarda esse sorrisinho, pq ele combina muito com vc.",
        ],
    ),
    "Quando esquecer o quanto é especial": criar_mensagens(
        [
            "Se vc esquecer o quanto é especial, lê isso com calma.",
            "Quando sua cabeça tentar te diminuir, lembra bem.",
            "Se vc se sentir pouca coisa, não acredita nisso.",
            "Quando vc duvidar de si mesma, eu te lembro.",
            "Se bater insegurança, segura essa verdade aqui.",
            "Quando vc achar que não é suficiente, para um segundo.",
            "Se alguém ou alguma coisa te fizer duvidar do seu valor, lembra.",
            "Quando vc não conseguir ver sua própria luz, eu vejo.",
            "Se vc se sentir perdida, volta pra essa mensagem.",
            "Quando esquecer do seu brilho, deixa eu te lembrar.",
        ],
        [
            "vc é muito importante pra mim.",
            "vc tem um jeitinho que ninguém copia.",
            "vc faz diferença na minha vida de verdade.",
            "eu gosto de vc exatamente do seu jeito.",
            "vc é mais incrível do que imagina.",
            "eu tenho sorte de ter vc por perto.",
            "vc merece amor, cuidado e paciência.",
            "tem muita coisa linda em vc.",
            "eu escolheria vc de novo, sem pensar duas vezes.",
            "vc é minha princesa, e isso não muda nos dias difíceis.",
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
        <div class="signature">com carinho, Gabriel 💜</div>
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

mostrar_timeline(LINHA_DO_TEMPO)

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

mostrar_cards(MOTIVOS)

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

mostrar_cards(PROMESSAS)

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
