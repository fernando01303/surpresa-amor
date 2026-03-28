import streamlit as st
import time

# Configura a aba do navegador
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# Título e mensagem inicial
st.title("Oi, meu amor! ❤️")
st.write("Eu estava pensando em você e resolvi usar meus 'talentos de programação' para fazer algo diferente...")

st.write("Sabe por que você é tão especial para mim?")

# Cria um botão para ela clicar
if st.button("Clique aqui para descobrir!"):
    # Solta balões na tela (efeito do Streamlit)
    st.balloons()
    
    # Mensagem final que aparece após o clique
    st.success("Porque você faz todos os meus dias serem incrivelmente melhores! Eu te amo demais! 🥰")
    
    st.write("P.S.: Fiz esse programinha só pra te arrancar um sorriso hoje.")
