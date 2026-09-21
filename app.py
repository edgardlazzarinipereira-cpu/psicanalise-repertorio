import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Plataforma Avançada de Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .card-box { background-color: #F8F9FA; padding: 15px; border-radius: 8px; border-left: 5px solid #2C3E50; margin-bottom: 10px; }
    .mapa-box { background-color: #EAF2F8; padding: 15px; border-radius: 8px; border-left: 5px solid #2471A3; margin-bottom: 10px; font-family: monospace; }
    .comparacao-box { background-color: #F4ECF7; padding: 15px; border-radius: 8px; border-left: 5px solid #8E44AD; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Base de Dados de Autores
base_autores = [
    {"nome": "Sigmund Freud", "categoria": "Clássico", "obra": "A Interpretação dos Sonhos (1900)", "conceito": "Inconsciente, Aparelho Psíquico e Pulsão."},
    {"nome": "Melanie Klein", "categoria": "Clássico", "obra": "A Psicanálise de Crianças (1932)", "conceito": "Posições Psíquicas e Fantasia Inconsciente."},
    {"nome": "Jacques Lacan", "categoria": "Clássico", "obra": "Escritos (1966)", "conceito": "O Inconsciente estruturado como linguagem."},
    {"nome": "Donald Winnicott", "categoria": "Clássico", "obra": "O Brincar e a Realidade (1971)", "conceito": "Objeto Transicional e Mãe Suficientemente Boa."},
    {"nome": "Wilfred Bion", "categoria": "Clássico", "obra": "O Crescer do Pensar (1962)", "conceito": "Função Alfa, Reverie e Elementos Beta."},
    {"nome": "André Green", "categoria": "Contemporâneo", "obra": "O Complexo de Vida / Complexo de Morte", "conceito": "Narcisismo de Morte e Afetos Negativos."},
    {"nome": "Thomas Ogden", "categoria": "Contemporâneo", "obra": "Os Sujeitos da Psicanálise (1994)", "conceito": "Terceiro Analítico Intersubjetivo."}
]

# Menu Lateral
st.sidebar.markdown("### Navegação de Estudo")
menu = st.sidebar.radio("Escolha o Módulo:", [
    "📚 Biblioteca de Obras", 
    "🎯 Quiz Interativo com Gabarito", 
    "🗺️ Mapas Mentais da Psicanálise", 
    "⚖️ Concordâncias e Divergências"
])

st.markdown("<p class='main-header'>🧠 Plataforma de Estudos: Psicanálise & Metapsicologia</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Ambiente interativo com quiz validado, mapas estruturais e cruzamento teórico entre autores.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MÓDULO 1: BIBLIOTECA ---
if menu == "📚 Biblioteca de Obras":
    st.subheader("Repositório de Autores e Conceitos Centrais")
    for item in base_autores:
        st.markdown(f"""
        <div class="card-box">
            <strong>{item['nome']}</strong> ({item['categoria']})<br>
            <strong>📚 Obra Principal:</strong> {item['obra']}<br>
            <strong>🔑 Conceito-Chave:</strong> {item['conceito']}
        </div>
        """, unsafe_allow_html=True)

# --- MÓDULO 2: QUIZ INTERATIVO COM CONFERÊNCIA E EXPLICAÇÃO ---
elif menu == "🎯 Quiz Interativo com Gabarito":
    st.subheader("Simulador de Fixação com Conferência Imediata")
    st.markdown("Responda às questões, clique em conferir e analise a explicação teórica fundamentada.")

    # Questão 1
    st.markdown("### Questão 1: Metapsicologia Freudiana")
    q1_op = st.radio(
        "Qual instância do aparelho psíquico freudiano opera estritamente sob o Princípio do Prazer, buscando descarga imediata de impulsos?",
        ["A) Superego", "B) Ego", "C) Id", "D) Inconsciente Coletivo"],
        key="q1"
    )
    if st.button("Conferir Questão 1"):
        if q1_op.startswith("C)"):
            st.success("✅ **Resposta Correta!**")
            st.info("**Explicação:** O Id é o polo pulsional do aparelho psíquico, totalmente inconsciente e regido pelo princípio do prazer, exigindo satisfação imediata sem considerar a realidade ou a moral.")
        else:
            st.error("❌ **Incorreto.** Revise a dinâmica estrutural entre Id, Ego e Superego em Freud.")

    st.markdown("---")

    # Questão 2
    st.markdown("### Questão 2: Escola Inglesa / Bion")
    q2_op = st.radio(
        "O que representam os 'Elementos Beta' na teoria metapsicológica de Wilfred Bion?",
        ["A) Dados sensoriais brutos e emoções não metabolizadas que geram sofrimento.", "B) Mecanismos de defesa maduros estruturados pelo ego.", "C) Conceitos linguísticos equivalentes à metáfora em Lacan.", "D) Objetos transicionais criados pelo bebê na ausência da mãe."],
        key="q2"
    )
    if st.button("Conferir Questão 2"):
        if q2_op.startswith("A)"):
            st.success("✅ **Resposta Correta!**")
            st.info("**Explicação:** Os elementos beta são impressões sensoriais e emoções cruas que ainda não puderam ser sonhadas ou pensadas. Eles precisam ser metabolizados pela 'função alfa' (continência/reverie) para virarem pensamentos utilizáveis.")
        else:
            st.error("❌ **Incorreto.** Lembre-se de que Bion estuda como a mente metaboliza dados sensoriais brutos.")

# --- MÓDULO 3: MAPAS MENTAIS ---
elif menu == "🗺️ Mapas Mentais da Psicanálise":
    st.subheader("🗺️ Mapas Mentais Estruturais")
    st.markdown("Visualização esquemática das ramificações teóricas a partir da fundação freudiana.")

    st.markdown("### 1. Mapa Geral das Escolas Psicanalíticas")
    st.markdown("""
    <div class="mapa-box">
    SIGMUND FREUD (Fundação da Psicanálise / Inconsciente)<br>
    │<br>
    ├──► ESCOLA INGLESA & RELAÇÕES OBJETAIS<br>
    │     ├── Melanie Klein ──► Posições precoces e fantasia inconsciente<br>
    │     ├── Donald Winnicott ──► Ambiente, mãe suficientemente boa e objeto transicional<br>
    │     └── Wilfred Bion ──► Teoria do pensar, continência e função alfa<br>
    │<br>
    ├──► O RETORNO A FREUD (FRANÇA)<br>
    │     └── Jacques Lacan ──► Inconsciente estruturado como linguagem (R-S-I)<br>
    │<br>
    └──► PSICANÁLISE CONTEMPORÂNEA<br>
          ├── André Green ──► Narcisismo de morte e patologias do vazio<br>
          └── Thomas Ogden ──► Terceiro analítico e matriz intersubjetiva
    </div>
    """, unsafe_allow_html=True)

# --- MÓDULO 4: CONCORDÂNCIAS E DIVERGÊNCIAS ---
elif menu == "⚖️ Concordâncias e Divergências":
    st.subheader("⚖️ Cruzamento Teórico: Concordâncias e Divergências entre Autores")
    st.markdown("Análise comparativa de como os teóricos dialogam ou rompem entre si.")

    st.markdown("""
    <div class="comparacao-box">
        <h4>1. Freud vs. Melanie Klein (O Inconsciente Infantil)</h4>
        <p><strong>🤝 Concordância:</strong> Ambos mantêm a centralidade do Complexo de Édipo e a importância estruturante da sexualidade infantil na formação da psique.</p>
        <p><strong>⚡ Divergência:</strong> Freud postulava que o superego e o complexo de Édipo surgiam tardiamente (por volta dos 4 a 5 anos). Klein, baseada na análise de crianças pequenas, demonstrou que o Édipo e as defesas severas operam muito mais precocemente, logo no primeiro ano de vida.</p>
    </div>
    
    <div class="comparacao-box">
        <h4>2. Melanie Klein vs. Donald Winnicott (A Relação Mãe-Bebê)</h4>
        <p><strong>🤝 Concordância:</strong> Ambos pertencem à Escola Inglesa e concordam que o bebê humano nasce em total dependência e imerso em relações objetais desde o início.</p>
        <p><strong>⚡ Divergência:</strong> Klein focou intensamente no mundo interno fantasmático, nos impulsos destrutivos e na culpa inata da criança. Winnicott deslocou o foco para o **ambiente real**: para ele, o bebê isolado não existe sem um ambiente adaptativo (a mãe suficientemente boa). O foco de Winnicott é a sustentação e o desenvolvimento do *Self*.</p>
    </div>

    <div class="comparacao-box">
        <h4>3. Freud vs. Jacques Lacan (A Estrutura do Inconsciente)</h4>
        <p><strong>🤝 Concordância:</strong> Lacan adota o lema de que o analista deve retornar rigorosamente a Freud contra as distorções da psicologia do ego americana.</p>
        <p><strong>⚡ Divergência:</strong> Freud via o inconsciente ligado a pulsões biológicas e traços mnêmicos reprimidos. Lacan o redefine através da linguística estrutural: para ele, *“o inconsciente é estruturado como uma linguagem”*, operando pelas leis do significante (metáfora e metonímia).</p>
    </div>
    """, unsafe_allow_html=True)
