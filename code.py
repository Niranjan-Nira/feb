import streamlit as st
import streamlit.components.v1 as components

# ---------------------------
# Settings
# ---------------------------
st.set_page_config(
    page_title="For You 💖",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 👉 Change this to her name
HER_NAME = "Thiya"

# Session state for celebration trigger
if "party" not in st.session_state:
    st.session_state.party = False

# ---------------------------
# Global Styles (Fonts + Background + Theme)
# ---------------------------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;600;800&display=swap" rel="stylesheet">

    <style>
      :root{
        --pink-50:#fff5f7;
        --pink-100:#ffe4ec;
        --pink-200:#ffd1e1;
        --pink-400:#ff9ecf;
        --pink-600:#ff6fa9;
        --rose-700:#e03c7a;
        --orange-dot:#ffa500;
        --gold:#ffd700;
        --white:#ffffff;
      }

      /* Background: blush gradient + orange sparkling dots layered */
      .stApp {
        background:
          radial-gradient(circle at 12% 8%, rgba(255,165,0,0.18) 2.2px, transparent 3px) 0 0/38px 38px,
          radial-gradient(circle at 88% 24%, rgba(255,165,0,0.15) 2.4px, transparent 3px) 0 0/56px 56px,
          radial-gradient(circle at 30% 80%, rgba(255,215,0,0.10) 3px, transparent 4px) 0 0/90px 90px,
          linear-gradient(180deg, var(--pink-50) 0%, var(--pink-100) 45%, var(--white) 100%);
      }

      /* Hide Streamlit default UI clutter for a clean, romantic page */
      header, footer, [data-testid="stDecoration"] {visibility: hidden;}
      .block-container {padding-top: 2.5rem; padding-bottom: 3rem;}

      /* Hero section */
      .hero {
        text-align: center;
        margin: 1rem auto 0.25rem auto;
      }

      /* Name styling: big script with glossy gradient + glow */
      .name {
        font-family: 'Great Vibes', cursive;
        font-size: clamp(58px, 10vw, 120px);
        line-height: 1.05;
        margin: 0.2rem 0 0.25rem 0;
        background: linear-gradient(90deg, var(--pink-600), var(--pink-400), var(--gold));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow:
          0 2px 18px rgba(255, 105, 180, 0.28),
          0 0 8px rgba(255, 165, 0, 0.18);
        position: relative;
      }

      /* Small sparkles around the name */
      .name::after {
        content: "✦ ✧ ✦";
        font-size: 18px;
        color: var(--gold);
        margin-left: 12px;
        filter: drop-shadow(0 0 6px rgba(255,215,0,0.6));
      }

      /* Question */
      .question {
        font-family: 'Poppins', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
        font-weight: 700;
        color: #c2185b;
        font-size: clamp(20px, 3.8vw, 34px);
        letter-spacing: 0.3px;
        margin-top: 0.25rem;
      }
      .question span {
        background: linear-gradient(90deg, var(--rose-700), var(--pink-600));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 2px 12px rgba(255, 105, 180, 0.18);
      }

      /* Button refinement */
      .stButton>button {
        border-radius: 16px;
        padding: 0.9rem 1.3rem;
        font-size: 1.15rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(135deg, #ff5ea8 0%, #ff86b6 50%, #ffa9c9 100%);
        border: 2px solid rgba(255, 160, 190, 0.35);
        box-shadow:
          0 10px 22px rgba(255, 105, 180, 0.35),
          0 6px 10px rgba(255, 165, 0, 0.12) inset;
        transition: transform 120ms ease, box-shadow 120ms ease;
      }
      .stButton>button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow:
          0 14px 28px rgba(255,105,180,0.42),
          0 0 0 3px rgba(255, 199, 224, 0.45);
      }
      .stButton>button:active { transform: translateY(0); }

      /* A soft caption footer */
      .footnote {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 300;
        color: #b93a7a;
        opacity: 0.8;
        margin-top: 0.5rem;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Body
# ---------------------------
st.markdown(
    f"""
    <div class="hero">
      <div class="name">{HER_NAME}</div>
      <div class="question">Will you be my <span>everything</span>? 💞</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Center the Yes button
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    yes = st.button("Yes 💘", use_container_width=True, type="primary")

if yes:
    st.session_state.party = True

# Celebration section
if st.session_state.party:
    # Streamlit built-in balloons
    st.balloons()

    # Confetti fireworks area (canvas-confetti via CDN)
    fireworks_html = """
    <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <style>
          html, body { margin:0; padding:0; background: transparent; }
          #stage { position: relative; height: 100vh; width: 100%; background: transparent; overflow: hidden; }
          canvas { position:absolute; inset:0; }
          .label {
            position: absolute;
            bottom: 18px;
            left: 50%;
            transform: translateX(-50%);
            font-family: Poppins, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
            color: #b93a7a;
            font-weight: 600;
            background: rgba(255,255,255,0.55);
            padding: 8px 14px;
            border-radius: 999px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
          }
        </style>
      </head>
      <body>
        <div id="stage"></div>
        <script>
          const duration = 6000; // total show time
          const end = Date.now() + duration;
          const colors = ['#ff6fa9','#ff9ecf','#ffd700','#ffa500','#ffffff','#ffcee3'];

          // main confetti instance, auto-resize canvas
          const myConfetti = confetti.create(null, { resize: true, useWorker: true });

          // launch both sides + center bursts repeatedly
          (function frame(){
            myConfetti({ particleCount: 80, angle: 60, spread: 55, origin: { x: 0 }, colors });
            myConfetti({ particleCount: 80, angle: 120, spread: 55, origin: { x: 1 }, colors });

            // center fireworks-like pulse
            myConfetti({ particleCount: 140, spread: 100, startVelocity: 45, origin: { y: 0.6 }, ticks: 250, gravity: 0.9, scalar: 1.0, colors });

            // comet sparks top
            myConfetti({ particleCount: 40, startVelocity: 65, spread: 360, origin: { y: 0.1 }, scalar: 0.9, colors });

            if (Date.now() < end) {
              requestAnimationFrame(frame);
            } else {
              // final golden boom
              myConfetti({ particleCount: 250, spread: 120, startVelocity: 55, origin: { y: 0.7 }, colors: ['#ffd700','#ffa500','#ffffff'] });
            }
          })();
        </script>
      </body>
    </html>
    """

    # Height ~ full visible area of the app content (adjust if needed)
    components.html(fireworks_html, height=600, scrolling=False)

st.markdown('<div class="footnote">Made with all my love 💗</div>', unsafe_allow_html=True)