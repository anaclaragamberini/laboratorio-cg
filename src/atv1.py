# Atividade 1 - Primeiro app Streamlit

import streamlit as st
import numpy as np

st.title("Computação Gráfica")
st.subheader("Atividade 1 - Setando o ambiente")

st.write("Nome: Ana Clara Gamberini")
st.write("Disciplina: Computação Gráfica")
st.write("Instituição: UniFil")

st.success("Meu primeiro aplicativo Streamlit está funcionando!")

st.divider()

st.subheader("Matriz Aleatória")

tamanho = st.slider(
    "Selecione o tamanho da matriz:",
    min_value=2,
    max_value=20,
    value=5
)

matriz = np.random.randint(
    0,
    256,
    size=(tamanho, tamanho)
)

st.write("Matriz gerada:")
st.write(matriz)

st.write("Representação visual da matriz:")
st.image(matriz.astype(np.uint8), clamp=True)