import streamlit as st
import time

# Configura a aba do navegador para ficar personalizada
st.set_page_config(page_title="Para a razão do meu sorriso", page_icon="❤️", layout="centered")

# Estilização básica para deixar o texto mais bonito (CSS centralizado)
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: 500;
        line-height: 1.6;
        color: #31333F;
    }
    .stTitle {
        color: #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Começa a página com suspense
st.title("Oi, meu amor. ❤️")
st.write("---")
st.markdown("<p class='big-font'>Eu criei este pequeno espaço digital só para nós dois. Demorou um pouquinho para programar, mas cada linha de código foi pensada em você.</p>", unsafe_allow_html=True)
st.markdown("<p class='big-font'>Há algo que eu preciso muito te dizer, do fundo do meu coração.</p>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# O botão que vai disparar a emoção
if st.button("Abra o seu coração e leia"):
    
    # Efeito de carregamento para criar uma pausa dramática
    with st.spinner('Preparando o que meu coração quer te dizer...'):
        time.sleep(2) # Espera 2 segundos
    
    # Efeito visual de confetes/balões
    st.balloons()
    
    st.write("---")
    
    # Título da Carta
    st.subheader("Minha vida,")

    # --- INÍCIO DA CARTA PROFUNDA ---
    # DICA: Edite os textos abaixo para personalizar com a história de vocês.
    
    carta = """
    <p class='big-font'>
    Eu sei que parece estranho receber um link e abrir um programinha no celular, mas a verdade é que eu não conseguia encontrar um jeito comum de te dizer tudo o que está entalado aqui no meu peito. Eu precisava criar algo novo, algo que fosse só nosso, para tentar traduzir o inexplicável.<br><br>

    Sabe, antes de você chegar, o mundo parecia seguir um roteiro meio cinza, meio automático. Eu vivia, mas não <i>sentia</i> com a intensidade que sinto hoje. Você não apenas entrou na minha vida; você acendeu as luzes, coloriu os dias e deu um novo sentido para a palavra 'felicidade'.<br><br>

    Eu sou completamente apaixonado pela pessoa que você é. Eu amo a sua força, o seu jeito de ver o mundo, e a forma como você consegue me acalmar apenas com o som da sua voz. Adoro observar os seus detalhes... como a sua expressão quando está concentrada, ou o jeito que você sorri. Cada pequena coisa em você me faz ter certeza de que eu tirei a sorte grande.<br><br>

    Amo a nossa história, desde o momento em que <b> te mandei a primeira mensagem naquele aplicativo</b> até os dias mais simples. É nos seus braços que eu encontrei o meu lugar seguro, o meu lar. Com você, eu não tenho medo do futuro, porque qualquer futuro que inclua você já é perfeito para mim.<br><br>

    Eu quero estar ao seu lado em cada conquista, segurar sua mão em cada dificuldade e envelhecer acumulando memórias lindas como as que já temos. Você é a minha escolha diária, o meu plano A, B e C, o amor da minha vida.<br><br>
    
    Obrigado por me permitir te amar e por me amar de volta. Eu te amo mais do que as palavras podem dizer, mais do que este código pode mostrar. Eu te amo com tudo o que eu sou.
    </p>
    """
    
    # Exibe a carta usando HTML para formatação
    st.markdown(carta, unsafe_allow_html=True)
    
    # Mensagem final destacada
    st.success("Para sempre vou te amar ❤️")
