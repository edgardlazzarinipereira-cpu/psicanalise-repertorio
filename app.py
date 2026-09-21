import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Repositório Clínico & Conceitual: Psicanálise",
    page_icon="🧠",
    layout="wide"
)

# Estilização visual limpa
st.markdown("""
    <style>
    .main-header { font-size: 24px; font-weight: bold; color: #2C3E50; }
    .sub-header { font-size: 18px; color: #7F8C8D; }
    .card-box { background-color: #F8F9FA; padding: 15px; border-radius: 8px; border-left: 5px solid #2C3E50; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Base de Dados Acadêmica e Rigorosa (Autores, Obras Reais e Conceitos Centrais)
base_autores = [
    # --- CLÁSSICOS / PIONEIROS ---
    {
        "nome": "Sigmund Freud",
        "categoria": "Clássico",
        "obra": "A Interpretação dos Sonhos (1900) / Três Ensaios sobre a Teoria da Sexualidade (1905)",
        "conceito": "Inconsciente, Aparelho Psíquico (Id, Ego, Superego) e Pulsão.",
        "rigor_tecnico": "Estruturou a metapsicologia determinando que o psiquismo não se reduz à consciência, operando por processos primários e secundários."
    },
    {
        "nome": "Melanie Klein",
        "categoria": "Clássico",
        "obra": "A Psicanálise de Crianças (1932) / Inveja e Gratidão (1957)",
        "conceito": "Posições Psíquicas (Esquizo-paranoide e Depressiva) e Fantasia Inconsciente.",
        "rigor_tecnico": "Deslocou o foco para as relações objetais precoces e a vida fantasmática primitiva do bebê."
    },
    {
        "nome": "Carl Gustav Jung",
        "categoria": "Clássico",
        "obra": "Os Arquetipos e o Inconsciente Coletivo / A Dinâmica do Inconsciente",
        "conceito": "Inconsciente Coletivo, Arquétipos e Processo de Individuação.",
        "rigor_tecnico": "Propôs uma ampliação teleológica da psique para além da biografia individual, integrando dimensões mitológicas e estruturais universais."
    },
    {
        "nome": "Jacques Lacan",
        "categoria": "Clássico",
        "obra": "Escritos (1966) / O Seminário, Livro 11: Os Quatro Conceitos Fundamentais da Psicanálise",
        "conceito": "O Inconsciente estruturado como linguagem, Estádio do Espelho e os Três Registros (R-S-I).",
        "rigor_tecnico": "Retorno a Freud fundamentado na linguística estrutural (Saussure e Jakobson), resgatando o sujeito do desejo na cadeia significante."
    },
    {
        "nome": "Donald Winnicott",
        "categoria": "Clássico",
        "obra": "O Brincar e a Realidade (1971) / A Família e o Desenvolvimento Individual",
        "conceito": "Objeto Transicional, Mãe Suficientemente Boa e Falso Self.",
        "rigor_tecnico": "Enfatizou o papel do ambiente facilitador inicial na maturação do ego e na construção da capacidade de estar sozinho."
    },
    {
        "nome": "Sándor Ferenczi",
        "categoria": "Clássico",
        "obra": "Thalassa: Ensaio sobre a Teoria da Genitalidade / Diário Clínico (1932)",
        "conceito": "Técnica Ativa, Empatia Tátil/Afetiva e Trauma Precoce.",
        "rigor_tecnico": "Pioneiro na revisão da neutralidade dogmática, analisou a introjeção da culpa do adulto pela criança nos casos de abuso."
    },
    {
        "nome": "Wilfred Bion",
        "categoria": "Clássico",
        "obra": "Experiências com Grupos (1948) / O Crescer do Pensar (Learning from Experience, 1962)",
        "conceito": "Função Alfa, Reverie, Elementos Alfa e Beta, Continência.",
        "rigor_tecnico": "Modelou como a mente metaboliza dados sensoriais brutos e emoções não pensadas através da matriz intersubjetiva."
    },
    {
        "nome": "Anna Freud",
        "categoria": "Clássico",
        "obra": "O Ego e os Mecanismos de Defesa (1936)",
        "conceito": "Mecanismos de Defesa do Ego (repressão, projeção, sublimação, regressão, etc.).",
        "rigor_tecnico": "Sistematização rigorosa de como o ego se protege contra a angústia gerada por impulsos internos e exigências externas."
    },
    {
        "nome": "Alfred Adler",
        "categoria": "Clássico",
        "obra": "O Sentido da Vida / A Ciência da Natureza Humana",
        "conceito": "Psicologia Individual, Sentimento de Inferioridade e Estilo de Vida.",
        "rigor_tecnico": "Focou na finalidade do comportamento humano orientada a metas sociais e na superação compensatória de sentimentos de desvalia."
    },
    {
        "nome": "Erich Fromm",
        "categoria": "Clássico",
        "obra": "O Coração do Homem (1964) / A Arte de Amar (1956)",
        "conceito": "Psicanálise Humanista, Mecanismos de Fuga da Libertad e Caráter Social.",
        "rigor_tecnico": "Articulou a psicanálise freudiana com a sociologia marxista para analisar o impacto das estruturas socioeconômicas no psiquismo."
    },

    # --- CONTEMPORÂNEOS ---
    {
        "nome": "André Green",
        "categoria": "Contemporâneo",
        "obra": "O Complexo de Vida / Complexo de Morte (1983) / A Diacronia do Negativo",
        "conceito": "Narcisismo de Morte, Afetos Negativos, Trabalho do Negativo.",
        "rigor_tecnico": "Atualizou a metapsicologia para dar conta de patologias do vazio e estados limites (borderline) onde a simbolização falha."
    },
    {
        "nome": "Thomas Ogden",
        "categoria": "Contemporâneo",
        "obra": "Os Sujeitos da Psicanálise (1994) / No Limiar do Sonho",
        "conceito": "Terceiro Analítico Intersubjetivo e Experiência de Sonhar a Própria Experiência.",
        "rigor_tecnico": "Foco na matriz relacional gerada na sessão, onde analista e paciente co-criam uma nova realidade psíquica."
    },
    {
        "nome": "Joyce McDougall",
        "categoria": "Contemporâneo",
        "obra": "Teatros do Eu (Theatres of the Body, 1989 / Theatres of the Mind)",
        "conceito": "Psicossomática psicanalítica, Neossexualidades e Soluções Asfixiantes.",
        "rigor_tecnico": "Estudo de como o corpo se torna um palco de encenação para conflitos que a mente falhou em traduzir em palavras."
    },
    {
        "nome": "Antonino Ferro",
        "categoria": "Contemporâneo",
        "obra": "A Técnica na Psicanálise (1996) / Evitar as Emoções, Experienciar as Emoções",
        "conceito": "O Campo Analítico, O Analista como Personagem e Narrativas Possíveis.",
        "rigor_tecnico": "Abordagem bioniana que transforma o analista em um metabolizador de narrativas abertas em vez de um intérprete dogmático de verdades ocultas."
    },
    {
        "nome": "Piera Aulagnier",
        "categoria": "Contemporâneo",
        "obra": "O Aprendiz de Historizador: Da Orelha ao Escrito (1984)",
        "conceito": "Violência da Interpretação, Pictograma e Construção do Eu.",
        "rigor_tecnico": "Investigação rigorosa sobre como o psiquismo infantil é enquadrado pelo discurso materno e institucional."
    },
    {
        "nome": "Christopher Bollas",
        "categoria": "Contemporâneo",
        "obra": "A Sombra do Objeto: Psicanálise do Conhecido Não Pensado (1987)",
        "conceito": "O Conhecido Não Pensado, Idioma Psíquico e Normose.",
        "rigor_tecnico": "Exploração dos registos estéticos e experienciais anteriores à nomeação verbal na clínica contemporânea."
    },
    {
        "nome": "Stephen Mitchell & Jay Greenberg",
        "categoria": "Contemporâneo",
        "obra": "A Relação de Objeto na Teoria Psicanalítica (1983 - Mitchell & Greenberg) / Relações Objetais na Psicanálise (Mitchell)",
        "conceito": "Matriz Relacional, Integração Pulsão vs. Relação.",
        "rigor_tecnico": "Fundadores da Psicanálise Relacional Norte-Americana, unificando a teoria dos drives com a matriz intersubjetiva."
    },
    {
        "nome": "Silvia Bleichmar",
        "categoria": "Contemporâneo",
        "obra": "A Fundamentação do Sujeito Psíquico (1993) / Violência Social, Violência Psíquica",
        "conceito": "Constituição do Sujeito, Metapsicologia Revisitada e Desnaturalização da Violência.",
        "rigor_tecnico": "Articulação complexa entre a metapsicologia freudiana e o materialismo histórico, focando na produção social da subjetividade."
    },
    {
        "nome": "René Roussillon",
        "categoria": "Contemporâneo",
        "obra": "O Platô da Simbolização (2001) / Paradojas y Situaciones Fronterizas",
        "conceito": "Trabalho de Simbolização, Sofrimento Narcísico-Identitário e Angústia de Desamparo.",
        "rigor_tecnico": "Investigação clínica sobre falhas primárias de simbolização e o manejo de pacientes com fraturas na identidade básica."
    },
    {
        "nome": "Fernando Urribarri",
        "categoria": "Contemporâneo",
        "obra": "O Campo da Psicanálise Contemporânea / Ensaios sobre André Green e a Clínica Atual",
        "conceito": "Metapsicologia Ampliada, Contemporaneidade e Complexidade Clínica.",
        "rigor_tecnico": "Sistematização teórica voltada para os dilemas da clínica atual frente às mutações dos laços sociais e subjetivos modernos."
    }
]

# Interface do App
st.markdown("<p class='main-header'>🧠 Repositório Acadêmico & Clínico: Psicanálise</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Consulta oficial de autores, obras primárias validadas e rigor metapsicológico para aplicação estruturada.</p>", unsafe_allow_html=True)
st.markdown("---")

# Filtro lateral para navegação
st.sidebar.header("Filtros de Consulta")
filtro_categoria = st.sidebar.selectbox("Filtrar por Categoria Teórica:", ["Todos", "Clássico", "Contemporâneo"])
busca_termo = st.sidebar.text_input("Pesquisar Autor ou Conceito:")

# Processamento de Filtros
autores_filtrados = base_autores
if filtro_categoria != "Todos":
    autores_filtrados = [a for a in autores_filtrados if a["categoria"] == filtro_categoria]

if busca_termo:
    autores_filtrados = [a for a in autores_filtrados if busca_termo.lower() in a["nome"].lower() or busca_termo.lower() in a["conceito"].lower() or busca_termo.lower() in a["obra"].lower()]

# Exibição dos Dados
st.markdown(f"### Exibindo {len(autores_filtrados)} registros cadastrados")

for autor in autores_filtrados:
    st.markdown(f"""
    <div class="card-box">
        <strong>{autor['nome']}</strong> &nbsp;|&nbsp; <em>Categoria: {autor['categoria']}</em><br>
        <strong>📚 Obra(s) de Referência:</strong> {autor['obra']}<br>
        <strong>🔑 Conceitos Centrais:</strong> {autor['conceito']}<br>
        <strong>⚙️ Rigor Técnico / Enquadre:</strong> {autor['rigor_tecnico']}
    </div>
    """, unsafe_allow_html=True)

# Rodapé informativo
st.markdown("---")
st.caption("Repositório desenvolvido sob rigor epistemológico estrito: separação estrita entre lentes de mecanismo (ciências biológicas) e de sentido (psicanálise). Sem achismos.")
