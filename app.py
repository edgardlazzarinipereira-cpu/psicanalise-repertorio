import streamlit as st
import random

# Configuração da Página
st.set_page_config(
    page_title="Plataforma de Alta Performance em Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual refinada
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .defesa-box { background-color: #F8F9FA; padding: 22px; border-radius: 10px; border-left: 6px solid #2980B9; margin-bottom: 20px; }
    .analogia-box { background-color: #EBF5FB; padding: 14px 18px; border-radius: 6px; border-left: 4px solid #2471A3; margin-top: 15px; font-style: italic; color: #1B4F72; }
    .mapa-central { background-color: #F4ECF7; padding: 20px; border-radius: 10px; border: 2px dashed #8E44AD; text-align: center; font-weight: bold; font-size: 18px; color: #512E5F; margin-bottom: 20px;}
    .mediador-box { background-color: #EAFAF1; padding: 20px; border-radius: 10px; border-left: 6px solid #27AE60; margin-top: 15px; }
    .pratica-box { background-color: #FEF9E7; padding: 15px; border-radius: 8px; border-left: 5px solid #F39C12; margin-top: 12px; }
    </style>
""", unsafe_allow_html=True)

# 1. Base de Dados Completa e Aprofundada para o Tribunal Teórico
base_autores = [
    {
        "autor": "Sigmund Freud",
        "papel": "Fundador da Psicanálise",
        "tese": "O psiquismo humano não se reduz à consciência. O aparelho psíquico é estruturado em instâncias em perpétuo conflito econômico e tópico: o Id (pulsional), o Ego (mediador e defensivo) e o Superego (herdeiro da moral e da interdição). A repressão atua para afastar do consciente conteúdos intoleráveis, gerando formações substitutivas como os sintomas.",
        "analogia": "O psiquismo é como uma grande empresa gerindo uma caldeira de alta pressão: o Id produz a energia bruta e o vapor sem hora para parar; o Superego é a auditoria rígida que aplica multas morais severas; e o Ego é o diretor estressado que tenta equilibrar as contas para a empresa não explodir na superfície.",
        "audio_texto": "Sigmund Freud explica que o psiquismo é regido pelo conflito permanente entre Id, Ego e Superego, onde o inconsciente direciona nossa vida através de repressões e pulsões."
    },
    {
        "autor": "Melanie Klein",
        "papel": "Pioneira das Relações Objetais",
        "tese": "A mente infantil opera desde o início em um cenário de intensos impulsos de vida e de morte. O bebê organiza suas experiências em duas posições fundamentais: a esquizo-paranoide, marcada pela clivagem (objeto totalmente bom versus totalmente mau) e angústia persecutória; e a posição depressiva, onde integra o objeto, reconhecendo que quem frustra é o mesmo que ama, inaugurando a culpa e o desejo de reparação.",
        "analogia": "É como o mundo emocional de uma criança diante de um brinquedo complexo: ora o mundo é visto em estilhaços de aniquilação total, ora se integra quando se percebe que quem nutre é o mesmo que frustra.",
        "audio_texto": "Melanie Klein demonstra que a mente se organiza nas posições esquizo-paranoide e depressiva, lidando com clivagens, fantasias primitivas, culpa e reparação."
    },
    {
        "autor": "Donald Winnicott",
        "papel": "Teorizador do Amparo e Ambiente",
        "tese": "O indivíduo isolado não existe; a unidade estrutural básica é a relação dupla mãe-bebê. O desenvolvimento emocional saudável depende de um ambiente facilitador e de uma mãe suficientemente boa, capaz de prover sustentação física e emocional (holding), permitindo que o bebê experimente a ilusão de onipotência antes de lidar com as frustrações graduais da realidade.",
        "analogia": "O ambiente emocional funciona como o sistema de suporte de vida de um traje espacial: quando o ambiente opera com sintonia fina e invisível, o astronauta se move com total liberdade e desenvolve autonomia, sem perceber o complexo mecanismo que o mantém respirando a cada segundo.",
        "audio_texto": "Donald Winnicott enfatiza que o sujeito se constitui a partir do ambiente facilitador, da mãe suficientemente boa e do holding que ampara o desenvolvimento do Self."
    },
    {
        "autor": "Wilfred Bion",
        "papel": "Teorizador do Pensar e dos Grupos",
        "tese": "A mente é um aparelho concebido para pensar pensamentos. O ser humano nasce exposto a sensações e emoções brutas e indigestas — os elementos beta. Para que a mente se desenvolva, é imperativa a presença de um continente (função alfa do analista em estado de reverie) que acolha, metabolize e devolva esses elementos em uma forma pensável e metabolizada (elementos alfa).",
        "analogia": "O analista funciona como um sistema digestivo e metabolizador psíquico: ele recebe os detritos emocionais caóticos, metaboliza-os e os devolve em nutrientes pensáveis.",
        "audio_texto": "Wilfred Bion defende que a mente metaboliza dados sensoriais brutos chamados elementos beta em pensamentos utilizáveis através da função alfa e da reverie do analista."
    },
    {
        "autor": "Jacques Lacan",
        "papel": "O Retorno a Freud (Estruturalista)",
        "tese": "O inconsciente é estruturado como uma linguagem. O sujeito humano constitui-se a partir da alteridade radical do Grande Outro, alienando-se na cadeia de significantes. O desejo não é uma necessidade biológica pura, mas sim o 'desejo do Outro', articulado nas malhas da metáfora e da metonímia ao longo dos registros Real, Simbólico e Imaginário.",
        "analogia": "O ser humano é como um ator que entra em um palco onde o roteiro e a língua já foram escritos antes dele; nós falamos a linguagem, mas somos falados por ela.",
        "audio_texto": "Jacques Lacan postula que o inconsciente é estruturado como uma linguagem e que o sujeito se constitui na ordem simbólica enredado pelo desejo do Outro."
    }
]

# 2. Banco de Questões do Quiz
banco_quiz_total = [
    {
        "nivel": "🟢 Simples",
        "pergunta": "Qual instância do aparelho psíquico freudiano opera estritamente sob o Princípio do Prazer, exigindo descarga imediata?",
        "opcoes": ["A) Superego", "B) Ego", "C) Id"],
        "correta": "C) Id",
        "explicacao": "O Id é o reservatório pulsional inconsciente regido unicamente pelo princípio do prazer."
    },
    {
        "nivel": "🔴 Complexo",
        "pergunta": "Como Wilfred Bion conceitua a conversão dos 'elementos beta' em 'elementos alfa' no processo analítico?",
        "opcoes": [
            "A) Através da repressão secundária operada pelo superego.",
            "B) Através da função alfa e do estado de reverie do analista, que atuam como continência metabolizadora de dados sensoriais brutos.",
            "C) Através da fixação da libido no estádio do espelho lacaniano."
        ],
        "correta": "B) Através da função alfa e do estado de reverie do analista, que atuam como continência metabolizadora de dados sensoriais brutos.",
        "explicacao": "Bion demonstra que o analista empresta sua mente para metabolizar sensações brutas (beta) em pensamentos (alfa)."
    },
    {
        "nivel": "🟢 Simples",
        "pergunta": "O que caracteriza o conceito de 'Objeto Transicional' em Donald Winnicott?",
        "opcoes": [
            "A) Um objeto físico (como um cobertor) que ajuda o bebê a fazer a ponte entre a onipotência e a realidade externa.",
            "B) A representação mental rigorosa do pai durante o complexo de Édipo.",
            "C) Uma defesa neurótica contra a castração."
        ],
        "correta": "A) Um objeto físico (como um cobertor) que ajuda o bebê a fazer a ponte entre a onipotência e a realidade externa.",
        "explicacao": "O objeto transicional alivia a angústia de separação e constitui a primeira posse não-eu."
    },
    {
        "nivel": "🔴 Complexo",
        "pergunta": "Qual a principal diferença entre a concepção do Édipo em Freud e na teoria de Melanie Klein?",
        "opcoes": [
            "A) Freud defendia que o Édipo ocorre no primeiro mês, enquanto Klein dizia que na velhice.",
            "B) Freud situava o Édipo na fase fálica (4-5 anos); Klein demonstrou que as defesas e a culpa operam de forma muito mais precoce no primeiro ano de vida.",
            "C) Klein descartava completamente a sexualidade infantil."
        ],
        "correta": "B) Freud situava o Édipo na fase fálica (4-5 anos); Klein demonstrou que as defesas e a culpa operam de forma muito mais precoce no primeiro ano de vida.",
        "explicacao": "Klein antecipou cronologicamente a angústia edípica para as fases orais e anais primitivas."
    },
    {
        "nivel": "🟢 Simples",
        "pergunta": "O que Lacan quer dizer com a frase: 'O inconsciente é estruturado como uma linguagem'?",
        "opcoes": [
            "A) Que o inconsciente pode ser aprendido em dicionários.",
            "B) Que o inconsciente obedece a leis linguísticas (metáfora e metonímia) e opera através da cadeia significante.",
            "C) Que os sonhos são falhas gramaticais sem sentido."
        ],
        "correta": "B) Que o inconsciente obedece a leis linguísticas (metáfora e metonímia) e opera através da cadeia significante.",
        "explicacao": "Lacan utiliza a linguística estrutural para demonstrar que o inconsciente possui gramática própria."
    }
]

# Inicialização de estados na sessão
if "quiz_perguntas" not in st.session_state:
    st.session_state.quiz_perguntas = random.sample(banco_quiz_total, min(5, len(banco_quiz_total)))
if "historico_respostas" not in st.session_state:
    st.session_state.historico_respostas = []

# Menu Lateral Restrito aos 3 Pilares
st.sidebar.markdown("### 🧠 Três Pilares de Estudo")
menu = st.sidebar.radio("Escolha o Módulo:", [
    "1. 🗺️ Arquitetura & Tribunal Teórico (com Áudio)", 
    "2. 🎯 Quiz Dinâmico (Até 5 Perguntas & Histórico)", 
    "3. ⚖️ Painel de Consulta aos Autores & Mediador"
])

st.markdown("<p class='main-header'>Plataforma de Alta Performance em Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Ambiente de estudo avançado com áudio otimizado, quiz interativo e mediação clínica estruturada.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- TÓPICO 1: MAPA CENTRAL & TRIBUNAL TEÓRICO (COM ÁUDIO FUNCIONAL) ---
if menu == "1. 🗺️ Arquitetura & Tribunal Teórico (com Áudio)":
    st.subheader("Pilar 1: Arquitetura Conceitual e Tribunal dos Autores")
    st.markdown("Explore o núcleo da psicanálise e selecione os autores para examinar suas defesas teóricas aprofundadas com analogias e áudio.")

    st.markdown("""
    <div class="mapa-central">
        🎯 NÚCLEO: PSICANÁLISE<br>
        <span style="font-size: 14px; font-weight: normal; color: #4A235A;">(Inconsciente, Conflito, Metapsicologia e Subjetividade)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗣️ Defesas Teóricas Aprofundadas")
    autor_selecionado = st.selectbox("Selecione o autor para análise e áudio:", [a["autor"] for a in base_autores])
    autor_data = next(a for a in base_autores if a["autor"] == autor_selecionado)

    st.markdown(f"""
    <div class="defesa-box">
        <h2>{autor_data['autor']}</h2>
        <p><strong>Papel Histórico:</strong> {autor_data['papel']}</p>
        <hr>
        <p style="font-size: 16px; line-height: 1.6;"><strong>A Defesa Teórica:</strong><br>{autor_data['tese']}</p>
        <div class="analogia-box">
            <strong>💡 Analogia Explicativa:</strong> {autor_data['analogia']}
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
            🔊 Reproduzir Síntese em Áudio
        </button>
    </div>
    """
    st.components.v1.html(audio_component, height=60)

# --- TÓPICO 2: QUIZ DINÂMICO ---
elif menu == "2. 🎯 Quiz Dinâmico (Até 5 Perguntas & Histórico)":
    st.subheader("Pilar 2: Quiz de Fixação Dinâmico (Níveis Simples e Complexos)")
    st.markdown("Teste seus conhecimentos metapsicológicos. Responda às questões abaixo e verifique seu histórico.")

    col_btn1, col_btn2 = st.columns([2, 3])
    with col_btn1:
        if st.button("🔄 Trazer Novas Perguntas para o Quiz"):
            st.session_state.quiz_perguntas = random.sample(banco_quiz_total, min(5, len(banco_quiz_total)))
            st.rerun()

    st.markdown("---")

    for idx, q in enumerate(st.session_state.quiz_perguntas):
        st.markdown(f"### Q{idx+1} [{q['nivel']}] — {q['pergunta']}")
        resposta_usuario = st.radio("Escolha uma opção:", q["opcoes"], key=f"quiz_q_{idx}")
        
        if st.button(f"Corrigir Questão {idx+1}", key=f"btn_corrigir_{idx}"):
            acertou = resposta_usuario.startswith(q["correta"][:3])
            
            registro = {
                "pergunta": q["pergunta"],
                "escolha": resposta_usuario,
                "correta": q["correta"],
                "status": "Acertou ✅" if acertou else "Errou ❌"
            }
            st.session_state.historico_respostas.append(registro)

            if acertou:
                st.success(f"✅ **Correto!** {q['explicacao']}")
            else:
                st.error(f"❌ **Incorreto.** A alternativa correta é: **{q['correta']}**.\n\n*{q['explicacao']}*")
        st.markdown("---")

    if st.session_state.historico_respostas:
        with st.expander("📊 Ver Histórico de Respostas Acumulado na Sessão"):
            for h_idx, h in enumerate(st.session_state.historico_respostas):
                st.markdown(f"""
                **{h_idx+1}. {h['status']}**<br>
                *Questão:* {h['pergunta']}<br>
                *Sua resposta:* {h['escolha']}<br>
                *Gabarito:* {h['correta']}
                """, unsafe_allow_html=True)
                st.markdown("---")
            if st.button("🗑️ Limpar Histórico"):
                st.session_state.historico_respostas = []
                st.rerun()

# --- TÓPICO 3: PAINEL DE CONSULTA AOS AUTORES & MEDIADOR (COM ATUALIZAÇÃO CORRIGIDA) ---
elif menu == "3. ⚖️ Painel de Consulta aos Autores & Mediador":
    st.subheader("Pilar 3: Painel de Consulta Aprofundada e Mediação Clínica")
    st.markdown("Insira uma situação clínica ou dúvida conceitual. O painel cruzará as perspectivas aprofundadas dos autores, trará diretrizes de **como agir** e concluirá com a avaliação do mediador.")

    # Usando uma chave dinâmica associada a um botão de envio para forçar a atualização correta
    with st.form(key="form_consulta_autores"):
        pergunta_usuario = st.text_input(
            "Qual é a sua dúvida ou cenário clínico para análise do painel?", 
            value="Como manejar um paciente que apresenta angústia persecutória severa e recusa o vínculo?"
        )
        submit_button = st.form_submit_button(label="Consultar Painel Analítico e Mediador")

    # A lógica executa sempre que o formulário for submetido, capturando perfeitamente o novo texto
    if submit_button:
        st.markdown("---")
        st.markdown(f"### 💬 Análise Coletiva para: *'{pergunta_usuario}'*")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:15px; border-radius:8px; margin-bottom:12px;">
                <strong>Sigmund Freud:</strong><br>
                <em>"Analisaríamos a questão sob o eixo da neurose de defesa e da projeção. O paciente recusa o vínculo porque o material recalcado retorna sob forma persecutória, mobilizando defesas severas do Ego contra a angústia sinal."</em>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:15px; border-radius:8px; margin-bottom:12px;">
                <strong>Melanie Klein:</strong><br>
                <em>"Trata-se de uma recaída franca na posição esquizo-paranoide. O objeto externo está sendo clivado e vivido como persecutório devido à projeção massiva de impulsos destrutivos."</em>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:15px; border-radius:8px; margin-bottom:12px;">
                <strong>Donald Winnicott:</strong><br>
                <em>"Encaro isso como uma falha severa na sustentação ambiental originária. O paciente não suporta o vínculo porque o ambiente inicial foi falho, gerando um Falso Self defensivo."</em>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div style="background-color:#F2F4F4; padding:15px; border-radius:8px; margin-bottom:12px;">
                <strong>Wilfred Bion:</strong><br>
                <em>"Há um transbordamento maciço de elementos beta não metabolizados. O psiquismo do paciente está inundado de sensações brutas sem conseguir sonhá-las."</em>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="pratica-box">
            <h3>🧭 Diretriz Prática: Como Agir Diante de "{pergunta_usuario[:30]}..."</h3>
            <p><strong>Conduta Clínica Recomendada:</strong></p>
            <ul>
                <li><strong>Evite confrontações diretas:</strong> Não tente argumentar racionalmente contra conteúdos persecutórios em momentos de pico de angústia (Freud/Klein).</li>
                <li><strong>Exerça continência pura (Holding & Reverie):</strong> Sustenha o clima emocional de forma estável e previsível, servindo como continente para o caos (Winnicott/Bion).</li>
                <li><strong>Respeite o ritmo do sujeito:</strong> Valide a dor do isolamento defensivo antes de propor qualquer interpretação teórica aprofundada.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mediador-box">
            <h3>⚖️ Conclusão do Mediador Psicanalítico (Síntese Avançada)</h3>
            <p><strong>Avaliação do Especialista:</strong><br>
            A convergência entre os autores demonstra que situações de alta complexidade clínica não se resolvem por imposição teórica, mas pela <strong>escuta enraizada na transferência e na continência</strong>. Enquanto Freud e Klein identificam a raiz do conflito estrutural, Winnicott e Bion fornecem o mapa de atuação prática para que o analista suporte o peso do sofrimento psíquico do paciente.</p>
        </div>
        """, unsafe_allow_html=True)
