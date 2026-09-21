import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Plataforma Avançada de Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual limpa e profissional
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .defesa-box { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 6px solid #2980B9; margin-bottom: 20px; }
    .analogia-box { background-color: #EBF5FB; padding: 12px 15px; border-radius: 6px; border-left: 4px solid #2471A3; margin-top: 12px; font-style: italic; color: #1B4F72; }
    .mapa-central { background-color: #F4ECF7; padding: 20px; border-radius: 10px; border: 2px dashed #8E44AD; text-align: center; font-weight: bold; font-size: 18px; color: #512E5F; margin-bottom: 20px;}
    .mediador-box { background-color: #EAFAF1; padding: 20px; border-radius: 10px; border-left: 6px solid #27AE60; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# Base de Dados de Autores
base_autores = [
    {
        "autor": "Sigmund Freud",
        "papel": "Fundador da Psicanálise",
        "tese": "O psiquismo é regido por conflitos tópicos e econômicos entre Id, Ego e Superego, onde a repressão atua como guardiã da moralidade contra a pulsão.",
        "analogia": "O psiquismo é como um iceberg econômico: a consciência é a ponta visível, enquanto o inconsciente submerso dita as correntes energéticas.",
        "audio_texto": "Sigmund Freud defende que o psiquismo é regido pelo conflito entre Id, Ego e Superego, operando através de forças inconscientes."
    },
    {
        "autor": "Melanie Klein",
        "papel": "Pioneira das Relações Objetais",
        "tese": "A mente opera desde o nascimento dividida entre a posição esquizo-paranoide e a dolorosa passagem para a posição depressiva através de fantasias inconscientes.",
        "analogia": "É como um caleidoscópio emocional infantil: ora o mundo é visto em estilhaços de aniquilação total, ora se integra quando se percebe que quem nutre é o mesmo que frustra.",
        "audio_texto": "Melanie Klein argumenta que a mente se organiza nas posições esquizo-paranoide e depressiva através de fantasias inconscientes precoces."
    },
    {
        "autor": "Donald Winnicott",
        "papel": "Teórico do Amparo e Ambiente",
        "tese": "Um bebê isolado não existe sem uma matriz vincular. O desenvolvimento depende de um ambiente facilitador provido por uma mãe suficientemente boa.",
        "analogia": "O ambiente emocional é como o oxigênio em um mergulho: quando a adaptação é perfeita, a criança respira autonomia sem notar a estrutura de suporte.",
        "audio_texto": "Donald Winnicott defende que o sujeito se constitui a partir da mãe suficientemente boa e do ambiente facilitador."
    },
    {
        "autor": "Wilfred Bion",
        "papel": "Teorizador do Pensar",
        "tese": "A mente é um aparelho para pensar pensamentos. Elementos beta (sensações brutas) precisam ser metabolizados pela função alfa do analista em reverie.",
        "analogia": "O analista funciona como um estômago psíquico: recebe os detritos emocionais caóticos, metaboliza-os e os devolve em nutrientes pensáveis.",
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

# Menu Lateral com exatamente 3 Tópicos Principais
st.sidebar.markdown("### 🧠 Três Pilares de Estudo")
menu = st.sidebar.radio("Escolha o Módulo:", [
    "1. 🗺️ Mapa Central & Tribunal Teórico (com Áudio)", 
    "2. 🎯 Quiz Interativo (Simples e Complexo)", 
    "3. ⚖️ Painel de Perguntas aos Autores & Mediador"
])

st.markdown("<p class='main-header'>Plataforma Avançada de Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Ambiente integrado com mapas mentais, áudio funcional, quiz avaliativo e painel com mediação teórica.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- TÓPICO 1: MAPA CENTRAL & TRIBUNAL TEÓRICO COM ÁUDIO ---
if menu == "1. 🗺️ Mapa Central & Tribunal Teórico (com Áudio)":
    st.subheader("Pilar 1: Arquitetura Conceitual e Tribunal dos Autores")
    st.markdown("Explore a rede central da psicanálise e selecione os autores para ouvir suas defesas em áudio.")

    st.markdown("""
    <div class="mapa-central">
        🎯 NÚCLEO: PSICANÁLISE<br>
        <span style="font-size: 14px; font-weight: normal; color: #4A235A;">(Inconsciente, Conflito, Metapsicologia e Subjetividade)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗣️ Defesas Teóricas e Reprodução de Áudio")
    autor_selecionado = st.selectbox("Selecione o autor para analisar e ouvir:", [a["autor"] for a in base_autores])
    autor_data = next(a for a in base_autores if a["autor"] == autor_selecionado)

    st.markdown(f"""
    <div class="defesa-box">
        <h2>{autor_data['autor']}</h2>
        <p><strong>Papel:</strong> {autor_data['papel']}</p>
        <hr>
        <p style="font-size: 16px; line-height: 1.6;"><strong>A Defesa Teórica:</strong><br>"{autor_data['tese']}"</p>
        <div class="analogia-box">
            <strong>💡 Analogia Prática:</strong> "{autor_data['analogia']}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    safe_text = autor_data['audio_texto'].replace('"', '\\"')
    audio_component = f"""
    <div>
        <button onclick="
            const utterance = new SpeechSynthesisUtterance('{safe_text}');
            utterance.lang = 'pt-BR';
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(utterance);
        " style="background-color: #2E4053; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-size: 15px; font-weight: bold;">
            🔊 Reproduzir Áudio da Síntese
        </button>
    </div>
    """
    st.components.v1.html(audio_component, height=60)

# --- TÓPICO 2: QUIZ INTERATIVO (SIMPLES E COMPLEXO) COM CORREÇÃO ---
elif menu == "2. 🎯 Quiz Interativo (Simples e Complexo)":
    st.subheader("Pilar 2: Avaliação de Fixação (Questões Simples e Complexas)")
    st.markdown("Teste seu conhecimento teórico. Responda e clique no botão de correção de cada bloco.")

    st.markdown("### 🟢 Questão 1 (Nível Simples): Metapsicologia Básica")
    q1 = st.radio(
        "Qual instância do aparelho psíquico freudiano opera sob o Princípio do Prazer, exigindo descarga imediata?",
        ["A) Superego", "B) Ego", "C) Id"],
        key="q_simples"
    )
    if st.button("Corrigir Questão 1"):
        if q1.startswith("C)"):
            st.success("✅ **Correto!** O Id é o polo pulsional inconsciente regido pelo prazer imediato.")
        else:
            st.error("❌ **Incorreto.** Lembre-se de que o Id busca descarga imediata de energia pulsional.")

    st.markdown("---")

    st.markdown("### 🔴 Questão 2 (Nível Complexo): Teoria de Bion e Klein")
    q2 = st.radio(
        "Como Wilfred Bion conceitua a transição dos 'elementos beta' para os 'elementos alfa' na matriz analítica?",
        [
            "A) Através da repressão secundária exercida pelo superego sobre os traços mnêmicos visuais.",
            "B) Através da função alfa do analista (em estado de reverie) que metaboliza dados sensoriais brutos em pensamentos.",
            "C) Através da estagnação do estágio do espelho formulado pela linguística estrutural lacaniana."
        ],
        key="q_complexa"
    )
    if st.button("Corrigir Questão 2"):
        if q2.startswith("B)"):
            st.success("✅ **Excelente! Resposta Correta.** Bion demonstra que o aparelho para pensar pensamentos transforma a matéria tóxica bruta (beta) em pensamentos utilizáveis (alfa) via continente-conteúdo.")
        else:
            st.error("❌ **Incorreto.** Revise os conceitos de elementos beta e função alfa de Wilfred Bion.")

# --- TÓPICO 3: PAINEL DE PERGUNTAS AOS AUTORES & MEDIADOR ---
elif menu == "3. ⚖️ Painel de Perguntas aos Autores & Mediador":
    st.subheader("Pilar 3: Painel de Consulta aos Autores e Conclusão do Mediador")
    st.markdown("Digite uma dúvida clínica ou teórica. O sistema cruzará a perspectiva dos autores e um **Mediador Especialista** trará a síntese avaliada.")

    pergunta_usuario = st.text_input("Qual é a sua dúvida ou caso clínico para os autores?", "Como lidar com a angústia de separação e o vazio em um paciente?")

    if st.button("Consultar Painel e Mediador"):
        st.markdown("---")
        st.markdown(f"### 💬 Resposta Coletiva para: *'{pergunta_usuario}'*")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:12px; border-radius:6px; margin-bottom:10px;">
                <strong>Sigmund Freud:</strong><br>
                <em>"Analisaria isso sob o prisma da perda de objeto e da economia da libido, avaliando como o sujeito investe narcisicamente a falta e lida com o luto da separação através da angústia sinal."</em>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:12px; border-radius:6px; margin-bottom:10px;">
                <strong>Melanie Klein:</strong><br>
                <em>"Isso remete diretamente à angústia de aniquilação da posição esquizo-paranoide e à dor depressiva de perder o objeto amado por culpa ou destruição fantasiada."</em>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:12px; border-radius:6px; margin-bottom:10px;">
                <strong>Donald Winnicott:</strong><br>
                <em>"Encararia como uma falha no ambiente de sustentação (holding). O paciente precisa resgatar a capacidade criativa através do uso de áreas transicionais."</em>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:12px; border-radius:6px; margin-bottom:10px;">
                <strong>Wilfred Bion:</strong><br>
                <em>"Trata-se de um transbordamento de elementos beta não metabolizados. O analista precisa servir como continente para conter o caos emocional bruto."</em>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mediador-box">
            <h3>⚖️ Conclusão do Mediador Psicanalítico (Síntese Avançada)</h3>
            <p><strong>Avaliação do Especialista:</strong><br>
            Embora cada autor utilize um vocabulário clínico distinto (Freud focando na tópica econômica, Klein na dinâmica das posições primitivas, Winnicott na falha ambiental e Bion na metabolização de estímulos), todos convergem para o mesmo eixo central: <strong>o sofrimento psíquico surge na interface entre o sujeito e a alteridade (o outro/ambiente)</strong>.</p>
            <p><em>Orientação Prática para o Estudo:</em> Na clínica, o manejo não deve ser rígido; o analista transita entre ser o <em>continente</em> (Bion) para a dor bruta, o provedor de <em>holding</em> (Winnicott) para a regressão, e o intérprete do conflito pulsional (Freud/Klein).</p>
        </div>
        """, unsafe_allow_html=True)
