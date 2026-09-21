import streamlit as st
import random

# Configuração da Página
st.set_page_config(
    page_title="Plataforma de Estudo: Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual
st.markdown("""
    <style>
    .main-header { font-size: 26px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 16px; color: #7F8C8D; }
    .card-box { background-color: #F8F9FA; padding: 15px; border-radius: 8px; border-left: 5px solid #2C3E50; margin-bottom: 10px; }
    .estudo-box { background-color: #EBF5FB; padding: 20px; border-radius: 10px; border: 1px solid #AED6F1; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Base de Dados Acadêmica Completa
base_autores = [
    # --- CLÁSSICOS / PIONEIROS ---
    {
        "nome": "Sigmund Freud",
        "categoria": "Clássico",
        "obra": "A Interpretação dos Sonhos (1900) / Três Ensaios sobre a Teoria da Sexualidade (1905)",
        "conceito": "Inconsciente, Aparelho Psíquico (Id, Ego, Superego) e Pulsão.",
        "rigor_tecnico": "Estruturou a metapsicologia determinando que o psiquismo não se reduz à consciência, operando por processos primários e secundários.",
        "pergunta_estudo": "Qual a diferença estrutural de funcionamento entre o Id e o Superego no modelo freudiano?",
        "resposta_estudo": "O Id opera pelo princípio do prazer buscando descarga imediata de impulsos primitivos; o Superego atua como a moral internalizada, exigindo ideal e operando muitas vezes com culpa punitiva."
    },
    {
        "nome": "Melanie Klein",
        "categoria": "Clássico",
        "obra": "A Psicanálise de Crianças (1932) / Inveja e Gratidão (1957)",
        "conceito": "Posições Psíquicas (Esquizo-paranoide e Depressiva) e Fantasia Inconsciente.",
        "rigor_tecnico": "Deslocou o foco para as relações objetais precoces e a vida fantasmática primitiva do bebê.",
        "pergunta_estudo": "O que caracteriza a transição da posição esquizo-paranoide para a posição depressiva em Klein?",
        "resposta_estudo": "Na esquizo-paranoide o objeto é clivado (totalmente bom ou totalmente mau) e impera a angústia de aniquilação. Na depressiva, a criança reconhece que o objeto bom e o mau são o mesmo, surgindo a culpa e o desejo de reparação."
    },
    {
        "nome": "Carl Gustav Jung",
        "categoria": "Clássico",
        "obra": "Os Arquetipos e o Inconsciente Coletivo / A Dinâmica do Inconsciente",
        "conceito": "Inconsciente Coletivo, Arquétipos e Processo de Individuação.",
        "rigor_tecnico": "Propôs uma ampliação teleológica da psique para além da biografia individual, integrando dimensões mitológicas e estruturais universais.",
        "pergunta_estudo": "Como o Inconsciente Coletivo de Jung se difere do inconsciente freudiano?",
        "resposta_estudo": "Enquanto o inconsciente em Freud é predominantemente pessoal (reprimidos da biografia do sujeito), o inconsciente coletivo de Jung é herdado, estrutural e comum a toda a humanidade, povoado por arquétipos."
    },
    {
        "nome": "Jacques Lacan",
        "categoria": "Clássico",
        "obra": "Escritos (1966) / O Seminário, Livro 11: Os Quatro Conceitos Fundamentais da Psicanálise",
        "conceito": "O Inconsciente estruturado como linguagem, Estádio do Espelho e os Três Registros (R-S-I).",
        "rigor_tecnico": "Retorno a Freud fundamentado na linguística estrutural (Saussure e Jakobson), resgatando o sujeito do desejo na cadeia significante.",
        "pergunta_estudo": "O que significa a célebre premissa lacaniana de que 'o inconsciente é estruturado como uma linguagem'?",
        "resposta_estudo": "Significa que o inconsciente não é um depósito animalesco de instintos brutos, mas opera obedecendo às leis linguísticas da metáfora e da metonímia na cadeia de significantes."
    },
    {
        "nome": "Donald Winnicott",
        "categoria": "Clássico",
        "obra": "O Brincar e a Realidade (1971) / A Família e o Desenvolvimento Individual",
        "conceito": "Objeto Transicional, Mãe Suficientemente Boa e Falso Self.",
        "rigor_tecnico": "Enfatizou o papel do ambiente facilitador inicial na maturação do ego e na construção da capacidade de estar sozinho.",
        "pergunta_estudo": "Qual é a função clínica e evolutiva do 'Objeto Transicional'?",
        "resposta_estudo": "É a primeira posse não-eu da criança (como um cobertor ou ursinho). Ele acolhe a angústia da separação da mãe e cria uma zona intermediária de experiência entre a realidade interna e externa."
    },
    {
        "nome": "Wilfred Bion",
        "categoria": "Clássico",
        "obra": "Experiências com Grupos (1948) / O Crescer do Pensar (Learning from Experience, 1962)",
        "conceito": "Função Alfa, Reverie, Elementos Alfa e Beta, Continência.",
        "rigor_tecnico": "Modelou como a mente metaboliza dados sensoriais brutos e emoções não pensadas através da matriz intersubjetiva.",
        "pergunta_estudo": "O que são 'Elementos Beta' na teoria bioniana e como eles se transformam?",
        "resposta_estudo": "São impressões sensoriais brutas e emoções não metabolizadas (fatos indigeríveis). Através da função alfa (da mãe ou do analista via reverie), eles são transformados em elementos alfa, tornando-se pensáveis."
    },
    {
        "nome": "Anna Freud",
        "categoria": "Clássico",
        "obra": "O Ego e os Mecanismos de Defesa (1936)",
        "conceito": "Mecanismos de Defesa do Ego (repressão, projeção, sublimação, regressão, etc.).",
        "rigor_tecnico": "Sistematização rigorosa de como o ego se protege contra a angústia gerada por impulsos internos e exigências externas.",
        "pergunta_estudo": "Qual a diferença primária entre repressão e negação segundo Anna Freud?",
        "resposta_estudo": "A repressão empurra um conteúdo inaceitável para fora da consciência (esquecimento defensivo). A negação atua sobre um dado da realidade externa evidente que o ego se recusa a admitir como existente."
    },
    # --- CONTEMPORÂNEOS ---
    {
        "nome": "André Green",
        "categoria": "Contemporâneo",
        "obra": "O Complexo de Vida / Complexo de Morte (1983) / A Diacronia do Negativo",
        "conceito": "Narcisismo de Morte, Afetos Negativos, Trabalho do Negativo.",
        "rigor_tecnico": "Atualizou a metapsicologia para dar conta de patologias do vazio e estados limites (borderline) onde a simbolização falha.",
        "pergunta_estudo": "O que caracteriza o conceito de 'Narcisismo de Morte' formulado por André Green?",
        "resposta_estudo": "É um investimento narcísico voltado para o esvaziamento, para a desobjetalização e para o silenciamento dos afetos, diferindo do narcisismo de vida que busca ligar e investir o objeto."
    },
    {
        "nome": "Thomas Ogden",
        "categoria": "Contemporâneo",
        "obra": "Os Sujeitos da Psicanálise (1994) / No Limiar do Sonho",
        "conceito": "Terceiro Analítico Intersubjetivo e Experiência de Sonhar a Própria Experiência.",
        "rigor_tecnico": "Foco na matriz relacional gerada na sessão, onde analista e paciente co-criam uma nova realidade psíquica.",
        "pergunta_estudo": "O que é o 'Terceiro Analítico' na perspectiva de Thomas Ogden?",
        "resposta_estudo": "É uma nova entidade intersubjetiva gerada na sessão pela união única entre a subjetividade do analista e a do paciente, funcionando como um gerador de significados que nenhum dos dois criaria sozinho."
    },
    {
        "nome": "Christopher Bollas",
        "categoria": "Contemporâneo",
        "obra": "A Sombra do Objeto: Psicanálise do Conhecido Não Pensado (1987)",
        "conceito": "O Conhecido Não Pensado, Idioma Psíquico e Normose.",
        "rigor_tecnico": "Exploração dos registos estéticos e experienciais anteriores à nomeação verbal na clínica contemporânea.",
        "pergunta_estudo": "O que Bollas define como 'O Conhecido Não Pensado'?",
        "resposta_estudo": "São experiências formativas precoces e impressões existenciais que foram vividas e registradas pelo corpo e pelo psiquismo, mas que ainda não ganharam forma verbal ou conceitual na mente."
    }
]

# Menu de Navegação na Barra Lateral
st.sidebar.markdown("### Navegação")
menu = st.sidebar.radio("Escolha o Modo:", ["📚 Consulta de Autores & Obras", "🧠 Modo Estudo (Flashcards Ativos)", "🎯 Quiz de Fixação"])

st.markdown("<p class='main-header'>🧠 Plataforma de Estudos: Psicanálise & Metapsicologia</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Ambiente interativo estruturado com bibliografia primária, rigor clínico e conceitos contemporâneos.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- MODO 1: CONSULTA ---
if menu == "📚 Consulta de Autores & Obras":
    st.subheader("Biblioteca de Autores e Fundamentos")
    
    filtro_cat = st.selectbox("Filtrar Categoria:", ["Todos", "Clássico", "Contemporâneo"])
    pesquisa = st.text_input("Pesquisar autor, conceito ou obra:")
    
    dados = base_autores
    if filtro_cat != "Todos":
        dados = [d for d in dados if d["categoria"] == filtro_cat]
    if pesquisa:
        dados = [d for d in dados if pesquisa.lower() in d["nome"].lower() or pesquisa.lower() in d["conceito"].lower() or pesquisa.lower() in d["obra"].lower()]

    for item in dados:
        st.markdown(f"""
        <div class="card-box">
            <strong>{item['nome']}</strong> ({item['categoria']})<br>
            <strong>📚 Obras:</strong> {item['obra']}<br>
            <strong>🔑 Conceitos:</strong> {item['conceito']}<br>
            <strong>⚙️ Rigor Técnico:</strong> {item['rigor_tecnico']}
        </div>
        """, unsafe_allow_html=True)

# --- MODO 2: FLASHCARDS DE ESTUDO ATIVO ---
elif menu == "🧠 Modo Estudo (Flashcards Ativos)" :
    st.subheader("Flashcards de Treinamento Metapsicológico")
    st.markdown("Teste sua retenção conceitual antes de abrir a resposta oficial do autor.")

    # Inicializar estado da sessão para randomizar ou navegar
    if "card_idx" not in st.session_state:
        st.session_state.card_idx = 0

    autor_atual = base_autores[st.session_state.card_idx]

    st.markdown(f"""
    <div class="estudo-box">
        <h3>Cartão {st.session_state.card_idx + 1} de {len(base_autores)}</h3>
        <p><strong>Autor de Referência:</strong> {autor_atual['nome']} ({autor_atual['categoria']})</p>
        <p><strong>Obra Base:</strong> {autor_atual['obra']}</p>
        <hr>
        <h4>❓ Pergunta Conceitual:</h4>
        <p style="font-size: 18px; font-weight: bold; color: #1B4F72;">{autor_atual['pergunta_estudo']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Botão para revelar resposta
    mostrar_resp = st.checkbox("Revelar Resposta Técnica", key=f"check_{st.session_state.card_idx}")
    
    if mostrar_resp:
        st.success(f"**Gabarito Metapsicológico:** {autor_atual['resposta_estudo']}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Autor Anterior"):
            st.session_state.card_idx = (st.session_state.card_idx - 1) % len(base_autores)
            st.rerun()
    with col2:
        if st.button("Próximo Autor ➡️"):
            st.session_state.card_idx = (st.session_state.card_idx + 1) % len(base_autores)
            st.rerun()

# --- MODO 3: QUIZ DE FIXAÇÃO ---
elif menu == "🎯 Quiz de Fixação":
    st.subheader("Simulador de Avaliação Teórica")
    st.markdown("Valide o seu entendimento cruzando conceitos teóricos fundamentais.")

    # Questão 1 do Quiz
    q1 = st.radio("1. Na metapsicologia freudiana, qual instância do aparelho psíquico opera predominantemente sob o Princípio do Prazer?", 
                  ["Superego", "Ego", "Id", "Inconsciente Coletivo"])
    
    if st.button("Corrigir Questão 1"):
        if q1 == "Id":
            st.success("Correto! O Id é o polo pulsional do aparelho psíquico regido inteiramente pelo princípio do prazer.")
        else:
            st.error("Incorreto. Revise os conceitos de Freud sobre o funcionamento do Id.")

    st.markdown("---")
    
    # Questão 2 do Quiz
    q2 = st.radio("2. O conceito de 'Função Alfa' e 'Reverie' pertence a qual grande autor da psicanálise?", 
                  ["Jacques Lacan", "Wilfred Bion", "Melanie Klein", "Donald Winnicott"])
    
    if st.button("Corrigir Questão 2"):
        if q2 == "Wilfred Bion":
            st.success("Correto! Bion desenvolveu a teoria do pensar focando na metabolização de elementos beta em alfa através da continência.")
        else:
            st.error("Incorreto. Esse é um pilar fundamental da obra de Wilfred Bion.")
