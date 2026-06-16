
import os
import base64
from datetime import datetime, timezone

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURAÇÕES PRINCIPAIS
# =========================================================

st.set_page_config(
    page_title="Para a Minha Princesa",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed",
)

PASTA = os.path.dirname(os.path.abspath(__file__))

# Ajuste aqui a data real do relacionamento.
# Formato: YYYY-MM-DDTHH:MM:SS
DATA_INICIO_RELACIONAMENTO = "2025-09-03T00:00:00"

# Arquivos de imagem que já estavam no seu projeto.
FOTOS = [
    ("amor.png",  "jogo aleatorio mais que foi especial"),
    ("amor2.jpg", "eu amava a sua skin de caveira, que combinava com vc"),
    ("amor3.jpg", "SAKJSKJSAJSKAJS"),
]

# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def img_b64(caminho: str) -> str:
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

def existe(nome_arquivo: str) -> bool:
    return os.path.exists(os.path.join(PASTA, nome_arquivo))

def intro_splash():
    caminho_cd = os.path.join(PASTA, "cd.png")
    if os.path.exists(caminho_cd):
        with open(caminho_cd, "rb") as f:
            cd_b64 = base64.b64encode(f.read()).decode()
        cd_tag = f'<img class="splash-cd" src="data:image/png;base64,{cd_b64}" alt="cd">'
    else:
        cd_tag = '<div class="fallback-heart">💜</div>'

    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
        .splash-wrap {{
            min-height: 70vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 18px;
            text-align: center;
            animation: enterUp .9s ease both;
        }}
        @keyframes enterUp {{
            from {{ opacity: 0; transform: translateY(24px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .cd-wrap {{
            position: relative;
            width: 210px;
            height: 210px;
        }}
        .splash-cd {{
            width: 210px;
            height: 210px;
            border-radius: 50%;
            object-fit: cover;
            animation: spin 10s linear infinite, glow 3s ease-in-out infinite;
            box-shadow: 0 0 32px rgba(168,85,247,.72), 0 0 95px rgba(168,85,247,.35);
            border: 6px solid rgba(255,255,255,.1);
        }}
        .fallback-heart {{
            width: 210px;
            height: 210px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 84px;
            animation: glow 2.8s ease-in-out infinite;
            background: rgba(109,40,217,.16);
            border: 1px solid rgba(221,214,254,.18);
        }}
        .splash-hole {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: #0d0820;
            border: 3px solid rgba(255,255,255,.38);
        }}
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
        @keyframes glow {{
            0%,100% {{ filter: drop-shadow(0 0 18px rgba(168,85,247,.42)); }}
            50% {{ filter: drop-shadow(0 0 34px rgba(168,85,247,.84)); }}
        }}
        .splash-title {{
            font-family: 'Playfair Display', serif;
            font-size: 40px;
            line-height: 1.1;
            margin: 0;
            color: var(--text);
            text-shadow: 0 10px 28px rgba(0,0,0,.35);
        }}
        .splash-sub {{
            font-size: 15px;
            line-height: 1.7;
            color: var(--muted);
            max-width: 340px;
            margin: 0;
        }}
        .splash-cta-note {{
            font-size: 13px;
            color: var(--muted);
            opacity: .9;
        }}
        </style>

        <div class="splash-wrap">
            <div class="cd-wrap">
                {cd_tag}
                <div class="splash-hole"></div>
            </div>
            <h1 class="splash-title">Para a Minha Princesa 💜</h1>
            <p class="splash-sub">um cantinho feito só pra guardar memórias, carinho e um monte de coisa nossa.</p>
            <p class="splash-cta-note">abre com calma... tem surpresa aqui dentro.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def inject_controls():
    """
    Injeta, uma única vez, um mini painel flutuante no documento pai:
    - botão dia/noite (sol/lua)
    - botão de música (coração pequeno)
    A música é um pad suave gerado com Web Audio API, sem depender de arquivo.
    """
    js = r"""
<script>
(function () {
try {
    const parentDoc = window.parent.document;
    if (parentDoc.getElementById("romance-floating-controls")) return;

    const style = parentDoc.createElement("style");
    style.id = "romance-floating-controls-style";
    style.textContent = `
      #romance-floating-controls {
        position: fixed;
        top: 14px;
        right: 14px;
        z-index: 99999;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px;
        border-radius: 999px;
        background: rgba(20, 12, 40, 0.28);
        border: 1px solid rgba(221,214,254,.18);
        backdrop-filter: blur(14px);
        box-shadow: 0 18px 42px rgba(0,0,0,.22);
      }

      html[data-theme="day"] #romance-floating-controls {
        background: rgba(255, 255, 255, 0.44);
        border-color: rgba(46, 16, 101, 0.14);
      }

      .romance-mini-btn {
        width: 36px;
        height: 36px;
        border-radius: 999px;
        border: 1px solid rgba(221,214,254,.22);
        background: linear-gradient(180deg, rgba(109,40,217,.78), rgba(76,29,149,.78));
        color: #fff;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
        box-shadow: 0 10px 24px rgba(76,29,149,.24);
        font-size: 17px;
        user-select: none;
        padding: 0;
      }

      html[data-theme="day"] .romance-mini-btn {
        background: linear-gradient(180deg, rgba(124,58,237,.78), rgba(168,85,247,.78));
        color: #fff;
      }

      .romance-mini-btn:hover {
        transform: translateY(-1px) scale(1.04);
        box-shadow: 0 14px 28px rgba(124,58,237,.32);
        filter: brightness(1.05);
      }

      .romance-mini-btn:active { transform: translateY(0) scale(.98); }

      .romance-heart-on {
        animation: heartPulse 1.25s ease-in-out infinite;
      }

      @keyframes heartPulse {
        0%,100% { transform: scale(1); }
        50% { transform: scale(1.12); }
      }

      .romance-mini-dot {
        width: 6px;
        height: 6px;
        border-radius: 999px;
        background: rgba(196,181,253,.75);
        box-shadow: 0 0 10px rgba(196,181,253,.4);
      }

      .romance-mini-label {
        font-size: 11px;
        color: rgba(245,243,255,.85);
        margin-right: 4px;
        letter-spacing: .06em;
        text-transform: uppercase;
        font-weight: 700;
        white-space: nowrap;
      }

      html[data-theme="day"] .romance-mini-label {
        color: rgba(36, 18, 73, .8);
      }

      @media (max-width: 600px) {
        #romance-floating-controls {
          top: 10px;
          right: 10px;
          gap: 6px;
          padding: 6px;
        }
        .romance-mini-btn { width: 34px; height: 34px; font-size: 16px; }
        .romance-mini-label { display: none; }
      }
    `;
    parentDoc.head.appendChild(style);

    const bar = parentDoc.createElement("div");
    bar.id = "romance-floating-controls";

    const label = parentDoc.createElement("div");
    label.className = "romance-mini-label";
    label.textContent = "tema";

    const themeBtn = parentDoc.createElement("button");
    themeBtn.type = "button";
    themeBtn.className = "romance-mini-btn";
    themeBtn.setAttribute("aria-label", "Alternar dia e noite");

    const musicBtn = parentDoc.createElement("button");
    musicBtn.type = "button";
    musicBtn.className = "romance-mini-btn";
    musicBtn.setAttribute("aria-label", "Tocar ou pausar música");

    const dot = parentDoc.createElement("div");
    dot.className = "romance-mini-dot";

    bar.appendChild(label);
    bar.appendChild(themeBtn);
    bar.appendChild(musicBtn);
    bar.appendChild(dot);
    parentDoc.body.appendChild(bar);

    const root = parentDoc.documentElement;
    const storedTheme = localStorage.getItem("romance-theme");
    const hour = new Date().getHours();
    const initialTheme = storedTheme || ((hour >= 6 && hour < 18) ? "day" : "night");

    function applyTheme(theme) {
      root.setAttribute("data-theme", theme);
      localStorage.setItem("romance-theme", theme);
      themeBtn.textContent = theme === "day" ? "☀" : "☾";
      themeBtn.title = theme === "day" ? "modo dia" : "modo noite";
    }

    applyTheme(initialTheme);

    themeBtn.addEventListener("click", () => {
      const current = root.getAttribute("data-theme") || "night";
      applyTheme(current === "night" ? "day" : "night");
    });

    // ---------- Música suave, sem arquivo externo ----------
    let audioCtx = null;
    let master = null;
    let oscillators = [];
    let gainNodes = [];
    let musicOn = localStorage.getItem("romance-music") === "on";

    function buildPad() {
      if (audioCtx) return;
      const AC = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AC();
      master = audioCtx.createGain();
      master.gain.value = 0.0001;
      master.connect(audioCtx.destination);

      const freqs = [220, 277.18, 329.63, 440];
      freqs.forEach((freq, i) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = i % 2 === 0 ? "sine" : "triangle";
        osc.frequency.value = freq;
        gain.gain.value = 0.0;

        osc.connect(gain);
        gain.connect(master);
        osc.start();

        oscillators.push(osc);
        gainNodes.push(gain);
      });

      const filter = audioCtx.createBiquadFilter();
      filter.type = "lowpass";
      filter.frequency.value = 900;
      master.disconnect();
      master.connect(filter);
      filter.connect(audioCtx.destination);

      const lfo = audioCtx.createOscillator();
      const lfoGain = audioCtx.createGain();
      lfo.frequency.value = 0.06;
      lfoGain.gain.value = 0.06;
      lfo.connect(lfoGain);
      lfoGain.connect(master.gain);
      lfo.start();

      window.__romanceLfo = lfo;
      window.__romanceFilter = filter;
    }

    async function startMusic() {
      buildPad();
      if (audioCtx.state === "suspended") {
        await audioCtx.resume();
      }
      musicOn = true;
      localStorage.setItem("romance-music", "on");
      musicBtn.textContent = "💜";
      musicBtn.classList.add("romance-heart-on");

      const target = 0.08;
      master.gain.cancelScheduledValues(audioCtx.currentTime);
      master.gain.setValueAtTime(master.gain.value, audioCtx.currentTime);
      master.gain.linearRampToValueAtTime(target, audioCtx.currentTime + 0.8);

      gainNodes.forEach((g, i) => {
        const base = [0.04, 0.025, 0.03, 0.018][i];
        g.gain.cancelScheduledValues(audioCtx.currentTime);
        g.gain.setValueAtTime(0.0, audioCtx.currentTime);
        g.gain.linearRampToValueAtTime(base, audioCtx.currentTime + 1.1);
      });
    }

    function stopMusic() {
      if (!audioCtx) {
        musicOn = false;
        localStorage.setItem("romance-music", "off");
        musicBtn.textContent = "🤍";
        musicBtn.classList.remove("romance-heart-on");
        return;
      }

      musicOn = false;
      localStorage.setItem("romance-music", "off");
      musicBtn.textContent = "🤍";
      musicBtn.classList.remove("romance-heart-on");

      master.gain.cancelScheduledValues(audioCtx.currentTime);
      master.gain.setValueAtTime(master.gain.value, audioCtx.currentTime);
      master.gain.linearRampToValueAtTime(0.0001, audioCtx.currentTime + 0.6);

      gainNodes.forEach(g => {
        g.gain.cancelScheduledValues(audioCtx.currentTime);
        g.gain.setValueAtTime(g.gain.value, audioCtx.currentTime);
        g.gain.linearRampToValueAtTime(0.0, audioCtx.currentTime + 0.55);
      });
    }

    musicBtn.addEventListener("click", async () => {
      if (musicOn) {
        stopMusic();
      } else {
        await startMusic();
      }
    });

    if (musicOn) {
      musicBtn.textContent = "💜";
      musicBtn.classList.add("romance-heart-on");
    } else {
      musicBtn.textContent = "🤍";
    }
} catch (e) {
    console.warn("romance controls error:", e);
}
})();
</script>
"""
    components.html(js, height=0, scrolling=False)

def render_realtime_counter():
    html = f"""
<div class="timer-card">
  <div class="timer-kicker">tempo do nosso relacionamento</div>
  <div class="timer-title">em tempo real</div>
  <div id="timer-main" class="timer-main">carregando...</div>
  <div class="timer-sub">dias, horas, minutos e segundos desde que tudo começou 💜</div>
</div>

<script>
(function() {{
  const start = new Date("{DATA_INICIO_RELACIONAMENTO}");
  const el = document.getElementById("timer-main");

  function pad(n) {{
    return String(n).padStart(2, "0");
  }}

  function update() {{
    const now = new Date();
    const diff = now - start;
    if (isNaN(diff)) {{
      el.innerHTML = "data de início inválida";
      return;
    }}
    const totalSeconds = Math.floor(diff / 1000);
    const days = Math.floor(totalSeconds / 86400);
    const hours = Math.floor((totalSeconds % 86400) / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    el.innerHTML = `<span>${{days}}</span> dias <span>${{pad(hours)}}</span> h <span>${{pad(minutes)}}</span> min <span>${{pad(seconds)}}</span> s`;
  }}

  update();
  setInterval(update, 1000);
}})();
</script>
"""
    components.html(html, height=190, scrolling=False)

def section_title(subtitle: str, title: str, text: str = ""):
    extra = f"<p>{text}</p>" if text else ""
    st.markdown(
        f"""
        <div class="section-title">
            <span>{subtitle}</span>
            <h2>{title}</h2>
            {extra}
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_cards(items):
    cols = st.columns(2)
    for idx, (title, body) in enumerate(items):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="mini-card">
                    <strong>{title}</strong>
                    <p>{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

def render_timeline(items):
    for icon, title, body in items:
        st.markdown(
            f"""
            <div class="timeline-item">
                <div class="timeline-dot">{icon}</div>
                <div>
                    <strong>{title}</strong>
                    <p>{body}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

def render_gallery(fotos):
    slides = []
    for filename, caption in fotos:
        path = os.path.join(PASTA, filename)
        if not os.path.exists(path):
            continue
        ext = filename.split(".")[-1].lower()
        mime = "image/png" if ext == "png" else "image/jpeg"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        slides.append((f"data:{mime};base64,{b64}", caption))

    if not slides:
        st.warning("Nenhuma foto encontrada na pasta do app.")
        return

    slides_html = "".join(
        f"""
        <div class="g-slide">
            <img src="{src}" loading="lazy" alt="memória {i+1}">
        </div>
        """ for i, (src, _) in enumerate(slides)
    )

    thumbs_html = "".join(
        f'<img src="{src}" class="g-thumb {"ativa" if i == 0 else ""}" onclick="goTo({i})" alt="miniatura {i+1}">'
        for i, (src, _) in enumerate(slides)
    )

    dots_html = "".join(
        f'<span class="g-dot {"ativa" if i == 0 else ""}" onclick="goTo({i})"></span>'
        for i in range(len(slides))
    )

    captions_js = "[" + ",".join(
        "'" + caption.replace("\\", "\\\\").replace("'", "\\'") + "'" for _, caption in slides
    ) + "]"

    html = f"""
    <div class="gallery-card">
        <div class="gallery-top">
            <div class="gallery-counter">memória <span id="g-idx">1</span> de <span id="g-total">{len(slides)}</span></div>
        </div>

        <div class="g-outer" id="g-outer">
            <div class="g-track" id="g-track">
                {slides_html}
            </div>
            <button class="g-arrow left" id="g-left" onclick="prevSlide()" aria-label="memória anterior">‹</button>
            <button class="g-arrow right" id="g-right" onclick="nextSlide()" aria-label="próxima memória">›</button>
        </div>

        <div id="g-caption" class="g-caption">{slides[0][1]}</div>

        <div class="g-dots">{dots_html}</div>
        <div class="g-thumbs">{thumbs_html}</div>
    </div>

    <script>
    (function() {{
      let idx = 0;
      const total = {len(slides)};
      const captions = {captions_js};
      const track = document.getElementById("g-track");
      const cap = document.getElementById("g-caption");
      const dots = document.querySelectorAll(".g-dot");
      const thumbs = document.querySelectorAll(".g-thumb");
      const left = document.getElementById("g-left");
      const right = document.getElementById("g-right");

      function sync() {{
        track.style.transform = `translateX(-${{idx * 100}}%)`;
        document.getElementById("g-idx").textContent = idx + 1;
        cap.classList.add("fade");
        setTimeout(() => {{
          cap.textContent = captions[idx];
          cap.classList.remove("fade");
        }}, 140);
        dots.forEach((d, i) => d.classList.toggle("ativa", i === idx));
        thumbs.forEach((t, i) => t.classList.toggle("ativa", i === idx));
        left.disabled = idx === 0;
        right.disabled = idx === total - 1;
      }}

      window.goTo = function(i) {{
        idx = Math.max(0, Math.min(total - 1, i));
        sync();
      }}
      window.prevSlide = function() {{
        if (idx > 0) idx--;
        sync();
      }}
      window.nextSlide = function() {{
        if (idx < total - 1) idx++;
        sync();
      }}

      sync();

      let startX = null;
      track.addEventListener("touchstart", e => startX = e.touches[0].clientX, {{passive:true}});
      track.addEventListener("touchend", e => {{
        if (startX === null) return;
        const dx = e.changedTouches[0].clientX - startX;
        if (Math.abs(dx) > 42) {{
          if (dx < 0) window.nextSlide();
          else window.prevSlide();
        }}
        startX = null;
      }});
    }})();
    </script>
    """
    components.html(html, height=860, scrolling=False)

# =========================================================
# CSS GLOBAL: TEMA, CURSOR, LAYOUT, CARDS E BOTOES
# =========================================================

st.markdown(
    """
    <style>
    :root {
        --bg-1: #120926;
        --bg-2: #090615;
        --bg-3: #20103f;
        --panel: rgba(33, 20, 69, 0.78);
        --panel-strong: rgba(24, 17, 52, 0.9);
        --text: #f5f3ff;
        --muted: #d8caff;
        --muted-2: #c4b5fd;
        --line: rgba(221,214,254,0.18);
        --line-strong: rgba(221,214,254,0.24);
        --accent: #a855f7;
        --accent-2: #8b5cf6;
        --accent-glow: rgba(168, 85, 247, 0.42);
        --shadow: rgba(0,0,0,0.46);
    }

    html[data-theme="day"] {
        --bg-1: #f8efff;
        --bg-2: #efe4ff;
        --bg-3: #e4d7ff;
        --panel: rgba(255,255,255,0.66);
        --panel-strong: rgba(255,255,255,0.8);
        --text: #26163f;
        --muted: #5d4b75;
        --muted-2: #7b60a0;
        --line: rgba(56, 25, 98, 0.14);
        --line-strong: rgba(56, 25, 98, 0.18);
        --accent: #7c3aed;
        --accent-2: #a855f7;
        --accent-glow: rgba(124, 58, 237, 0.28);
        --shadow: rgba(79, 29, 131, 0.14);
    }

    .stApp {
        background:
            radial-gradient(circle at 50% -10%, rgba(196, 181, 253, 0.30), transparent 32rem),
            radial-gradient(circle at 0% 30%, rgba(236, 72, 153, 0.14), transparent 22rem),
            linear-gradient(145deg, var(--bg-1) 0%, var(--bg-2) 52%, var(--bg-3) 100%);
        color: var(--text);
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
        opacity: 0.14;
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
        opacity: .9;
    }

    html[data-theme="day"] .stApp::after {
        background: linear-gradient(180deg, transparent 0%, rgba(255, 250, 255, 0.32) 100%);
        opacity: .75;
    }

    @keyframes moveStars {
        from { transform: translateY(0); }
        to { transform: translateY(-700px); }
    }

    .block-container {
        position: relative;
        z-index: 1;
        max-width: 900px;
        padding-top: 72px;
        padding-bottom: 54px;
    }

    .stApp, .stApp * {
        cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><path fill='%23a855f7' d='M16 28s-9.8-5.9-12.7-11.4C.8 11.3 2.7 6.8 7 6.1c2.7-.4 5.1.9 6.6 3 1.5-2.1 3.9-3.4 6.6-3 4.3.7 6.2 5.2 3.7 10.5C25.8 22.1 16 28 16 28z'/></svg>") 16 16, auto;
    }

    h1, h2, h3 {
        text-align: center;
        letter-spacing: 0;
        margin-top: 0;
    }

    h1 {
        color: var(--text);
        font-family: 'Playfair Display', serif;
        font-size: 54px;
        line-height: 1.05;
        margin-bottom: 8px;
        text-shadow: 0 12px 34px rgba(0, 0, 0, 0.35);
    }

    h2 {
        color: var(--text);
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        margin: 0 0 10px;
    }

    .texto {
        text-align: center;
        color: var(--muted);
        font-size: 18px;
        margin: 0 auto 26px;
        max-width: 640px;
        line-height: 1.7;
    }

    .hero-note,
    .soft-card,
    .mini-card,
    .timeline-item,
    .timer-card,
    .gallery-card {
        background: linear-gradient(180deg, rgba(46, 16, 101, 0.78), rgba(23, 18, 58, 0.90));
        border: 1px solid var(--line);
        border-radius: 24px;
        box-shadow: 0 22px 56px var(--shadow), inset 0 1px 0 rgba(255,255,255,0.08);
        backdrop-filter: blur(12px);
    }

    html[data-theme="day"] .hero-note,
    html[data-theme="day"] .soft-card,
    html[data-theme="day"] .mini-card,
    html[data-theme="day"] .timeline-item,
    html[data-theme="day"] .timer-card,
    html[data-theme="day"] .gallery-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.72), rgba(245, 238, 255, 0.76));
        box-shadow: 0 18px 44px var(--shadow), inset 0 1px 0 rgba(255,255,255,0.46);
    }

    .section-title {
        margin: 34px auto 18px;
        text-align: center;
    }

    .section-title span {
        color: var(--muted-2);
        display: block;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .section-title p {
        color: var(--muted);
        font-size: 16px;
        line-height: 1.65;
        margin: 0 auto;
        max-width: 640px;
    }

    .timeline-item {
        display: grid;
        grid-template-columns: 42px 1fr;
        gap: 14px;
        align-items: start;
        padding: 16px;
        margin-bottom: 14px;
    }

    .timeline-dot {
        align-items: center;
        background: rgba(168, 85, 247, 0.18);
        border: 1px solid var(--line);
        border-radius: 999px;
        color: var(--text);
        display: flex;
        font-size: 18px;
        height: 42px;
        justify-content: center;
        width: 42px;
    }

    .timeline-item strong {
        color: var(--text);
        display: block;
        font-size: 17px;
        margin-bottom: 5px;
    }

    .timeline-item p {
        color: var(--muted);
        line-height: 1.6;
        margin: 0;
    }

    .mini-card {
        color: var(--muted);
        line-height: 1.6;
        min-height: 128px;
        padding: 18px;
        margin-bottom: 14px;
    }

    .mini-card strong {
        color: var(--text);
        display: block;
        font-size: 18px;
        margin-bottom: 8px;
    }

    .mini-card p { margin: 0; }

    .timer-card {
        padding: 20px 18px;
        margin: 2px 0 18px;
    }

    .timer-kicker {
        text-align: center;
        color: var(--muted-2);
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .08em;
        margin-bottom: 8px;
    }

    .timer-title {
        text-align: center;
        font-family: 'Playfair Display', serif;
        color: var(--text);
        font-size: 27px;
        margin-bottom: 12px;
    }

    .timer-main {
        text-align: center;
        color: var(--text);
        font-size: 18px;
        font-weight: 700;
        line-height: 1.55;
    }

    .timer-main span {
        color: var(--accent);
        font-size: 24px;
        font-family: 'Playfair Display', serif;
    }

    .timer-sub {
        text-align: center;
        color: var(--muted);
        font-size: 14px;
        margin-top: 10px;
        line-height: 1.55;
    }

    .gallery-card {
        padding: 18px 18px 20px;
        margin-bottom: 24px;
    }

    .gallery-top {
        display: flex;
        justify-content: center;
        margin-bottom: 12px;
    }

    .gallery-counter {
        color: var(--muted-2);
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .g-outer {
        position: relative;
        overflow: hidden;
        border-radius: 22px;
        box-shadow: 0 12px 36px rgba(0,0,0,.30);
        touch-action: pan-x;
    }

    .g-track {
        display: flex;
        transition: transform .42s cubic-bezier(.4,0,.2,1);
        will-change: transform;
    }

    .g-slide {
        min-width: 100%;
    }

    .g-slide img {
        width: 100%;
        display: block;
        object-fit: contain;
        max-height: 600px;
        background: rgba(0,0,0,.22);
        border-radius: 22px;
    }

    .g-arrow {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 46px;
        height: 46px;
        border-radius: 999px;
        border: 1px solid rgba(221,214,254,.25);
        background: rgba(109,40,217,.72);
        color: white;
        font-size: 24px;
        cursor: pointer;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(6px);
        opacity: .94;
    }

    .g-arrow.left { left: 12px; }
    .g-arrow.right { right: 12px; }

    .g-arrow:disabled {
        opacity: .22;
        cursor: default;
    }

    .g-caption {
        text-align: center;
        color: var(--text);
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        margin: 14px 6px 0;
        min-height: 30px;
        transition: opacity .25s;
    }

    .g-caption.fade { opacity: 0; }

    .g-dots {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin: 12px 0 10px;
    }

    .g-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: rgba(196,181,253,.35);
        cursor: pointer;
        transition: transform .22s, background .22s;
    }

    .g-dot.ativa {
        background: var(--accent);
        transform: scale(1.4);
        box-shadow: 0 0 8px rgba(168,85,247,.7);
    }

    .g-thumbs {
        display: flex;
        gap: 9px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 6px;
    }

    .g-thumb {
        width: 64px;
        height: 64px;
        object-fit: cover;
        border-radius: 12px;
        border: 2px solid rgba(221,214,254,.14);
        cursor: pointer;
        transition: transform .2s, border-color .2s, box-shadow .2s;
    }

    .g-thumb:hover {
        transform: scale(1.07);
        border-color: rgba(168,85,247,.5);
    }

    .g-thumb.ativa {
        border: 2px solid var(--accent);
        box-shadow: 0 0 14px rgba(168,85,247,.65);
        transform: scale(1.05);
    }

    .stButton > button {
        width: 100%;
        min-height: 46px;
        background: linear-gradient(135deg, rgba(109, 40, 217, 0.92), rgba(139, 92, 246, 0.92));
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

    .hero-note {
        color: var(--text);
        font-size: 18px;
        line-height: 1.75;
        margin: 0 0 28px;
        padding: 22px 24px;
        text-align: center;
    }

    .quote {
        color: var(--text);
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        line-height: 1.45;
        margin: 0;
        text-align: center;
    }

    .quote-small {
        color: var(--muted-2);
        font-size: 15px;
        line-height: 1.7;
        margin: 14px auto 0;
        max-width: 560px;
        text-align: center;
    }

    .secret {
        background: linear-gradient(135deg, rgba(109, 40, 217, 0.48), rgba(30, 27, 75, 0.94));
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

    html[data-theme="day"] .secret {
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.20), rgba(255, 255, 255, 0.72));
        color: var(--text);
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 66px;
            padding-left: 18px;
            padding-right: 18px;
        }

        h1 { font-size: 40px; }
        h2 { font-size: 27px; }

        .hero-note,
        .mini-card,
        .timer-card,
        .gallery-card,
        .soft-card {
            border-radius: 20px;
        }

        .mini-card {
            padding: 15px;
        }

        .timer-main {
            font-size: 16px;
        }

        .timer-main span {
            font-size: 20px;
        }

        .timeline-item {
            grid-template-columns: 36px 1fr;
            padding: 14px;
        }

        .timeline-dot {
            height: 36px;
            width: 36px;
        }

        .g-slide img {
            max-height: 360px;
        }

        .g-arrow {
            width: 42px;
            height: 42px;
            font-size: 22px;
        }

        .g-thumb {
            width: 58px;
            height: 58px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# INÍCIO: CONTROLES E TEMA
# =========================================================

inject_controls()

if "entrou" not in st.session_state:
    st.session_state.entrou = False

if not st.session_state.entrou:
    intro_splash()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Entrar no nosso cantinho 💜"):
            st.session_state.entrou = True
            st.rerun()
    st.stop()

# =========================================================
# CONTEÚDO PRINCIPAL
# =========================================================

st.title("Para a Minha Princesa")

caminho_cd = os.path.join(PASTA, "cd.png")
if os.path.exists(caminho_cd):
    pass
else:
    st.warning("Coloque cd.png na mesma pasta do app para o disco girando aparecer.")

st.markdown(
    """
    <div class="hero-note">
    Um cantinho só nosso, feito para guardar memórias, carinho e tudo aquilo que eu nem sempre consigo falar direito.
    </div>
    """,
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

render_realtime_counter()

section_title(
    "galeria",
    "memórias que eu guardo",
    "desliza, toca nas miniaturas ou usa as setinhas pra ver tudo."
)
render_gallery(FOTOS)

section_title(
    "cartinha",
    "um pedacinho do que eu sinto",
    "pq tem coisa que só faz sentido quando vem do coração."
)

st.markdown(
    """
    <div class="soft-card" style="padding:22px 20px; line-height:1.85; color:var(--text); font-size:18px;">
    desde que vc entrou na minha vida, tudo ficou mais leve de um jeito que eu nem sei explicar.<br><br>
    eu gosto das nossas conversas, das nossas risadas, das nossas fases aleatórias e até dos momentos em que a gente só fica existindo junto.<br>
    queria algo que parecesse comigo, com vc, com a nossa história.<br><br>
    eu amo como a gente se ajuda, como a gente se entende e como o nosso amor é reciproco.<br>
    vc é minha princesa, meu bem, e uma das partes mais lindas da minha vida.<br><br>
    com carinho, gabriel 💜
    </div>
    """,
    unsafe_allow_html=True,
)

section_title(
    "nossa história",
    "algumas partes que eu guardo",
    "o mais bonito às vezes tá nas coisas mais simples mesmo."
)
render_timeline([
    ("🎮", "o começo", "foi tudo meio simples no início, mas eu guardo isso com muito carinho."),
    ("💜", "as conversas", "do nada vc foi virando uma das melhores partes do meu dia."),
    ("🤍", "hoje", "hoje eu só sei que te amo muito e que eu queria te guardar num lugar seguro do meu coração."),
])

section_title(
    "motivos",
    "coisas que eu amo em vc",
    "uns motivos, entre muitos, pra vc nunca duvidar do seu valor pra mim."
)
render_cards([
    ("seu jeitinho", "vc tem um jeito que acalma tudo ao redor, e isso me pega demais."),
    ("sua companhia", "até as coisas mais simples ficam melhores quando vc tá por perto."),
    ("nossas risadas", "eu amo nossas besteiras, pq só a gente entende e isso é muito nossa cara."),
    ("seu carinho", "vc tem um jeito de cuidar de mim que fica morando na minha cabeça."),
])

st.markdown(
    """
    <div class="quote">
    "vc é a mãe que eu quero pros meus filhos."
    </div>
    <div class="quote-small">
    eu falo isso sem medo, pq eu sinto de verdade. vc é amor, parceria e paz pra mim.
    </div>
    """,
    unsafe_allow_html=True,
)

section_title(
    "promessas",
    "pros próximos capítulos",
    "não são promessas enormes. são jeitos simples de continuar te escolhendo todo dia."
)
render_cards([
    ("cuidar", "quero continuar te cuidando do meu jeito, mesmo nas minhas tentativas meio tortas."),
    ("lembrar", "quero guardar nossas memórias, até as pequenas que parecem bobas pra todo mundo."),
    ("escolher", "quero continuar te escolhendo nos dias bons e nos dias difíceis também."),
    ("ficar", "quero viver mais coisas com vc, sem pressa, uma de cada vez."),
])

section_title("recadinhos", "abre quando precisar", "")
recado = st.selectbox(
    "Escolha um recadinho",
    [
        "Quando estiver com saudade",
        "Quando o dia estiver pesado",
        "Quando quiser sorrir",
        "Quando esquecer o quanto é especial",
    ],
    label_visibility="collapsed",
)

mensagens = {
    "Quando estiver com saudade": [
        "se a saudade apertar, lembra que eu também sinto a sua falta do nada. eu fico feliz só de existir na sua vida.",
        "quando bater saudade, lembra das nossas conversas e ri um pouquinho. vc também mora nos meus pensamentos do nada.",
        "se vc sentir minha falta, guarda um pouco desse carinho aí dentro. eu gosto muito de vc, simples assim.",
    ],
    "Quando o dia estiver pesado": [
        "se o dia tiver pesado, respira devagar. vc não precisa resolver tudo hoje.",
        "quando tudo parecer demais, vai com calma. só continuar já é muita coisa.",
        "se sua cabeça estiver cheia, para um pouquinho. vc merece descanso sem culpa.",
    ],
    "Quando quiser sorrir": [
        "se vc quiser sorrir, lembra da gente no jogo. eu amo nossas piadas sem sentido.",
        "quando quiser rir um pouco, pensa nas nossas fases aleatórias. vc rindo é uma das coisas mais lindas pra mim.",
        "se bater vontade de ficar mais leve, lembra das nossas besteiras. eu gosto quando a gente vira criança do nada.",
    ],
    "Quando esquecer o quanto é especial": [
        "se vc esquecer o quanto é especial, lê isso com calma: vc é tudo pra mim, minha princesa.",
        "quando sua cabeça tentar te diminuir, lembra bem: vc tem um jeitinho que ninguém copia.",
        "se vc se sentir pouca coisa, não acredita nisso. vc faz diferença na minha vida de verdade.",
    ],
}

if "mensagem_atual" not in st.session_state:
    st.session_state.mensagem_atual = mensagens[recado][0]
if st.session_state.get("recado_ativo") != recado:
    st.session_state.recado_ativo = recado
    st.session_state.mensagem_atual = mensagens[recado][0]

col_a, col_b = st.columns([1, 1])
with col_a:
    if st.button("💌 Ver outra mensagem"):
        opcoes = mensagens[recado]
        st.session_state.mensagem_atual = opcoes[(opcoes.index(st.session_state.mensagem_atual) + 1) % len(opcoes)]

with col_b:
    if st.button("✨ Trocar recado"):
        opcoes = mensagens[recado]
        st.session_state.mensagem_atual = opcoes[(opcoes.index(st.session_state.mensagem_atual) + 1) % len(opcoes)]

st.markdown(
    f"""
    <div class="secret">
    {st.session_state.mensagem_atual}
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

if st.button("💜 Abrir surpresa final"):
    st.balloons()
    st.markdown(
        """
        <div class="hero-note">
        minha princesa...<br><br>
        eu fiz isso aqui pensando em vc do jeitinho que vc é, com cada detalhe nosso que eu guardo aqui.<br>
        eu amo vc do fundo do meu coração, de um jeito que eu não consigo expressar bonito sempre, mas que é real todos os dias.<br>
        vc é tudo pra mim. e eu vou continuar te escolhendo, te cuidando e te amando, sempre. 💜
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.success("🤍 ainda vamos criar muitas memórias juntos, minha princesa 💜")

st.markdown(
    """
    <div style="text-align:center; color:var(--muted); font-size:14px; line-height:1.6;">
    Se o JavaScript estiver desligado, o contador em tempo real e os botões flutuantes não vão funcionar.
    </div>
    """,
    unsafe_allow_html=True,
)
