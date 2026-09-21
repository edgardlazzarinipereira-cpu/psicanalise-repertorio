import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Plataforma Imersiva de Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual para os debates e mapas
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .defesa-box { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 6px solid #2980B9; margin-bottom: 20px; }
    .analogia-box { background-color: #EBF5FB; padding: 12px 15px; border-radius: 6px; border-left: 4px solid #2471A3; margin-top: 12px; font-style: italic; color: #1B4F72; }
    .mapa-central { background-color: #F4ECF7; padding: 20px; border-radius: 10px; border: 2px dashed #8E44AD; text-align: center; font-weight: bold; font-size: 18px; color: #512E5F; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# Base de Defesas Teóricas (Autores em 1ª pessoa com termos técnicos e analogias)
base_defesas = [
    {
        "autor": "Sigmund Freud",
        "papel": "Fundador da Psicanálise",
        "tese": "O psiquismo não se reduz à consciência; sou implacável ao afirmar que o aparelho psíquico é regido por conflitos tópicos e econômicos entre o Id, o Ego e o Superego, onde a repressão atua como guardiã da moralidade contra a pulsão.",
        "analogia": "O psiquismo é como um iceberg econômico: a consciência é apenas a ponta visível, enquanto a imensa massa submersa do inconsciente dita a direção das correntes por meio de pressões energéticas constantes.",
        "audio_texto": "Sigmund Freud defende que o psiquismo é regido pelo conflito entre Id, Ego e Superego, operando através de forças inconscientes."
    },
    {
        "autor": "Melanie Klein",
        "papel": "Pioneira das Relações Objetais",
        "tese": "O psiquismo infantil é um teatro de crueldades primitivas. Sustento que a mente opera desde o nascimento dividida entre a posição esquizo-paranoide — marcada pela clivagem do objeto em total bom ou totalmente mau — e a dolorosa passagem para a posição depressiva.",
        "analogia": "É como um caleidoscópio emocional na infância: o bebê ora enxerga o mundo em estilhaços de aniquilação total (bom versus mau absoluto), ora tenta colar os pedaços quando descobre que quem nutre é o mesmo que frustra.",
        "audio_texto": "Melanie Klein argumenta que a mente se organiza nas posições esquizo-paranoide e depressiva através de fantasias inconscientes precoces."
    },
    {
        "autor": "Donald Winnicott",
        "papel": "Teórico do Amparo e Ambiente",
        "tese": "Eu vos digo que um bebê isolado não existe; o que existe é uma matriz vincular inseparável. O desenvolvimento saudável depende de um ambiente facilitador provido por uma mãe suficientemente boa, que sustenta o ego imaturo do infante por meio do holding.",
        "analogia": "O ambiente emocional é como o oxigênio em um mergulho: quando a adaptação materna é fina e contínua, a criança nem percebe a estrutura que a protege, respirando autonomia sem notar o cilindro de suporte.",
        "audio_texto": "Donald Winnicott defende que o sujeito se constitui a partir da mãe suficientemente boa e do ambiente facilitador."
    },
    {
        "autor": "Wilfred Bion",
        "papel": "Teorizador do Pensar e dos Grupos",
        "tese": "A mente é um aparelho para pensar os pensamentos. O indivíduo nasce incapaz de metabolizar dados sensoriais brutos — os elementos beta. É necessária a função alfa do analista, operando em reverie, para transformar essa matéria tóxica em elementos alfa pensáveis.",
        "analogia": "O analista funciona como um estômago psíquico ou um filtro biológico: recebe os detritos emocionais indigestos e caóticos do paciente, os metaboliza com continente carinhoso e técnico, e os devolve em nutrientes assimiláveis.",
        "audio_texto": "Wilfred Bion explica que a mente metaboliza elementos beta em alfa através da função de continência e reverie."
    },
    {
        "autor": "Jacques Lacan",
        "papel": "O Retorno a Freud (Estruturalista)",
        "tese": "Recuso o biologismo raso! O inconsciente é estruturado como uma linguagem. O sujeito nasce prematuro e se constitui no estádio do espelho, enredado na cadeia de significantes do Grande Outro, onde o desejo é sempre o desejo do Outro.",
        "analogia": "O ser humano é como um ator que entra em um palco onde o roteiro, o figurinista e a língua já foram escritos antes dele; nós falamos a linguagem, mas somos falados pelas estruturas simbólicas que nos antecedem.",
        "audio_texto": "Jacques Lacan postula que o inconsciente é estruturado como uma linguagem e que o sujeito se aliena na cadeia significante."
    }
]

# Menu Lateral
st.sidebar.markdown("### Navegação Imersiva")
menu = st.sidebar.radio("Escolha o Módulo:", [
    "🗺️ Mapa Central: Psicanálise em Rede", 
    "🗣️ Tribunal Teórico (Defesas dos Autores)", 
    "🃏 Cards de Estudo com Áudio & Prática"
])

st.markdown("<p class='main-header'>🧠 Plataforma Imersiva de Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Explore mapas conceituais e assista aos autores defendendo suas teses com rigor técnico e analogias.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MÓDULO 1: MAPA MENTAL CENTRALIZADO ---
if menu == "🗺️ Mapa Central: Psicanálise em Rede":
    st.subheader("🗺️ Mapa Mental: A Psicanálise no Centro")
    st.markdown("Esquema visual mostrando como o núcleo psicanalítico irradia para as diferentes escolas teóricas.")

    st.markdown("""
    <div class="mapa-central">
        🎯 NÚCLEO: PSICANÁLISE<br>
        <span style="font-size: 14px; font-weight: normal; color: #4A235A;">(O Inconsciente, o Conflito e a Subjetividade)</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏛️ Eixo Fundacional e Escola Inglesa")
        st.markdown("""
        - **Sigmund Freud** ➔ *Tópicas, Aparelho Psíquico & Repressão*
        - **Melanie Klein** ➔ *Posições Primitivas & Fantasia Inconsciente*
        - **Donald Winnicott** ➔ *Holding, Ambiente & Objeto Transicional*
        - **Wilfred Bion** ➔ *Função Alfa, Reverie & Elementos Beta*
        """)

    with col2:
        st.markdown("### 🌐 Eixo Estrutural e Contemporâneo")
        st.markdown("""
        - **Jacques Lacan** ➔ *Inconsciente como Linguagem & RSI*
        - **André Green** ➔ *Narcisismo de Morte & Vazio*
        - **Thomas Ogden** ➔ *Terceiro Analítico Intersubjetivo*
        - **Christopher Bollas** ➔ *O Conhecido Não Pensado*
        """)

# --- MÓDULO 2: TRIBUNAL TEÓRICO (DEFESAS EM 1ª PESSOA) ---
elif menu == "🗣️ Tribunal Teórico (Defesas dos Autores)":
    st.subheader("🗣️ Tribunal Teórico: Os Autores em Defesa de Suas Teses")
    st.markdown("Leia as argumentações técnicas e as analogias elaboradas por cada grande teólogo da psique humana.")

    autor_selecionado = st.selectbox("Escolha o autor para ouvir a defesa:", [a["autor"] for a in base_defesas])

    # Encontrar dados do autor escolhido
    autor_data = next(a for a in base_defesas if a["autor"] == autor_selecionado)

    st.markdown(f"""
    <div class="defesa-box">
        <h2>{autor_data['autor']}</h2>
        <p><strong>Papel Histórico:</strong> {autor_data['papel']}</p>
        <hr>
        <p style="font-size: 16px; line-height: 1.6;"><strong>A Defesa Teórica (Termos Técnicos):</strong><br>"{autor_data['tese']}"</p>
        
        <div class="analogia-box">
            <strong>💡 Analogia Explicativa:</strong> "{autor_data['analogia']}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Áudio (Text-to-Speech) integrado para o celular ou PC
    safe_text = autor_data['audio_texto'].replace("'", "").replace('"', "")
    audio_html = f"""
        <button onclick="
            var utterance = new SpeechSynthesisUtterance('{safe_text}');
            utterance.lang = 'pt-BR';
            window.speechSynthesis.speak(utterance);
        " style="background-color: #2E4053; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 15px;">
            🔊 Ouvir Defesa do Autor em Áudio
        </button>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- MÓDULO 3: CARDS DE ESTUDO MULTIMÍDIA ---
elif menu == "🃏 Cards de Estudo com Áudio & Prática":
    st.subheader("🃏 Cards de Estudo e Síntese Conceitual")
    for item in base_defesas:
        st.markdown(f"""
        <div style="background-color: #F8F9FA; padding: 15px; border-radius: 8px; border-left: 5px solid #1B4F72; margin-bottom: 15px;">
            <h4>{item['nome'] if 'nome' in item else item['autor']}</h4>
            <p><strong>Tese Central:</strong> {item['tese']}</p>
            <p><strong>Analogia:</strong> {item['analogia']}</p>
        </div>
        """, unsafe_allow_html=True)
