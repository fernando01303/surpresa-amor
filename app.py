import streamlit as st
import random

# Configura a aba do navegador
st.set_page_config(page_title="Para a razão do meu sorriso", page_icon="❤️", layout="centered")

# --- CSS PERSONALIZADO (A MÁGICA ESTÁ AQUI) ---
# Este bloco define como o texto e a animação de corações funcionam.
custom_css = """
<style>
/* Centraliza e embeleza o texto principal */
.stMarkdown {
    font-size: 20px !important;
    font-weight: 500;
    line-height: 1.6;
    color: #31333F;
    text-align: center;
}
.stTitle {
    color: #ff4b4b;
    text-align: center;
}

/* Define a animação dos corações lentos */
@keyframes coracoesLentos {
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}

/* Estila cada coração individual */
.coracao {
    position: fixed;
    bottom: -10px;
    font-size: 24px;
    color: #ff4b4b;
    user-select: none;
    pointer-events: none;
    animation: coracoesLentos linear infinite;
    /* Velocidade LENTA: 10 a 15 segundos para subir */
    animation-duration: calc(10s + (5s * var(--sorte-velocidade)));
}

/* Container para segurar os corações */
#container-coracoes {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    z-index: 999; /* Garante que fiquem na frente */
}
</style>
"""
# Injeta o CSS
st.markdown(custom_css, unsafe_allow_html=True)


# --- LÓGICA DO PROGRAMA ---

# Começa a página com suspense
st.title("Oi, meu amor. ❤️")
st.write("---")
st.markdown("Eu criei este pequeno espaço digital só para nós dois. Demorou um pouquinho para programar, mas cada linha de código foi pensada em você.")
st.markdown("Há algo que eu preciso muito te dizer, do fundo do meu coração.")

st.write(" ")
st.write(" ")

# Variável para controlar se os corações devem aparecer
if 'mostrar_coracoes' not in st.session_state:
    st.session_state.mostrar_coracoes = False

# O botão que ela clica
if st.button("Abra o seu coração e leia"):
    st.session_state.mostrar_coracoes = True

# --- EXIBE A ANIMAÇÃO E A CARTA SE O BOTÃO FOI CLICADO ---
if st.session_state.mostrar_coracoes:
    
    # --- GERAÇÃO HTML DOS CORAÇÕES ---
    # Cria 30 corações com posições e velocidades levemente aleatórias
    coracoes_html = '<div id="container-coracoes">'
    for i in range(30):
        posicao_horizontal = random.uniform(0, 100) # Posição X (0-100%)
        atraso_inicial = random.uniform(0, 5) # Atraso para começar (0-5s)
        # Sorteia uma variação de velocidade para misturar (será usada pelo CSS)
        sorte_velocidade = random.uniform(0, 1) 
        
        coracoes_html += f'<span class="coracao" style="left: {posicao_horizontal}vw; animation-delay: {atraso_inicial}s; --sorte-velocidade: {sorte_velocidade};">❤️</span>'
    coracoes_html += '</div>'
    
    # Injeta o HTML dos corações na tela
    st.markdown(coracoes_html, unsafe_allow_html=True)
    
    
    # --- CARTA PROFUNDA ---
    st.write("---")
    st.subheader("Minha vida,")

    carta = """
    <p class='big-font' style='text-align: justify;'>
    Eu sei que parece estranho receber um link e abrir um programinha no celular, mas a verdade é que eu não conseguia encontrar um jeito comum de te dizer tudo o que está entalado aqui no meu peito. Eu precisava criar algo novo, algo que fosse só nosso, para tentar traduzir o inexplicável.<br><br>

    Sabe, antes de você chegar, o mundo parecia seguir um roteiro meio cinza, meio automático. Eu vivia, mas não <i>sentia</i> com a intensidade que sinto hoje. Você não apenas entrou na minha vida; você acendeu as luzes, coloriu os dias e deu um novo sentido para a palavra 'felicidade'.<br><br>

    Eu sou completamente apaixonado pela pessoa que você é. Eu amo a sua força, o seu jeito de ver o mundo, e a forma como você consegue me acalmar apenas com o som da sua voz. Adoro observar os seus detalhes... como a sua expressão quando está concentrada, ou o jeito que você sorri quando <b>[coloque aqui um detalhe fofo, ex: 'toma café' ou 'vê um gatinho']</b>. Cada pequena coisa em você me faz ter certeza de que eu tirei a sorte grande.<br><br>

    Amo a nossa história, desde o momento em que <b>[cite uma memória curta, ex: 'nos vimos pela primeira vez naquele bar']</b> até os dias mais simples, preguiçosos no sofá. É nos seus braços que eu encontrei o meu lugar seguro, o meu lar. Com você, eu não tenho medo do futuro, porque qualquer futuro que inclua você já é perfeito para mim.<br><br>

    Eu quero estar ao seu lado em cada conquista, segurar sua mão em cada dificuldade e envelhecer acumulando memórias lindas como as que já temos. Você é a minha escolha diária, o meu plano A, B e C, o amor da minha vida.<br><br>
    
    Obrigado por me permitir te amar e por me amar de volta. Eu te amo mais do que as palavras podem dizer, mais do que este código pode mostrar. Eu te amo com tudo o que eu sou.
    </p>
    """
    st.markdown(carta, unsafe_allow_html=True)
    st.success("Para sempre seu. ❤️")
