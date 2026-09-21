import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Plataforma Otimizada de Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual limpa e corrigida (sem bugs de HTML na tela)
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .defesa-box { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 6px solid #2980B9; margin-bottom: 20px; }
    .analogia-box { background-color: #EBF5FB; padding: 12px 15px; border-radius: 6px; border-left: 4px solid #2471A3; margin-top: 12px; font-style: italic; color: #1B4F72; }
    .mapa-central { background-color: #F4ECF7; padding: 20px; border-radius: 10px; border: 2px dashed #8E44AD; text-align: center; font-weight: bold; font-size: 18px; color: #512E5F; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# Base de Dados Unificada (Teoria, Defesa, Analogia e Áudio)
base_autores_otimizada = [
    {
        "autor": "Sigmund Freud",
        "papel": "Fundador da Psicanálise",
        "tese": "O psiquismo não se reduz à consciência; o aparelho psíquico é regido por conflitos tópicos e econômicos entre Id, Ego e Superego, onde a repressão atua como guardiã da moralidade contra a pulsão.",
        "analogia": "O psiquismo é como um iceberg econômico: a consciência é apenas a ponta visível, enquanto a imensa massa submersa do inconsciente dita as correntes energéticas.",
        "audio_texto": "Sigmund Freud defende que o psiquismo é regido pelo conflito entre Id, Ego e Superego, operando através de forças inconscientes."
    },
    {
        "autor": "Melanie Klein",
        "papel": "Pioneira das Relações Objetais",
        "tese": "A mente opera desde o nascimento dividida entre a posição esquizo-paranoide — clivagem do objeto em total bom ou mau — e a dolorosa passagem para a posição depressiva.",
        "analogia": "É como um caleidoscópio emocional infantil: ora o mundo é visto em estilhaços de aniquilação total, ora se integra quando se percebe que quem nutre é o mesmo que frustra.",
        "audio_texto": "Melanie Klein argumenta que a mente se organiza nas posições esquizo-paranoide e depressiva através de fantasias inconscientes precoces."
    },
    {
        "autor": "Donald Winnicott",
        "papel": "Teórico do Amparo e Ambiente",
        "tese": "Um bebê isolado não existe sem uma matriz vincular. O desenvolvimento depende de um ambiente facilitador provido por uma mãe suficientemente boa através do holding.",
        "analogia": "O ambiente emocional é como o oxigênio em um mergulho: quando a adaptação é perfeita, a criança respira autonomia sem notar a estrutura de suporte.",
        "audio_texto": "Donald Winnicott defende que o sujeito se constitui a partir da mãe suficientemente boa e do ambiente facilitador."
    },
    {
        "autor": "Wilfred Bion",
        "papel": "Teorizador do Pensar e dos Grupos",
        "tese": "A mente é um aparelho para pensar pensamentos. Elementos beta (sensações brutas) precisam ser metabolizados pela função alfa do analista em estado de reverie.",
        "analogia": "O analista funciona como um estômago psíquico: recebe os detritos emocionais caóticos do paciente, os metaboliza e os devolve em nutrientes pensáveis.",
        "audio_texto": "Wilfred Bion explica que a mente metaboliza elementos beta em alfa através da função de continência e reverie."
    },
    {
        "autor": "Jacques Lacan",
        "papel": "O Retorno a Freud (Estruturalista)",
        "tese": "O inconsciente é estruturado como uma linguagem. O sujeito se constitui no estádio do espelho, enredado na cadeia de significantes do Grande Outro.",
        "analogia": "O ser humano é como um ator que entra em um palco onde o roteiro e a língua já foram escritos antes dele; nós falamos a linguagem, mas somos falados por ela.",
        "audio_texto": "Jacques Lacan postula que o inconsciente é estruturado como uma linguagem e que o sujeito se aliena na cadeia significante."
    }
]

# Menu Lateral Restrito aos 3 Tópicos Principais
st.sidebar.markdown("### 🧠 Três Pilares de Estudo")
menu = st.sidebar.radio("Escolha o Tópico:", [
    "1. 🗺️ Mapa Central da Psicanálise", 
    "2. 🗣️ Tribunal Teórico (Defesa dos Autores)", 
    "3. 🃏 Cards, Exemplos & Áudio"
])

st.markdown("<p class='main-header'>Plataforma de Alta Performance em Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Ambiente otimizado com metodologias ativas de aprendizado e suporte multimídia.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- TÓPICO 1: MAPA MENTAL CENTRAL ---
if menu == "1. 🗺️ Mapa Central da Psicanálise":
    st.subheader("Pilar 1: Arquitetura Conceitual Centralizada")
    st.markdown("Visualização espacial da psicanálise irradiando para seus desdobramentos teóricos fundamentais.")

    st.markdown("""
    <div class="mapa-central">
        🎯 NÚCLEO: PSICANÁLISE<br>
        <span style="font-size: 14px; font-weight: normal; color: #4A235A;">(Inconsciente, Conflito, Metapsicologia e Subjetividade)</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏛️ Eixo Clássico & Inglês")
        st.markdown("""
        - **Freud** ➔ Aparelho Psíquico & Pulsão
        - **Klein** ➔ Posições & Fantasia Primitiva
        - **Winnicott** ➔ Holding & Objeto Transicional
        - **Bion** ➔ Função Alfa & Elementos Beta
        """)
    with col2:
        st.markdown("### 🌐 Eixo Estrutural & Contemporâneo")
        st.markdown("""
        - **Lacan** ➔ Inconsciente como Linguagem
        - **Green** ➔ Narcisismo de Morte & Vazio
        - **Ogden** ➔ Terceiro Analítico Intersubjetivo
        """)

# --- TÓPICO 2: TRIBUNAL TEÓRICO (DEFESAS) ---
elif menu == "2. 🗣️ Tribunal Teórico (Defesa dos Autores)":
    st.subheader("Pilar 2: Argumentação Ativa e Analogias Clínicas")
    st.markdown("Estudo imersivo através da defesa técnica e analógica de cada autor em primeira pessoa.")

    autor_selecionado = st.selectbox("Selecione o autor para analisar a tese:", [a["autor"] for a in base_autores_otimizada])
    autor_data = next(a for a in base_autores_otimizada if a["autor"] == autor_selecionado)

    # Renderização HTML segura garantindo que nenhuma tag apareça como texto puro
    st.markdown(f"""
    <div class="defesa-box">
        <h2>{autor_data['autor']}</h2>
        <p><strong>Papel:</strong> {autor_data['papel']}</p>
        <hr>
        <p style="font-size: 16px; line-height: 1.6;"><strong>A Defesa Teórica (Rigof Técnico):</strong><br>"{autor_data['tese']}"</p>
        <div class="analogia-box">
            <strong>💡 Analogia Explicativa:</strong> "{autor_data['analogia']}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Áudio integrado (Text-to-Speech nativo do navegador)
    safe_text = autor_data['audio_texto'].replace("'", "").replace('"', "")
    audio_html = f"""
        <button onclick="
            var utterance = new SpeechSynthesisUtterance('{safe_text}');
            utterance.lang = 'pt-BR';
            window.speechSynthesis.speak(utterance);
        " style="background-color: #2E4053; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 15px;">
            🔊 Ouvir Síntese em Áudio
        </button>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- TÓPICO 3: CARDS, EXEMPLOS E ÁUDIO ---
elif menu == "3. 🃏 Cards, Exemplos & Áudio":
    st.subheader("Pilar 3: Fixação Multimodal e Prática Clínica")
    st.markdown("Cartões de resumo estruturado combinando teoria, aplicações e reforço auditivo.")

    for item in base_autores_otimizada:
        st.markdown(f"""
        <div style="background-color: #F8F9FA; padding: 18px; border-radius: 8px; border-left: 5px solid #1B4F72; margin-bottom: 15px;">
            <h4>{item['autor']}</h4>
            <p><strong>Conceito Central:</strong> {item['tese']}</p>
            <p style="color: #7D3C98;"><strong>Analogia Prática:</strong> {item['analogia']}</p>
        </div>
        """, unsafe_allow_html=True)
