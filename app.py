import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Plataforma Multimídia de Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual avançada e suporte a cartões
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .card-estudo { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 6px solid #2471A3; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .mapa-central { background-color: #EBF5FB; padding: 20px; border-radius: 10px; border: 2px dashed #2980B9; text-align: center; font-weight: bold; font-size: 18px; color: #1B4F72; margin-bottom: 20px;}
    .exemplo-pratico { background-color: #F4ECF7; padding: 10px 15px; border-radius: 6px; border-left: 4px solid #8E44AD; margin-top: 10px; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# Base de Dados Completa com Exemplos Práticos e Textos de Áudio
base_autores_multimidia = [
    {
        "nome": "Sigmund Freud",
        "papel": "Fundador / Pai da Psicanálise",
        "conceito": "Inconsciente, Aparelho Psíquico (Id, Ego, Superego) e Repressão.",
        "exemplo": "Um profissional que sofre de exaustão crônica, mas se recusa a descansar porque o Superego exige perfeição constante, demonstrando o conflito entre o desejo inconsciente de pausa e a cobrança moral interna.",
        "audio_texto": "Sigmund Freud é o fundador da psicanálise. Seu foco central é o inconsciente e o aparelho psíquico dividido entre Id, Ego e Superego."
    },
    {
        "nome": "Melanie Klein",
        "papel": "Pioneira da Psicanálise Infantil e Relações Objetais",
        "conceito": "Posições Esquizo-paranoide e Depressiva, Fantasia Inconsciente.",
        "exemplo": "Uma pessoa que, ao menor sinal de erro de um colega de trabalho, passa a enxergá-lo como 'totalmente péssimo', refletindo a clivagem da posição esquizo-paranoide.",
        "audio_texto": "Melanie Klein reformulou as bases Kleinianas focando nas posições mentais primitivas e na fantasia inconsciente do bebê."
    },
    {
        "nome": "Donald Winnicott",
        "papel": "Escola Inglesa / Teoria do Amparo",
        "conceito": "Mãe Suficientemente Boa, Objeto Transicional e Falso Self.",
        "exemplo": "O uso de um cobertor de apego ou um objeto de conforto por uma criança (ou o ritual de café de um adulto) para aplacar a angústia de separação e transição.",
        "audio_texto": "Donald Winnicott destacou a importância do ambiente facilitador, cunhando o conceito de objeto transicional e falso self."
    },
    {
        "nome": "Wilfred Bion",
        "papel": "Teórico dos Processos Grupais e do Pensar",
        "conceito": "Função Alfa, Reverie e Elementos Beta.",
        "exemplo": "Um aluno que chega à sessão de treino extremamente ansioso e irritado sem motivo aparente; o treinador/terapeuta acolhe essa carga bruta (reverie) e a devolve organizada e calma.",
        "audio_texto": "Wilfred Bion estudou como a mente metaboliza dados sensoriais brutos, os elementos beta, transformando-os em pensamentos através da função alfa."
    },
    {
        "nome": "Jacques Lacan",
        "papel": "O Retorno a Freud (Estruturalismo)",
        "conceito": "O Inconsciente estruturado como linguagem, Estádio do Espelho e os Três Registros (RSI).",
        "exemplo": "Um lapso de linguagem (ato falhado) em uma reunião de negócios que revela exatamente o desejo oculto que a pessoa tentava esconder.",
        "audio_texto": "Jacques Lacan uniu a psicanálise à linguística, afirmando que o inconsciente é estruturado como uma linguagem."
    },
    {
        "nome": "André Green",
        "papel": "Psicanálise Contemporânea Francesa",
        "conceito": "Narcisismo de Morte e Afetos Negativos.",
        "exemplo": "Pacientes que entram em estados de apatia profunda e desligamento emocional diante de perdas, operando sob o esvaziamento do narcisismo.",
        "audio_texto": "André Green atualizou a metapsicologia para focar nas patologias do vazio e no narcisismo de morte."
    }
]

# Menu de Navegação na Barra Lateral
st.sidebar.markdown("### Navegação Multimídia")
menu = st.sidebar.radio("Escolha o Módulo:", [
    "🗺️ Mapa Central: Psicanálise & Autores", 
    "🃏 Cards de Estudo com Exemplos & Áudio", 
    "🎯 Quiz Interativo com Gabarito"
])

st.markdown("<p class='main-header'>🧠 Plataforma Multimídia de Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Estude com mapas conceituais estruturados, exemplos práticos do cotidiano e recursos de voz.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MÓDULO 1: MAPA MENTAL CENTRALIZADO ---
if menu == "🗺️ Mapa Central: Psicanálise & Autores":
    st.subheader("🗺️ Mapa Mental: A Psicanálise no Centro")
    st.markdown("Esquema visual interativo mostrando a irradiação dos conceitos a partir da matriz psicanalítica.")

    st.markdown("""
    <div class="mapa-central">
        🎯 PSICANÁLISE (O Inconsciente e a Dinâmica Subjetiva)
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏛️ Eixo Clássico / Fundacional")
        st.markdown("""
        - **Sigmund Freud** ➔ *Aparelho Psíquico & Pulsão*
        - **Melanie Klein** ➔ *Posições Psíquicas Primitivas*
        - **Donald Winnicott** ➔ *Ambiente & Objeto Transicional*
        - **Wilfred Bion** ➔ *Função Alfa & Continência*
        - **Jacques Lacan** ➔ *Incordiente como Linguagem*
        """)

    with col2:
        st.markdown("### 🌐 Eixo Contemporâneo")
        st.markdown("""
        - **André Green** ➔ *Narcisismo de Morte & Vazio*
        - **Thomas Ogden** ➔ *Terceiro Analítico Intersubjetivo*
        - **Christopher Bollas** ➔ *O Conhecido Não Pensado*
        - **Antonino Ferro** ➔ *O Analista como Co-criador*
        - **René Roussillon** ➔ *Impasses da Simbolização*
        """)

# --- MÓDULO 2: CARDS DE ESTUDO COM EXEMPLOS E ÁUDIO (TEXT-TO-SPEECH) ---
elif menu == "🃏 Cards de Estudo com Exemplos & Áudio":
    st.subheader("🃏 Cards de Estudo: Teoria + Exemplo Prático + Áudio")
    st.markdown("Cada card traz a síntese do autor, um exemplo real de como isso acontece e um player de voz embutido.")

    for i, item in enumerate(base_autores_multimidia):
        st.markdown(f"""
        <div class="card-estudo">
            <h3>{item['nome']}</h3>
            <p><strong>Papel:</strong> {item['papel']}</p>
            <p><strong>Conceito-Chave:</strong> {item['conceito']}</p>
            <div class="exemplo-pratico">
                <strong>💡 Exemplo Prático de Como Acontece:</strong> {item['exemplo']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Recurso nativo de HTML5 Audio/Speech para o celular e navegador falarem o texto estruturado
        # Usamos a API de síntese de fala integrada do navegador web (funciona perfeitamente em mobile e PC)
        safe_text = item['audio_texto'].replace("'", "").replace('"', "")
        audio_html = f"""
            <button onclick="
                var utterance = new SpeechSynthesisUtterance('{safe_text}');
                utterance.lang = 'pt-BR';
                window.speechSynthesis.speak(utterance);
            " style="background-color: #2E4053; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer; font-size: 14px; margin-bottom: 25px;">
                🔊 Ouvir Resumo em Áudio ({item['nome']})
            </button>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# --- MÓDULO 3: QUIZ COM GABARITO EXPLICATIVO ---
elif menu == "🎯 Quiz Interativo com Gabarito":
    st.subheader("🎯 Simulador de Fixação Teórica")
    
    q1 = st.radio(
        "1. Qual autor introduziu o conceito de 'Objeto Transicional' para descrever o item (como um paninho ou ursinho) que acolhe a angústia de separação do bebê?",
        ["A) Sigmund Freud", "B) Donald Winnicott", "C) Jacques Lacan", "D) André Green"],
        key="q_quiz_1"
    )
    if st.button("Conferir Resposta do Quiz"):
        if q1.startswith("B)"):
            st.success("✅ **Correto!** Winnicott criou o conceito de objeto transicional como a zona intermediária de experiência entre o bebê e o mundo externo.")
        else:
            st.error("❌ **Incorreto.** Revise os cards de Donald Winnicott.")
